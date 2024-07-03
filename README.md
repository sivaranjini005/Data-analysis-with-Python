# **DATA ANALYSIS CHALLENGES**
## Contents:
      * Demographic Data Analyser
      * Medical Data Visualizer
      * Sea level Predictor
      * Page view Time series visualizer
## Description:
     This repository can help us get the data analysis challenges given by freecodecamp on different data sets using Python(Data Analysis and Data Visualization) and libraries like Numpy (Numerical computation), Pandas(Data Manipulation), Matplotlib and seaborn (Data Visualization). Below we will get the description of each analysis.
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
         * Cardio vascular disease positively correlated with age(0.2), cholesterol(0.2) and weight(0.2) and negatively correlated with height(-0.1)
         overall heat map highlights that weight, age, cholesterol and glucose levels are some of the significant factors associated with cardio-vascular disease.
### 3.Sea Level Predictor:
          Here we will analyze a dataset of the global average sea level change since 1880. We will use the data to predict the sea level change through year 2050.
          File source:epa_sea_level.csv
          ![Sea level plot](https:raw//githubusercontent.com/sivaranjini005/Data-analysis-with-Python/blob/master/sea%20level%20predictor/sea_level_plot.png)
          * The plot indicates a consistent rise in sea levels over time.
          * The slope of the red line (1880-2050) suggests a gradual increase in sea level over the entire period.
          * The slope of the green line (2000-2050) is steeper, indicating that the rate of sea level rise has increased in recent years.
          If the recent trend continues, the sea level rise by 2050 could be significantly higher than if the historical trend were to continue unchanged.
### 4. Page View Time Series Visualiser:
          Here we will visualize time series data using a line chart, bar chart, and box plots. We will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.
          * Initially cleaned the data set by filtering out the top 2.5% and bottom 2.5% of pageviews 
          * From the line chart we find that there is a clear upward trend in the number of daily page views over the given period, indicating that the forum's popularity has grown significantly.There appear to be recurring patterns in the data, indicating possible seasonal variations in forum activity. For example, there are noticeable peaks around certain times each year.
          * From the bar chart we get the monthly average views, making us understand that last quarters in all years have more average views than other quarters. So there is a seasonality based views on this page forum.
          * From the box plot we observe that there is a significant growth in the page views over the years and we find that highest peak and lowest views as outliers, from this both year wise and month wise box plots we can say that there is a seasonality in page views.

### Mean, Median, Standard Deviation Using Numpy
```
import numpy as np

def calculate(list_):
    if len(list_) != 9:
        raise ValueError('List must contain nine numbers')
    array_ = np.array(list_).reshape(3,3)

    mean_ax0 = np.mean(array_, axis = 0)
    mean_ax1 = np.mean(array_, axis = 1)
    mean_all = np.mean(array_)

    var_a0 = np.var(array_, axis = 0)
    var_a1 = np.var(array_, axis = 1)
    var_al = np.var(array_)

    var_ax0 = np.around(var_a0, decimals= 3)
    var_ax1 = np.around(var_a1, decimals= 3)
    var_all = np.around(var_al, decimals= 3)


    std_a0 = np.std(array_, axis = 0)
    std_a1 = np.std(array_, axis = 1)
    std_al = np.std(array_)

    std_ax0 = np.around(std_a0, decimals= 3)
    std_ax1 = np.around(std_a1,decimals= 3)
    std_all = np.around(std_al, decimals= 3)

    max_ax0 = np.max(array_, axis = 0)
    max_ax1 = np.max(array_, axis = 1)
    max_all = np.max(array_)

    min_ax0 = np.min(array_, axis = 0)
    min_ax1 = np.min(array_, axis = 1)
    min_all = np.min(array_)

    sum_ax0 = np.sum(array_, axis = 0)
    sum_ax1 = np.sum(array_, axis = 1)
    sum_all = np.sum(array_)

    return {'mean': [mean_ax0.tolist(), mean_ax1.tolist(), float(mean_all)],
            'variance': [var_ax0.tolist(), var_ax1.tolist(), float(var_all)],
            'standard_deviation': [std_ax0.tolist(), std_ax1.tolist(), float(std_all)],
            'max': [max_ax0.tolist(), max_ax1.tolist(), float(max_all)],
            'min': [min_ax0.tolist(), min_ax1.tolist(), float(min_all)],
            'sum': [sum_ax0.tolist(), sum_ax1.tolist(), float(sum_all)]}
```

    The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
           
           
      
        
        
     
