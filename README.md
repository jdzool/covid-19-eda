# covid-19-eda
Exploratory data analysis around the covid-19 pandemic 

## Setup: Data Sources

Data is source from the [Public Health England: arcgis microsite](https://www.arcgis.com/apps/opsdashboard/index.html#/f94c3c90da5b4e9f9a0b19484dd4bb14). This site is being updated daily with UK wide confirmed cases and confirmed cases at a 

The some of the source data driving the microsite is available (here)[https://www.arcgis.com/home/item.html?id=e5fd11150d274bebaaf8fe2a7a2bda11]

## Setup: File Structure 

If you want to run this code on your machine. You will need to download the data and place it in a folder (/data). The file structure for your repo should look something like below. I am not pushing data to github. 

├── data  
   └── DailyConfirmedCases.xlsx  
├── logistic_fit_to_plot.py  
├── papers  
   └── TUe\ -\ Technical_Report_Prediction_Corona_Virus.pdf  
├── plots  
   └── 2020-03-21_corona_virus_fit.png  


## Initial outputs 

<center>
<img src="https://github.com/jdzool/covid-19-eda/blob/master/plots/2020-03-21_corona_virus_fit.png" height="400">
</center>


## Further questions  

* How to calculate R_0?  
* When can an accurate prediction of the peak date be made? 
* Is it possible to observe a change in the behaviour of the infection rate with social distancing / removal of leisure activities (pubs, restaurants, gyms, cinemas etc..) from 19th March 2020? This would be apparent in a changing infection rate. 

## Assumptions
* Sampling statistics / testing levels are consistent over time
* Region infection rate / human behaviour is the same at the local level as the national level (we do not have a time series for each region)