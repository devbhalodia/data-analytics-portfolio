# Superstore Sales & Customer Analytics – End‑to‑End Project


A full-stack analytics project on the **Superstore** dataset covering data cleaning, exploratory analysis, SQL KPI querying, forecasting with **Prophet**, **RFM customer segmentation**, interactive **Power BI** dashboards, and a final **insights report**.

This repository is organized to be fully reproducible and portfolio‑ready.

## Dataset
- Source: Superstore dataset (local copy: `cleaned_superstore.csv`)
- Shape: **9994 rows × 21 columns**
- Example columns: row_id, order_id, order_date, ship_date, ship_mode, customer_id, customer_name, segment, country, city...
- Detected date columns: order_date, ship_date

## Tech Stack
pandas, numpy, matplotlib, seaborn, prophet, mysql

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
   - Steps (headings detected): Data cleaning, EDA, Univariate analysis (numerical columns), Conclusions:-, Univariate analysis (Categorical columns), Conclusions:-, Bivariate analysis (numeric - numeric), Conclusions:-, Bivariate analysis (numeric - categorical), Conclusions:-...
2. **SQL KPI Queries** (`02_sql_kpi_queries.ipynb`)  
   - KPIs computed via SQL (examples below). Headings detected: Total sales by region, Top 5 products by Profit, Monthly sales trend (year-wise), Top 3 customers by sales, Average order value (AOV), Customer lifetime value (cltv), Profit margin (%), Sales by Category and Sub-Category, Discount Impact on Profit, Top 3 States by Sales in Each Region...
3. **Forecasting & RFM** (`04_sales_forecasting_rfm_segmentation.ipynb`)  
   - Prophet-based time series forecasting and customer RFM scoring. Headings detected: 6 month Sales forecasting using Prophet model, RFM Customer Segmentation
4. **Dashboarding** (`03_powerbi_dashboard.pbix`)  
   - Interactive visuals to explore sales, profit, customers, and regional trends.
5. **Final Insights Report** (`05_final_insights.pdf`)  
   - Business insights and recommendations synthesizing all steps.

## Example SQL KPIs
```
query = """ select Region, round(sum(Sales),2) as 'total_sales', round(sum(Profit),2) as 'total_profit' from

query = """ select `Product Name` as 'prod_name' , round(sum(Profit),2) as 'profit' from superstore
```

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
