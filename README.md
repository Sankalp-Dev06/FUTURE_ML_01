# 📊 Sales Forecasting Dashboard Project

## 🎯 Project Overview

This project delivers a comprehensive **Sales Forecasting Dashboard** using advanced machine learning (Prophet) for forecasting and **Power BI** for interactive business intelligence. The workflow covers data cleaning, exploration, forecasting, and professional dashboarding.

---

## 🚀 Project Structure

```
sales_forecasting_dashboard/
├── Data/
│   ├── Raw/                    # Original Superstore dataset
│   ├── Processed/              # Cleaned and processed data for BI
│   └── Forecast/               # Model-generated forecasts (national & regional)
├── notebooks/                  # Jupyter notebooks for EDA, modeling, prep
│   ├── 01_exploration.ipynb
│   ├── 02_forecast.ipynb
│   └── 03_dashboard_data_preparation.ipynb
├── Sale Forecast Dashboard.pbix          # Power BI dashboard file (main deliverable)
├── requirements.txt            # Python dependencies for data/modeling
└── README.md                   # Project documentation (this file)
```

---

## 📈 Data & Modeling Pipeline

1. **Data Exploration** (`notebooks/01_exploration.ipynb`)
   - Cleans, explores, and visualizes the Superstore dataset.
2. **Forecasting** (`notebooks/02_forecast.ipynb`)
   - Trains Prophet models (national & regional), outputs forecast CSVs.
3. **Dashboard Data Prep** (`notebooks/03_dashboard_data_preparation.ipynb`)
   - Aggregates and formats data for Power BI.

**Processed data** is saved in `Data/Processed/` and `Data/Forecast/`.

---

## 📊 Power BI Dashboard: `Sale Forecast.pbix`

### **How to Use**
- Open `Sale Forecast.pbix` in Power BI Desktop (free from Microsoft).
- If prompted, update data source paths to your local CSVs in `Data/Processed/`.
- Click “Refresh” to load the latest data.

### **Dashboard Pages & Features**
1. **Overview**
   - Executive KPIs (latest forecast, average, regions)
   - National forecast trend (with confidence intervals)
   - Regional performance comparison
     <img width="1168" height="742" alt="Screenshot 2025-07-13 164710" src="https://github.com/user-attachments/assets/a6dc5cb7-7c32-4f83-a571-fdcbc6fe2ba5" />


2. **National Forecast**
   - Interactive time series with date slicer
   - Monthly/seasonal breakdowns
   - Key statistics (average, max, min, volatility)
     <img width="1162" height="732" alt="image" src="https://github.com/user-attachments/assets/2fb221bf-f375-48e3-9758-f925e3c750f0" />
     <img width="1169" height="732" alt="image" src="https://github.com/user-attachments/assets/84a0ef81-469c-4bb2-a650-3be62ae13cff" />


3. **Regional Analysis**
   - Multi-region comparison (line/bar charts)
   - Regional performance table and ranking
     <img width="1173" height="656" alt="image" src="https://github.com/user-attachments/assets/ae1a6a75-463a-44b1-9bbf-c6df397195d2" />


**All visuals are interactive:**  
- Use slicers to filter by date or region  
- Hover for tooltips  
- Drill down for details

---

## 🛠️ Technical Stack

- **Python**: Data cleaning, modeling (Prophet), CSV export
- **Power BI**: Data visualization, business intelligence
- **Jupyter Notebooks**: EDA, modeling, and data prep
- **Data**: Superstore sales (monthly, by region)

---

## 🚀 Quick Start

### **Python Data Pipeline**
```bash
pip install -r requirements.txt
# Run notebooks in order for data prep and forecasting
```

### **Power BI Dashboard**
1. Open `Sale Forecast.pbix` in Power BI Desktop
2. Update data source paths if needed
3. Click “Refresh” to load latest data
4. Explore the dashboard!

---

## 📈 Key Metrics & Insights

- **Forecast**: Prophet model predictions (with upper/lower bounds)
- **Growth Rate**: % change from historical to forecast
- **Volatility**: Standard deviation of sales
- **Regional Performance**: Compare and rank regions
- **Seasonality**: Monthly/seasonal sales patterns

---

## 🔍 Troubleshooting

- **Power BI Data Not Loading?**
  - Check that CSV paths in Power BI match your local folder structure
  - Click “Transform Data” > “Edit Source” to update paths

- **Python Errors?**
  - Ensure all packages in requirements.txt are installed
  - Run notebooks in order

---

## 👤 Author

**Developed by:**  
- Sankalp Tiwari  
- [LinkedIn](www.linkedin.com/in/sankalp-tiwari-350545203)  
- [GitHub](https://github.com/Sankalp-Dev06)


