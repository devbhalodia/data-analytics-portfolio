# Superstore Sales & Customer Analytics – End‑to‑End Project


A full-stack analytics project on the **Superstore** dataset covering data cleaning, exploratory analysis, SQL KPI querying, forecasting with **Prophet**, **RFM customer segmentation**, interactive **Power BI** dashboards, and a final **insights report**.

This repository is organized to be fully reproducible and portfolio‑ready.

## Dataset
- Source: [Superstore dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- Shape: **9994 rows × 21 columns**
- Example columns: row_id, order_id, order_date, ship_date, ship_mode, customer_id, customer_name, segment, country, city...
- Detected date columns: order_date, ship_date

## Tech Stack
pandas, numpy, matplotlib, seaborn, prophet, mysql, powerbi

## Repository Structure
```
✓ 01_data_cleaning_and_eda.ipynb
✓ 02_sql_kpi_queries.ipynb
✓ 03_powerbi_dashboard.pbix
✓ 04_sales_forecasting_rfm_segmentation.ipynb
✓ 05_final_insights.pdf
✓ superstore.csv
✓ cleaned_superstore.csv
✓ Indian Startup.pbix
```

## Workflow
1. **Data Cleaning & EDA** (`01_data_cleaning_and_eda.ipynb`)  
   - Steps: Data cleaning step-by-step, EDA (Univariate, Bivariate, Multivariate), Drawing out key data insights and Business insights along with recommendations.
2. **SQL KPI Queries** (`02_sql_kpi_queries.ipynb`)  
   - KPIs computed via SQL included:  
     - **Total Sales by Region** – compare performance across regions  
     - **Top 5 Products by Profit** – identify most profitable products  
     - **Monthly Sales Trend (Year-wise)** – track seasonality and growth  
     - **Top 3 Customers by Sales** – highlight key customer accounts  
     - **Average Order Value (AOV)** – measure customer spending behavior  
     - **Customer Lifetime Value (CLTV)** – estimate long-term customer profitability  
     - **Profit Margin (%)** – monitor margins across sales  
     - **Sales by Category and Sub-Category** – analyze product hierarchy performance  
     - **Discount Impact on Profit** – evaluate effect of discounting on margins  
     - **Top 3 States by Sales in Each Region** – find best-performing geographies 
3. **Forecasting & RFM** (`04_sales_forecasting_rfm_segmentation.ipynb`)  
    - Conducted advanced analytics combining **time-series forecasting** and **customer segmentation**:  
     - **6-Month Sales Forecasting with Prophet** – captured seasonality (Q4 spikes, Q1 dips) and generated forward-looking trends to support inventory and promotion planning.  
     - **RFM Customer Segmentation** – scored customers on **Recency, Frequency, and Monetary value** to classify them into high-value, loyal, and at-risk cohorts; provided actionable retention and reactivation strategies.  
4. **Dashboarding** (`03_powerbi_dashboard.pbix`)  
   - Interactive visuals to explore most relevant business KPIs. 
5. **Final Insights Report** (`05_final_insights.pdf`)  
   - Business insights and recommendations synthesizing all steps.

## Reproducibility – How to Run

1. **Clone & setup**
   ```bash
   git clone <your-repo-url>.git
   cd <repo>
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt  # or install libs listed below
   ```

2. **Data cleaning & EDA**  
   Open and run `01_data_cleaning_and_eda.ipynb`. Adjust the CSV path if necessary.

3. **SQL KPIs**  
   Configure credentials in the notebook (or use a `.env`). Run `02_sql_kpi_queries.ipynb` to generate KPI tables.

4. **Forecasting & RFM**  
   Run `04_sales_forecasting_rfm_segmentation.ipynb` to produce time series forecasts (Prophet) and RFM segments.

5. **Dashboard**  
   Open `03_powerbi_dashboard.pbix` in Power BI Desktop. Refresh connections to point to your local CSV/SQL output tables.

6. **Insights**  
   Review `05_final_insights.pdf` for the executive summary of findings and recommendations.

## Key Results (Highlights)
- Clear **seasonality**: Q4 spikes in sales with Q1 dips; stable recovery in Q2–Q3.
- **Technology** category drives margin; **Furniture** suffered from deep discounting.
- **RFM** segmentation separated high-value vs reactivation-needed cohorts.
- **SQL KPIs** exposed regional underperformance and discount-profit tradeoffs.
- **Power BI** dashboard enables slicing by region, category, segment, and time.

## Business Insights (from `05_final_insights.pdf`)
- West region leads; South underperforms and needs pricing/discount fixes.  
- Average shipping time ≈ 3.5 days; scope to prioritize SLAs for top customers.  
- Discounts >30% often flip profit negative; curbing top loss-makers can recover profit.  
- Repeat customers ≈ 99% of revenue → focus on retention and loyalty.  
- Prophet 6‑month outlook shows repeated Q4 surges; plan inventory & promos accordingly.

## Minimal Requirements
Ensure these are installed:
- pandas, numpy
- matplotlib, plotly, seaborn
- prophet (or cmdstanpy backend)
- scikit-learn, scipy, statsmodels (if used)
- sqlalchemy + a MySQL driver (e.g., pymysql)
- jupyter

## Acknowledgments
- Superstore dataset (for educational/portfolio use)
- Prophet by Meta
- Power BI Desktop
