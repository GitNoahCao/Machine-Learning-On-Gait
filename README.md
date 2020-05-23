# Machine-Learning-On-Gait

In this project, what we are trying to do is using the data of linear accelerometer sensor in our cell phone to calculate people’s walking speed, step frequency, and distance. We also used different machine learning models to identify the influence of gender, speed, and right foot or left foot on gait (a person's manner of walking).

To accomplish those goals, we collected data under different walking speed, like slow walking, fast walking and running. Also, we collect data from different heights of people, 160cm and 180cm. Then, we tried different filters to clean the data, numerical integration and Fourier transform to get walking speed and distance and different machine learning methods to analyze the data.

This project collected data by using 3d accelerometer sensor (Physics Toolbox Sensor Suite) in cell phone. 
For data cleaning and filtering part, LOESS Smoothing, Kalman Filtering and Butterworth filter were used to compare the result. 

For Machine Learning part, Gaussian Naive Bayes, KNeighborsClassifier, Support Vector Classifier, Regular Decision Tree, VotingClassifier were used for comparing conclusions.


#Group member
1.Noah Cao
2.John Zhang

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

***Data_Cleaning_and_Machine_Learning.ipynb*** can be viewed directly on Github. It also can be opened by Jupyter Notebook(Anaconda).  This file includes analysis of data cleaning and machine learning. All data filtering and machine learning results are in this file. To make the running time reasonable, the inputted sensor data size is 20 seconds (from 50s to 70s). User can choose larger data size by editing the code.

***walking.py*** is for getting the walking start and end time, walking speed, distance, frequency of steps and so on. 

***walking.py*** takes .csv file as input and outputs images into the images folder and on the terminal it will display the information of velocity, distance and frequency of steps. 

please use the command: ***python3 walking.py male_180_slow_walking.csv*** to run it and you can change the input .csv file to any other files.
