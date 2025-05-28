## 📊 Central Superstore Dashboard – Project Overview & Analysis

### 🎯 Objective

The goal of this project is to create an interactive web-based dashboard using *Streamlit* to analyze and visualize sales data from a fictional retail company, "Central Superstore." The dataset includes detailed information on orders, shipping, customers, and products, and enables stakeholders to draw actionable insights through rich visualizations.

---

### 📁 Dataset Description

The dataset consists of *2323 records* and *21 columns*, covering:

* *Order Metadata*: Order ID, Dates (Order/Ship), Shipping Mode.
* *Customer Info*: Customer ID, Name, Segment.
* *Location Info*: Country, City, State, Region, Postal Code.
* *Product Info*: Category, Sub-Category, Product ID, Product Name.
* *Transaction Data*: Sales, Quantity, Discount, Profit.

---

### 🧩 Key Functional Modules

#### 1. *Homepage / Main Viewer*

* Displays the entire dataset in paginated form.
* Allows users to navigate records 250 rows per page.
* A good entry point to inspect raw data.

#### 2. *Pie Chart Visualizations*

* Provides pie charts for categorical data distributions:

  * *Ship Mode*
  * *Segment*
  * *Top 10 Cities*
  * *State*
* Users can explore how orders are spread across different logistics modes and customer types.

#### 3. *Geography-Based Analysis*

* Users can filter data by *Category, **Segment, and **Ship Mode*.
* Visualizations include:

  * *Average Delivery Days* by City and State.
  * *Number of Orders* by City and State.
  * *Total Profit* by City and State.
* Supports data-driven decisions on logistics and regional strategy.

#### 4. *Customer Insights*

* Analyzes customer behavior based on:

  * *Total Orders* per Customer ID.
  * *Average Quantity* ordered per customer.
  * *Total Profit* per Customer.
* Also includes:

  * *Profit by Segment*
  * *Year-wise Customer Acquisition Trend*

#### 5. *Product Performance*

* Allows filtering by State to localize the analysis.
* Visuals cover:

  * *Average Delivery Days per Category*
  * *Total Profit by Category*
  * *Top Products by Profit*
  * *Yearly Profit Trend*
* Helps understand which products and categories drive the most value.

#### 6. *Placeholder Section*

* One page (presumably for future development) is not yet implemented and shows a placeholder.

---

### 🧠 Technologies Used

* *Streamlit*: For web-based UI.
* *Plotly Express*: For interactive and aesthetic charts.
* *Pandas*: For data manipulation.
* *Custom Functions & Widgets*: Modular code with helper methods for figure updates, color schemes, and UI components.

---

### ✅ Key Insights Supported

* Regional performance and delivery efficiency.
* Product category profitability.
* Customer ordering behavior.
* Shipping methods distribution.
* Annual trends in sales and profit.

---

## 🚀 Live Demo

Check out the live app here:  
👉 [Central Superstore Analysis App](https://centralsuperstoreanalysiswithapp-edcsv9vamdcchfiemzsqve.streamlit.app/)
