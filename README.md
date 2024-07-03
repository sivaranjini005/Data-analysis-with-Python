# **DATA ANALYSIS CHALLENGES**
## Contents:
      * Demographic Data Analyser
      * Medical Data Visualizer
      * Sea level Predictor
      * Page view Time series visualizer
## Description:
     This repository can help us get the data analysis challenges on different data sets using Python(Data Analysis and Data Visualization) and libraries like Numpy (Numerical computation), Pandas(Data Manipulation), Matplotlib and seaborn (Data Visualization). Below we will get the description of each analysis.
 ### 1.Demographic Data Analyser:
      Here we have the demographic dataset that was extracted from 1994 census database. In this we have analysed the data set using Pandas and what we understand is as follows
           1. People's population by race includes whites (27816), Black(3124), Asian-Pac-Islander (1039), Amer-Indian-Eskimo(311) and others comes under counts of 271
           2. Average age of men during that time was around 39 only
           3. People's earning more than 50k are higher for people with higher education (46.54%) than people without higher education(17.37%)
           4. we can understand the minimum work hours per week is 1 hour
           5. 22% of wealthy people who earns more than 50k are in United States
           6. Professional specialities are prevelant occupation in India during that time
           
### 2.Medical Data Visualizer:
     The rows in the medical examination dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices. Below are what I have done using this data set
     * Added a new column 'overweight' to determine whether the person is 'Obese' or 'not' by calculating the BMI and normalised the dataset by setting 0 to normal range (True values) and 1 to above normal range for 'cholesterol' and 'gluc' column
     *From the bar chart what we get to know is 
         * Being physically active is associated with lower chances of cardio vascular disease.
         * Higher cholesterol and glucose level are more common among individuals with cardio vascular disease.
         * Overweight individuals are more prone to cardio vascular disease
         * Smoking and Alcohol does not provide any significant difference in this given data set.
     * From the Heat map visualization, we understand that
         * There is a strong positive correlation between weight and overweight(0.7)
         * There is a moderate positive correlation between height and weight(0.5)
         * There is a positive correlation between cholesterol and glucose level (0.4)
         * Cardio vascular disease positively correlatd with age(0.2), cholesteroal(0.2) and weight(0.2) and negatively correlated with height(-0.1)
         overall heat map highlights that weight, age, cholesterol and glucose levels are some of the significant factors associated with cardio-vascular disease.
      
           
           
      
        
        
     
