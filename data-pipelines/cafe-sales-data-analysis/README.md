# ☕ Cafe Sales Data Analysis

## 📊 Project Overview

This project focuses on **cleaning, preprocessing, and analyzing cafe sales data** to extract meaningful business insights.

It transforms raw, inconsistent transactional data into a structured dataset and visualizes key patterns in customer spending and product performance.

---

## ⚙️ Data Cleaning

The cleaning process ensures data consistency and correctness:

* Replacement of invalid values (`ERROR`, `UNKNOWN`, empty) with `NaN`
* Conversion of numerical columns:

  * `Quantity`
  * `Price Per Unit`
  * `Total Spent`
* Handling missing values:

  * Median imputation for numerical features
  * Default category `"Unknown"` for categorical data
* Recalculation of `Total Spent` using:

  ```
  Total Spent = Quantity × Price Per Unit
  ```
* Date parsing with proper format handling

---

## 🔄 Data Preprocessing

The preprocessing pipeline enhances the dataset for analysis:

### 🔹 Feature Engineering

* Extraction of:

  * `Month`
  * `DayOfWeek`

### 🔹 Encoding

* One-hot encoding applied to:

  * `Payment Method`
  * `Location`

### 🔹 Normalization

* Standardization of `Total Spent` using **StandardScaler**

---

## 📈 Data Visualization

The project includes visual insights into sales performance:

### 📦 Sales by Product

* Bar chart showing total revenue per item

### 📊 Spending Distribution

* Histogram illustrating customer spending behavior

📁 Outputs saved in:

```
outputs/figures/
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 📁 Project Structure

```
cafe-sales-data-analysis/
│
├── data/
├── scripts/
│   ├── cleaning.py
│   ├── preprocessing.py
│   └── visualization.py
│
├── outputs/
│   └── figures/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python scripts/cleaning.py
python scripts/preprocessing.py
python scripts/visualization.py
```

---

## 🎯 Key Outcomes

* Clean and structured dataset
* Feature-engineered data ready for analysis
* Visual insights into product performance and spending patterns

---

## 💡 Future Improvements

* Add sales prediction model
* Build dashboard (Streamlit)
* Perform customer segmentation

---

## 👨‍💻 Author

Yassine Amri
