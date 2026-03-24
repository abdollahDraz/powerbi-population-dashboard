# 📊 Population Analysis Dashboard (Power BI)

## 🚀 Project Overview

This project is a **complete data analysis pipeline** that transforms raw population data into a professional and interactive Power BI dashboard.

The project covers:

* Data collection (Web Scraping)
* Data cleaning
* Data modeling (DAX)
* Data visualization (Dashboard)

---

## 🌐 Data Source

* Source: Wikipedia
* Dataset: List of countries and dependencies by population
* Method: Web Scraping using Python

---

## 🧩 Data Collection (Python)

The dataset was collected using a Python script located in:

```
scripts/scraping.py
```

### 🔧 Tools Used:

* requests
* BeautifulSoup
* pandas

### ⚙️ Process:

* Send HTTP request
* Parse HTML content
* Extract table data
* Clean and store as CSV

---

## 🧹 Data Processing (Power BI - Power Query)

* Cleaned raw data
* Converted data types
* Fixed percentage format
* Handled missing values

---

## 🧠 Data Modeling (DAX)

### Key Measures:

* Total Population
* Average Population
* Max Population
* Min Population
* Population Percentage Contribution
* Ranking by Population

---

## 📊 Dashboard Pages

---

### 🟦 Overview Page

![Overview](assets/Screenshot%202026-03-24%20144840.png)

#### 🔹 Features:

* KPI Cards (Total, Avg, Max, Min)
* Top 10 Countries by Population
* Population Distribution (Donut Chart)
* Interactive Date Filter

---

### 🟧 Analysis Page

![Analysis](assets/Screenshot%202026-03-24%20144854.png)

#### 🔹 Features:

* Population Trend Over Time 📈
* Top vs Least Populated Countries
* Comparative Analysis
* Dynamic Filtering

---

## 📂 Project Structure

```
powerbi-population-dashboard/
│
├── assets/        # Dashboard screenshots
├── data/          # Dataset (CSV)
├── docs/          # Documentation
├── report/        # Power BI file (.pbix)
├── scripts/       # Web scraping script
├── README.md
```

---

## 🛠️ Tools & Technologies

* Power BI
* Python
* Pandas
* BeautifulSoup
* DAX

---

## 💡 Key Insights

* India and China are the most populated countries
* Population distribution is highly concentrated
* Clear trends over time using interactive filtering

---

## ▶️ How to Run

### 1️⃣ Install requirements:

```
pip install -r scripts/requirements.txt
```

### 2️⃣ Run scraping script:

```
python scripts/scraping.py
```

### 3️⃣ Open Power BI file:

```
report/Web_Scrapping_Population_Countaries.pbix
```

---

## 👨‍💻 Project Owner

**Abdollah Mohammed Draz**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
