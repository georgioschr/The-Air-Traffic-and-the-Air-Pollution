# Air-Traffic and Air-Pollution Relation and Correlation

Has been stated that the unforeseen outbreak due to COVID-19 in the 21st century, and the forced confinement of millions of inhabitants over the world, mainly during the first part of 2020, has shown a reduction in the temperature in the bigger capitals worldwide.

> _"Human activity is the cause of the climate problem."_
> António Guterres, COP27, Egypt, Nov. 2022

## Objectives:
In this project, we investigate how air traffic contributes to the increase in air pollution and how this may also affect global warming. We will try to utilize open historical data from Cyprus air-quality measures and air traffic for analysis and correlation between airline traffic and air pollutants per area and period and identify how the increase in emissions degrades air quality. 

We have selected to work with Cyprus data, as Cyprus island has high seasonal traffic of tourists in mainly the summer period and we as assume that this variation will reflect as well in the air quality measurements. The following figure show this seasonal variance.
![image](https://user-images.githubusercontent.com/92388643/213927561-34e44929-effa-41ce-aa90-7ee5853e9358.png)

_Source:_ [ceicdata](https://www.ceicdata.com/en/indicator/cyprus/visitor-arrivals)

Furthermore, the pandemic period COVID-19 was significantly impacted air traffic,  mainly during the second quarter of 2020 due to the hard measures that Cyprus took in order to minimize the spread of the disease. This fro has shown this drop (see the following figure from Euro Control data) and 

The following graph from Euro Control data shows this substantial reduction during the second quarter of 2020. This fluctuation is very useful for our analysis as we expect to see a similar decrease in air pollutants in the areas or cities of Cyprus airports.

![image](https://user-images.githubusercontent.com/92388643/213886184-7c684756-522a-48d7-8186-714995bf7b2b.png)
_Source:_ [Euro Control](https://www.eurocontrol.int/Economics/2020-DailyTrafficVariation-States.html)

## Data Sources:
- [Cyprus Air Quality Hourly Historical Data](https://www.data.gov.cy/node/3849?language=en)
- [Cyprus Air Quality Current Data](https://www.data.gov.cy/node/1451?language=en)
- [Cyprus (Larnaca) Air Traffic Daily Historical Data](https://www.data.gov.cy/node/2451?language=en)
- [Cyprus (Pafos) Air Traffic Daily Historical Data](https://www.data.gov.cy/node/2462?language=en)

## Data Processing
The process have been 
- [Air_Quality_Data Transformation](/notebook/air_quality_data_csv.ipynb)
- [Air Traffic Data Transformation](/notebook/air_traffic_data_transformation.ipynb)

## Analysis
- [Data Analysis](/notebook/data_analysis.ipynb)

## Results

In order to quantify the relationship between two traffic and pollutants variables is to use the Pearson correlation coefficient, which measures the linear association between two variables.
It always takes on a value between -1 and 1 where:
- -1 indicates a perfectly negative linear correlation
- 0 indicates no linear correlation
- 1 indicates a perfectly positive linear correlation
To determine if a correlation coefficient is statistically significant, we calculate the corresponding t-score and p-value.

![image](https://user-images.githubusercontent.com/92388643/213930826-cdb37a56-b8e1-4840-92ba-49e5f44e6370.png)
This shows that there is a collaboration between some popular and the air traffic between 0,3 and 0,5, but the p-value is close to 0 which indicates a weak correlation.

#### Correlation matrix
![image](https://user-images.githubusercontent.com/92388643/213930091-ec89d269-1cbc-4c81-98ad-926aa971d650.png)

![image](https://user-images.githubusercontent.com/92388643/213828120-02a1eac5-c608-429c-96f6-2a77532f84d3.png)

## References: 
1. [What is NOx](https://www.noxfondet.no/en/articles/what-is-nox/)
2. [Cyprus Air Quality](https://www.airquality.dli.mlsi.gov.cy/)

## Data Virtualization
[Dashboard](https://datastudio.google.com/s/rtKC0BK1SYg)

