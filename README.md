# 📈 FUTURE_ML_01 – AI-Powered Sales Forecasting Dashboard

This project is part of my internship assignment where I built a predictive analytics dashboard to forecast retail sales using historical data and machine learning.

## 📂 Project Structure

```
├── Data/
│   ├── Processed/
│   │   ├── monthly_sales_by_region.csv    # Processed monthly sales data by region
│   │   └── monthly_sales_national.csv      # Processed national monthly sales data
│   └── Raw/
│       └── Superstore.csv                  # Raw superstore sales data
├── notebooks/
│   └── 01_exploration.ipynb               # Data exploration and preprocessing notebook
└── requirements.txt                       # Project dependencies
```

## Overview

This project analyzes superstore sales data to create forecasting models for both national and regional sales trends. The analysis includes data cleaning, exploratory data analysis (EDA), and preparation of data for time series forecasting.

### Features

- Data preprocessing and cleaning
- Outlier detection and handling
- Time series analysis
- Regional sales breakdown
- Preparation of Prophet-ready datasets

## 🛠️ Tech Stack

- Python (Pandas, Prophet, Matplotlib, Seaborn)
- Power BI
- Git & GitHub


## 📊 Data Processing Steps

1. Data loading and initial exploration
2. DateTime conversion for Order and Ship dates
3. Basic time range analysis
4. Daily sales analysis with outlier detection
5. Monthly sales trend analysis
6. Regional sales breakdown
7. Export of processed data for forecasting

## Getting Started

### Prerequisites

- Python 3.12
- Required packages listed in `requirements.txt`

### Installation

1. Clone the repository
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebooks in the `notebooks/` directory

## Data Files

- **Raw Data**: Superstore.csv - Contains the original sales data
- **Processed Data**: 
  - monthly_sales_national.csv - National level sales data prepared for forecasting
  - monthly_sales_by_region.csv - Region-wise sales data prepared for forecasting

## Future Enhancements

- Implementation of Prophet forecasting models
- Interactive dashboard development
- Additional feature engineering
- Model performance evaluation
- Automated retraining pipeline

## 🙋‍♂️ Author

- **Name**: Sankalp Tiwari
- **Internship Program**: AI-Powered Forecasting Dashboard
- **GitHub**: Sankalp-Dev06 (https://github.com/Sankalp-Dev06)

