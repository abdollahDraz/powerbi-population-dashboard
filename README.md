# 📊 Population Analysis Dashboard (Power BI)

## 🚀 Project Overview

This project presents a **professional end-to-end data analysis solution** using Power BI.

It starts from **data collection (Web Scraping)** from Wikipedia and ends with a fully interactive dashboard that provides insights into global population distribution and trends.

---

## 🧩 Project Workflow

### 1️⃣ Data Collection (Web Scraping)

* Source: Wikipedia
* Tool: Python (BeautifulSoup + Requests)
* Script: `scripts/scraping.py`

👉 The script extracts:

* Country
* Population
* Percentage
* Date

---

### 2️⃣ Data Processing

* Cleaned using Power Query
* Converted Percentage to proper format
* Created calculated columns & measures

---

### 3️⃣ Data Modeling (DAX)

Key measures used:

* Total Population
* Average Population
* Max / Min Population
* Population % Contribution
* Ranking (Top Countries)

---

### 4️⃣ Data Visualization

Built using Power BI with:

* KPI Cards
* Bar Charts
* Pie / Donut Charts
* Line Charts
* Slicers (Date Filters)

---

## 📈 Dashboard Pages

---

### 🟦 Overview Page

![Overview](assets/Screenshot%202026-03-24%20144840.png)

#### 🔹 Features:

* Total Population KPI
* Average Population
* Max / Min Population
* Top 10 Countries by Population
* Population Distribution (Donut Chart)
* Date Filter

---

### 🟧 Analysis Page

![Analysis](assets/Screenshot%202026-03-24%20144854.png)

#### 🔹 Features:

* Population Trend Over Time 📈
* Top vs Least Countries Comparison
* Advanced Filtering by Date
* Detailed Country Analysis

---

## 🛠️ Tools & Technologies

* **Power BI** → Dashboard & Visualization
* **Python** → Web Scraping
* **Pandas** → Data Handling
* **BeautifulSoup** → HTML Parsing
* **DAX** → Data Modeling

---

## 📂 Project Structure

```
powerbi-population-dashboard/
│
├── data/        # Dataset (CSV)
├── report/      # Power BI file (.pbix)
├── assets/      # Dashboard screenshots
├── scripts/     # Web scraping script
├── README.md
```

---

## 💡 Key Insights

* Identify the most populated countries globally
* Understand population distribution (%)
* Analyze trends over time
* Compare top vs least populated countries

---

## ▶️ How to Run

### 1️⃣ Install dependencies:

```
pip install -r scripts/requirements.txt
```

### 2️⃣ Run scraping script:

```
python scripts/scraping.py
```

### 3️⃣ Open Power BI file:

```
report/population_dashboard.pbix
```

---

## 👨‍💻 Author

** Abdollah Mohammed Deraz ""

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
