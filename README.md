
# Swiggy Restaurant Performance Analysis – Power BI Project

## Project Overview
This project analyzes 50 Swiggy-listed restaurants in Bangalore using **Power BI** and **Python** for data-driven insights. It focuses on restaurant performance, customer satisfaction, delivery efficiency, pricing, and discount strategies.

By integrating **interactive dashboards** and a **regression-based Python script**, this analysis helps restaurant owners, analysts, and decision-makers optimize operations in the competitive food delivery market.

---

## Project Structure

```
Swiggy-Restaurant-Analysis-PowerBI/
│
├── Dashboard/
│   ├── Swiggy_Analysis.pbix
│   ├── Dashboard_Screenshot.png
│   └── Regression_ScatterPlot_Python.png
│
├── Data/
│   └── BA_projectData_updated.xlsx
│
├── Code/
│   └── linear_regression_discount_vs_order.py
│
└── README.md
```



## Objectives

- Clean and structure Swiggy restaurant data using Excel and Power BI.
- Create DAX measures to evaluate performance KPIs like sales, delivery time, and ratings.
- Visualize insights using charts (bar, line, pie, area, scatter, donut).
- Use **Python for linear regression** to analyze how discounts affect average order value.
- Identify top-performing restaurants and areas for improvement.
- Support strategic decision-making with actionable insights.

---

## Dataset

**File:** `BA_projectData_updated.xlsx`  
Manually extracted from the Swiggy app and Google, this dataset includes:

- 📍 Restaurant name, location, cuisine type
- ⭐ Customer ratings, best-rated dishes
- 💰 Starting price, total orders, delivery charges
- 🎁 Discounts, refund requests, dine-in availability

---

## Tools & Technologies

| Tool             | Purpose                                      |
|------------------|----------------------------------------------|
| **Power BI**     | Data visualization, DAX calculations         |
| **Python**       | Linear regression using sklearn & matplotlib |
| **Excel**        | Initial data preparation and cleanup         |

---

## Dashboard Highlights

KPIs (Cards)
₹86M+ in total sales
1320 refund requests
Biryani as the best-rated dish
Marathahalli – top ordering location (43.47%)

Visuals
Line Chart: Discount (%) by restaurant
Bar Chart: Delivery time vs charges
Donut Chart: Average order value
Pie Chart: Orders by location
Table View: Restaurant details
Scatter Plot: Discount vs Avg Order Value (with regression line

---

## Python Integration: Linear Regression

A regression analysis was performed to study the relationship between discounts and average order value using Python.

This regression line helps understand whether offering more discount leads to higher or lower order value.

---

## 📐 DAX Measures Used

```plaintext
Total Revenue         = SUMX(Sheet1, Sheet1[items] * Sheet1[Starting price])
Average Rating        = AVERAGE(Sheet1[rating])
Average Discount      = AVERAGEX(Sheet1, SUBSTITUTE(Sheet1[discount], "%", ""))
Total Items Sold      = SUM(Sheet1[items])
Standard Deviation    = STDEV.S(column)/SQRT(COUNT(column))
Sample Error          = Value - AVERAGE(column)
Sample Variance       = VAR.S(column)





