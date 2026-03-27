# 🏷️ Nike Sales Data Analysis

## 📊 Project Overview

This project focuses on **data cleaning, preprocessing, and exploratory data analysis (EDA)** on a Nike sales dataset.

The goal is to transform raw, inconsistent data into a clean and structured format, then extract insights through **visualization techniques**.

---

## ⚙️ Data Preprocessing Pipeline

The preprocessing phase ensures data quality and consistency through several steps:

### 🔹 Data Cleaning

* Removal of duplicate records based on `Order_ID`
* Conversion of `Order_Date` to datetime format
* Handling missing values using:

  * Median (numerical columns)
  * Mode (categorical columns)
  * Default values (e.g., 0 or "Unknown")

### 🔹 Data Correction

* Fixing negative values in `Units_Sold`
* Limiting `Discount_Applied` to a maximum of 100%
* Replacing invalid `MRP` values

### 🔹 Data Standardization

* Cleaning and normalizing `Region` values (e.g., fixing typos like *delhii → delhi*)

### 🔹 Feature Engineering

* One-hot encoding:

  * `Sales_Channel`
  * `Gender_Category`
* Creation of new feature:

  * `Profit_Margin`

### 🔹 Data Normalization

* Min-Max scaling applied to:

  * `Units_Sold`
  * `MRP`
  * `Revenue`
  * `Profit`

---

## 📈 Data Visualization

The project includes several visualizations to explore relationships and distributions:

### 🔥 Correlation Heatmap

* Displays relationships between numerical variables
* Helps identify strong correlations

### 📊 Revenue Distribution

* Histogram with KDE curve
* Shows how revenue values are distributed

### 📦 Revenue by Product Line

* Bar plot of total revenue per product category
* Highlights best-performing product lines

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib

---

## 📁 Project Structure

```
nike-sales-data-analysis/
│
├── data/
├── scripts/
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── validation.py
│   ├── exploration.py
│   ├── visualization.py
│   └── export_data.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 How to Run the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Run the project
python main.py
```

---

## 🎯 Key Outcomes

* Clean and consistent dataset ready for analysis
* Automated preprocessing pipeline
* Insightful visualizations for business understanding

---

## 💡 Future Improvements

* Add machine learning models (sales prediction)
* Build an interactive dashboard (Streamlit / Power BI)
* Deploy as a data analytics web app

---

## 👨‍💻 Author

Yassine Amri
