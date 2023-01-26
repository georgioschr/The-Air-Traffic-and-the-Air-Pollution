# Air-Traffic and Air-Pollution Relation and Correlation

Has been stated that the unforeseen outbreak due to COVID-19 in the 21st century, and the forced confinement of millions of inhabitants over the world, mainly during the first part of 2020, has shown a reduction in the temperature in the bigger capitals worldwide.

> _"Human activity is the cause of the climate problem."_
> António Guterres, COP27, Egypt, Nov. 2022

## Objectives:
In this project, we investigate how air traffic contributes to the increase in air pollution and how this may also affect global warming. We utilize open historical data from Cyprus air-quality measures and air traffic for analysis and correlation between airline traffic and air pollutants per area and period and identify how the increase in emissions degrades air quality. 

We have selected to work with Cyprus data, as Cyprus island has high seasonal traffic of tourists in mainly the summer period and we as assume that this variation will reflect as well in the air quality measurements. The following figure show this seasonal variance.

<img src="https://user-images.githubusercontent.com/92388643/213927561-34e44929-effa-41ce-aa90-7ee5853e9358.png" alt="alt text" width="700" height="300">

_Source:_ [ceicdata](https://www.ceicdata.com/en/indicator/cyprus/visitor-arrivals)

Furthermore, the pandemic period COVID-19 was significantly impacted air traffic,  mainly during the second quarter of 2020 due to the hard measures that Cyprus took in order to minimize the spread of the disease. The following graph from Euro Control page shows this substantial reduction during the second quarter of 2020. This fluctuation is very useful for our analysis as we expect to see a similar decrease in air pollutants close to the Cyprus airports.

![image](https://user-images.githubusercontent.com/92388643/213935990-d1f58811-f495-4590-92f1-9aa5160b18a9.png)
_Source:_ [Euro Control](https://www.eurocontrol.int/Economics/2020-DailyTrafficVariation-States.html)

## Data Sources:
- [Cyprus Air Quality Hourly Historical Data](https://www.data.gov.cy/node/3849?language=en)
- [Cyprus Air Quality Current Data](https://www.data.gov.cy/node/1451?language=en)
- [Cyprus (Larnaca) Air Traffic Daily Historical Data](https://www.data.gov.cy/node/2451?language=en)
- [Cyprus (Pafos) Air Traffic Daily Historical Data](https://www.data.gov.cy/node/2462?language=en)

## Data Processing
The data preprocessing requires to use use a Distributed data system. We have selected to use Hadoop Spark and [Google Cloud DataProc](https://cloud.google.com/dataproc/docs/concepts/overview) in order to process the historical data of Air Quality that we have downloaded from the Cyprus data portal  and aggregate them at a daily granularity, for easy data manipulation and analysis.
- [DataProc Setup and Job Scheduling](/cloud-dataproc)
- [Air_Quality_Data Transformation](/notebook/air_quality_data_csv.ipynb)

Air Traffic provided by the Cyprus portal is in a variety of formats, as they use excel and CSV files with different schemas every some years.
- [Air Traffic Data Transformation](/notebook/air_traffic_data_transformation.ipynb)

## Analysis
This notebook shows step by step the analysis that we have performed
- [Data Analysis](/notebook/data_analysis.ipynb)

## Results

In order to quantify the relationship between two traffic and pollutants variables is to use the Pearson correlation coefficient, which measures the linear association between two variables.
It always takes on a value between -1 and 1 where:
- -1 indicates a perfectly negative linear correlation
- 0 indicates no linear correlation
- 1 indicates a perfectly positive linear correlation

To determine if a correlation coefficient is statistically significant, we calculate the corresponding t-score and p-value.

![image](https://user-images.githubusercontent.com/92388643/213933010-9275d1ec-293b-4b78-8b3f-d3c172050407.png)

This shows that there is a correlation between some pollutants and air traffic which is around 30%-49% for NOx, NOx, C6H6, and CO and this and their collection is a moderate positive. Also, the p-value is less than 0.01, so the correlation is statistically significant and can be used.

#### Correlation matrix
![image](https://user-images.githubusercontent.com/92388643/213930091-ec89d269-1cbc-4c81-98ad-926aa971d650.png)

However, as we deal with time series data, we need to investigate also for the seasonality effect in all variables not only in air traffic, and check whether is possible to their relation/correlation by removing the possible seasonality.

From the following graphs, we can easily view the relationship and how the pollutant of NO and NOx values are drops parallel with air traffic during the 1st and 2nd quarter of 2020
![image](https://user-images.githubusercontent.com/92388643/213934403-06c0a4eb-7306-4c72-aef8-19fe542b3e2f.png)
![image](https://user-images.githubusercontent.com/92388643/213934383-73f4d597-dab0-417f-bc03-4a15a18de9bb.png)

## References: 
1. [What is NOx](https://www.noxfondet.no/en/articles/what-is-nox/)
2. [Cyprus Air Quality](https://www.airquality.dli.mlsi.gov.cy/)

## Data Virtualization
[Dashboard](https://datastudio.google.com/s/rtKC0BK1SYg)

