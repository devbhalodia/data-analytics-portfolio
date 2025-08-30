# 📊 Superstore Sales & Customer Analytics  

## 📌 Objective  
The aim of this project is to analyze **Superstore sales and customer behavior** to identify key drivers of business performance, uncover growth opportunities, and provide actionable recommendations.  
This end-to-end project covers:  
- **Data Cleaning** for accuracy and consistency  
- **Exploratory Data Analysis (EDA)** to study sales & profit patterns  
- **Time Series Forecasting (Prophet)** for predicting sales trends  
- **RFM Customer Segmentation** to classify customers into High, Mid, and Low value groups  
- **SQL-based KPI Extraction** for business insights  
- **Interactive Dashboard (Power BI)** for visualization and decision-making support  

---

## 🗂️ Data Source  
The dataset used is the **Superstore Dataset** from Kaggle:  
🔗 [Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)  

Each row represents a **unique customer transaction**, containing details such as:  
- Order date  
- Product purchased  
- Quantity & Discount  
- Sales value & Profit  
- Customer information  
- Shipping mode, Segment, Region  

---

## ⚙️ Workflow  

1. **Data Cleaning**  
   - Fixed datatypes, standardized column names  
   - Checked for nulls & duplicates (none found)  

2. **Exploratory Data Analysis (EDA)**  
   - **Univariate Analysis** → category-wise & region-wise insights  
   - **Bivariate Analysis** → sales, profit, discount & quantity relations  
   - Key takeaway: Profitability is volatile across products and shipping modes.  

3. **Time Series Forecasting (Prophet)**  
   - Predicted **next 6 months sales**  
   - Found **seasonality & cyclic trends**  
     - Q4 & early Q1 → strong spikes (holiday/New Year)  
     - Q2 dip → recovery in April, followed by slowdown in Q2–Q3  

4. **RFM Customer Segmentation**  
   - Segmented customers into:  
     - **High Value (39.6%)** – Loyal & high spenders  
     - **Mid Value (35.7%)** – Potential to be upgraded  
     - **Low Value (24.7%)** – Least engaged, risk of churn  

5. **SQL KPI Extraction**  
   - Queried important KPIs such as:  
     - Average Order Value (AOV)  
     - Profit Margin  
     - Sales & Profit by Region  
     - Category/Sub-Category contribution  
     - Discount impact on profits  
   - Integrated into a **Power BI Dashboard**  

---

## 📈 Key Insights  

- **Profitability Volatility** → High profits & heavy losses exist across shipping modes, categories, and discounts.  
- **Seasonality Matters** → Sales peak in Q4 (holidays) and recover every April, but slow down in mid-year.  
- **Customer Engagement** → Nearly 40% high-value customers, but ~25% low-value segment shows disengagement risk.  
- **Discounts > 20%** → Often lead to losses, suggesting pricing policy revision is needed.  
- **Regional Nuance** → West & East drive most sales, but South underperforms and needs marketing focus.  

---

## 💡 Recommendations  

1. **Seasonal Planning**  
   - Stock up & strengthen logistics for Q4 & Jan–Apr peaks.  
   - Introduce loyalty rewards during off-season dips.  

2. **Pricing & Discount Policy**  
   - Avoid excessive discounts (>20%) to protect margins.  
   - Revisit discount structure for bulk buyers & low-margin categories.  

3. **Customer Strategy**  
   - High Value → retain with loyalty programs  
   - Mid Value → targeted marketing to upgrade them  
   - Low Value → retention offers, reminders, and engagement campaigns  

4. **Regional Focus**  
   - Push marketing & discounts in the **South region** to boost engagement.  

---

## 📊 Dashboard Preview  
The Power BI dashboard enables interactive exploration of:  
- Sales & Profit trends  
- Regional performance  
- Product category contributions  
- Discount vs Profit impact  
- RFM segmentation insights  

---

## 🛠️ Tech Stack  

- **Languages/Tools:** Python (Pandas, Matplotlib, Seaborn, Prophet), SQL, Power BI  
- **Libraries:** Prophet, Numpy, Scikit-learn, Matplotlib, Seaborn  
- **Visualization:** Power BI Interactive Dashboard  
- **Data Source:** Kaggle Superstore Dataset  

---

## ✅ Conclusion  
This project combines **data analysis, forecasting, and segmentation** into a complete end-to-end business intelligence workflow.  
By addressing **pricing inefficiencies**, improving **customer retention**, and leveraging **seasonal demand trends**, the business can strengthen profitability and ensure sustainable growth.  
