'''
Using the app: Physics Toolbox Sensor Suite
The Sensor Collection Rate: 205Hz
'''
import sys
import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

FS = 205	# The Sensor Collection Rate: 205Hz
CUTOFF = 5	# Assume the fastest frequency is 5 steps per second
ORDER = 3	# The ORDER of butterworth filter
	
def get_velocity(peaks, data, time):
	v = []
	for i in np.arange(peaks.size-1):
		v.append(np.trapz(data[peaks[i]:peaks[i+1]], time[peaks[i]:peaks[i+1]]))
	velocity = np.mean(v)
	return velocity

def get_peaks(data):
	peaks, _ = find_peaks(data)
	npeaks, _ = find_peaks(-data)
	peaks = peaks[data[peaks] > np.mean(data[peaks])]
	to_be_deleted = []
	for i in np.arange(peaks.size-1):
		mins = np.min(data[peaks[i]:peaks[i+1]])
		if(mins > np.mean(data[npeaks])):
			to_be_deleted.append(i+1)
	real_peaks = np.delete(peaks, to_be_deleted)
	return real_peaks

def butter_filter(df):
	normal_cutoff = CUTOFF / (0.5 * FS)
	b, a = signal.butter(3, normal_cutoff, btype='low', analog=False)
	x = signal.filtfilt(b, a, df['ax'])
	y = signal.filtfilt(b, a, df['ay'])
	z = signal.filtfilt(b, a, df['az'])
	return x, y, z

def plot_origin(df):
	plt.figure(figsize=(30, 15))
	plt.subplot(3, 1, 1)
	plt.plot(df['time'].values, df['ax'], 'r.')	#forward, backward []
	plt.title('X-axis: forward, backward', fontsize=20)
	plt.xlim(50, 70)
	plt.grid()

	plt.subplot(3, 1, 2)
	plt.plot(df['time'].values, df['ay'], 'g.')	#up, down [-1, 1.5]
	plt.title('Y-axis: up, down', fontsize=20)
	plt.xlim(50, 70)
	plt.grid()

	plt.subplot(3, 1, 3)
	plt.plot(df['time'].values, df['az'], 'b.')	#left, right [-1, 1]
	plt.title('Z-axis: left, right', fontsize=20)
	plt.xlim(50, 70)
	plt.grid()
	plt.savefig('images/Origin_Data.png')
	# plt.show()
	plt.close()

def plot_butter_filtered(time, x, y, z):
	plt.figure(figsize=(30, 15))
	plt.subplot(3, 1, 1)
	plt.plot(time, x, 'r-', linewidth=3)
	plt.title('X-axis: forward, backward', fontsize=20)
	plt.xlim(50, 70)
	plt.grid()

	plt.subplot(3, 1, 2)
	plt.plot(time, y, 'g-', linewidth=3)
	plt.title('Y-axis: forward, backward', fontsize=20)
	plt.xlim(50, 70)
	plt.grid()

	plt.subplot(3, 1, 3)
	plt.plot(time, z, 'b-', linewidth=3)
	plt.title('Z-axis: forward, backward', fontsize=20)
	plt.xlim(50, 70)
	plt.grid()
	plt.savefig('images/Filtered_data.png')
	# plt.show()
	plt.close()

def plot_ff(time, data, freq, FF):
	plt.figure(figsize=(30, 15))
	plt.subplot(2, 1, 1)
	plt.plot(time, data, 'b')
	plt.title('Time Domain', fontsize=20)
	plt.subplot(2, 1, 2)
	plt.plot(freq, FF, 'r')
	plt.title('Frequency Domain', fontsize=20)
	plt.savefig('images/Fourier_Transform.png')
	# plt.show()
	plt.close()

def plot_peak(time, data, peak):
	plt.figure(figsize=(30, 15))
	plt.plot(time, data, 'b-', linewidth=3)
	plt.plot(time[peak], data[peak], "r*", ms=15)
	plt.xlim(50, 70)
	plt.title('Peaks', fontsize=20)
	plt.savefig('images/Peaks.png')
	# plt.show()
	plt.close()

def main(infile):
	df = pd.read_csv(infile)
	plot_origin(df)

	# Using butterworth low pass filter
	low_passed_x, low_passed_y, low_passed_z = butter_filter(df)
	df['low_passed_x'] = low_passed_x
	plot_butter_filtered(df['time'].values, low_passed_x, low_passed_y, low_passed_z)
	
	# Try to find each step and when people walking by finding the peaks
	real_peaks = get_peaks(low_passed_x)	# Find peaks
	plot_peak(df['time'].values, low_passed_x, real_peaks)

	v = get_velocity(real_peaks, low_passed_x, df['time'].values)
	start = df['time'].values[real_peaks[0]]
	end = df['time'].values[real_peaks[-1]]
	print('velocity is: %f\nDistance is: %f'%(v, v*(end-start)))

	# Get only the walking/running data
	df = df[df['time']>start]
	df = df[df['time']<end]

	# Fourier transform:
	# Get the frequence
	n = len(df['low_passed_x'].values)
	k = np.arange(int(n/2)+1)	#make sure the range of frequency match the range of Fourier transform result
	T = n/FS
	freq = k/T

	# Get the Fourier transform result for only real parts
	FF = np.fft.rfft(df['low_passed_x'].values)
	FF = abs(FF)
	plot_ff(df['time'].values, df['low_passed_x'].values, freq, FF)

	# find the frequency of steps
	freq_index = np.argmax(FF)
	print('The frequency of steps is: ', freq[freq_index])
	print('Steps from peak finding: %f\nSteps from Fourier transform: %f'%(real_peaks.size, freq[freq_index]*(end-start)))

if __name__=='__main__':
	infile = sys.argv[1]
	main(infile)