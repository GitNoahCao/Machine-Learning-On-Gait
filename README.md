# Sensors, Noise, and Walking
This project is for using accelerometer sensor in phone to find when people walking, walking speed and distance. Also, different machine learning models were used to identify the influence of gender, speed, and right foot or left foot on gait.

#Group member
1.Noah Cao
2.Haishuo Zhang

## Required languages and Libraries:
- jupyter notebook
- python3
- sys
- numpy
- pandas
- scipy
- matplotlib
- Seaborn
- Sklearn


## How to run:
There are two programming files for this project.

***Data_Cleaning_and_Machine_Learning.ipynb*** can be viewed directly on Gitlab. It also can be opened by Jupyter Notebook(Anaconda).  This file includes analysis of data cleaning and machine learning. All data filtering and machine learning results are in this file. To make the running time reasonable, the inputted sensor data size is 20 seconds (from 50s to 70s). User can choose larger data size by editing the code.

***walking.py*** is for getting the walking start and end time, walking speed, distance, frequency of steps and so on. 

***walking.py*** takes .csv file as input and outputs images into the images folder and on the terminal it will display the information of velocity, distance and frequency of steps. 

please use the command: ***python3 walking.py male_180_slow_walking.csv*** to run it and you can change the input .csv file to any other files.