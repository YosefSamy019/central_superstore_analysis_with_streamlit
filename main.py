import math

import pandas as pd
import streamlit as st

from functions.functions import load_dataset, global_init

def main():
    df = None
    global_init()


    st.title('Central Superstore')
    st.write("""
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
    """)
    st.write('\n')

    st.divider()

    st.header('Dataset Viewer')

    with st.spinner("Loading dataset"):
        df = load_dataset()
        st.session_state['df'] = df

    PAGE_MAX = 150
    no_pages = math.ceil(len(df) / PAGE_MAX)

    cols = st.columns([0.35, 0.65])
    cols[1].markdown(f'{no_pages} pages, each page has {PAGE_MAX} records')
    selected_page_no = cols[0].number_input(f'Enter page number:', step=1, min_value=1, max_value=no_pages)
    selected_page_no_minus_one = selected_page_no - 1
    st.dataframe(df.iloc[PAGE_MAX * selected_page_no_minus_one:PAGE_MAX * selected_page_no, :])


if __name__ == "__main__":
    main()
