# Analyzing User Behavior in Cosmetics E-Commerce  
### Funnel Drop-offs and Retention Cohorts  

## Project Overview  
This project analyzes user behavior in an **E-Commerce Cosmetics Shop** using event-level data from **Oct 2019 – Feb 2020**. It focuses on two essential areas:  

1. **Funnel Analysis** – Understanding how users move from *viewing → carting → purchasing* and where the biggest drop-offs occur.  
2. **Retention Cohort Analysis** – Measuring how well the business retains its customers after their first purchase.  

The goal of this project was to simulate a **real-world data analyst case study**, extract insights, and provide **business recommendations** that can help optimize conversions and customer loyalty.  

Dataset: [Kaggle – E-commerce Events History in Cosmetics Shop](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop)  

---

## Tech Stack  
- **Python** (Pandas, Matplotlib, Seaborn) → Data cleaning, analysis, visualization  
- **Power BI** → Interactive dashboard creation  
- **Jupyter/Colab Notebook** → Code & step-by-step analysis  

---

## Key Analyses  

### 1. Funnel Analysis  
- **Overall Funnel (Oct–Feb)**:  
  - Views: 1.59M → Carts: 398K → Purchases: 110K  
  - Overall View → Purchase Conversion: **6.92%**  
  - Biggest bottleneck: **View → Cart (75% drop-off)**  

- **Month-over-Month Funnel**:  
  - Best conversion in **Nov–Jan (holiday season)**, with November peaking at **8.86%** overall conversion.  
  - Cart → Purchase drop-offs improved during festive campaigns.  

- **Adjusted Funnel with Cart Removals**:  
  - High **remove_from_cart activity in Nov–Feb**, showing user indecisiveness.  
  - Once items remain in the cart, purchase likelihood increases significantly (Nov purchase rate: 76%).  

- **Brand Segmentation**:  
  - Leaders: **Irisk (19.77%)**, Runail, Grattol  
  - Laggards: **Kapous (7.84%)**, Estel (9.95%)  
  - Add-to-cart behavior was the main differentiator across brands.  

---

### 2. Retention Cohort Analysis  
- Cohorts formed by **first purchase month**.  
- **Month 1 Retention**: Highest in Oct cohort (18.49%), but overall less than 20% across months.  
- Long-term loyalty is weak – **over 80% of users churn after first purchase**.  
- Festive season improved short-term retention, but loyalty dropped post-January.  

---

## Dashboard  
An interactive Power BI dashboard was created with 7 visuals:  
1. Funnel Chart – Overall conversion stages  
2. Line Chart – Monthly conversion trend  
3. Clustered Column – Drop-off comparison (View→Cart vs Cart→Purchase)  
4. Combo Chart – Adjusted funnel with cart removals  
5. Clustered Bar – Conversion by top brands  
6. Matrix Heatmap – Retention cohorts  
7. KPI Cards – Overall Conversion % and Cart Abandonment %  

---

## Key Insights  
- Conversion rate (6.92%) is above typical e-commerce benchmarks, but **browsers rarely convert to carting**.  
- **Cart abandonment (72%)** is a major leakage point.  
- **Festive campaigns drive results** – Nov–Jan outperforms other months.  
- **Brand disparities** are large; strong performers dominate conversions.  
- **Customer loyalty is weak** – retention drops off heavily after first purchase.  

---

## Recommendations  
- Improve **product pages** with clearer descriptions, reviews, and images to convert browsers into cart users.  
- **Reduce cart abandonment** through checkout optimization, more payment options, and timely reminders.  
- Replicate **holiday campaign strategies** in off-season with smaller discounts, time-limited offers, and rewards.  
- **Promote lagging brands** via discounts, bundling, and better placement while leveraging strong brands as traffic drivers.  
- Strengthen **customer retention** with loyalty programs, personalized marketing, and targeted re-engagement for one-time buyers.  

---

## Repository Structure  
```
01_Funnel_Analysis_&_Retention_Cohort.ipynb   # Python analysis notebook
02_Dashboard.pbix                            # Power BI dashboard template
03_Report.pdf                                # Detailed project report
images/                                      # Dashboard screenshot
README.md                                    # Project documentation
```

---

## Conclusion  
This project demonstrates how funnel analysis and retention cohorts can uncover **conversion bottlenecks** and **loyalty challenges** in e-commerce. While the shop has strong seasonal sales, long-term retention and cart abandonment remain critical improvement areas.  
