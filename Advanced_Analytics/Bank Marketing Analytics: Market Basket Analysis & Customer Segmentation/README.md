# Advanced Customer Analytics for Banking Campaigns  
### *Market Basket Analysis & Customer Segmentation*  

## 📌 Project Overview  
This project applies **Market Basket Analysis (Apriori algorithm)** and **Customer Segmentation (KMeans clustering)** on a **Bank Marketing dataset** to derive actionable insights for campaign optimization.  

- **Market Basket Analysis** uncovers hidden associations among customer attributes and campaign outcomes.  
- **Customer Segmentation** groups customers into meaningful clusters based on demographics, financial status, and campaign interactions.  

The goal is to help banks **optimize marketing resources, target high-value segments, and design personalized campaigns**.  

---

## ⚙️ Methodology  

### 1. Market Basket Analysis (MBA)  
- **Algorithm**: Apriori (association rules mining)  
- **Steps**:  
  - Data preparation with one-hot encoding  
  - Generate frequent itemsets above minimum support  
  - Derive rules using **support, confidence, and lift**  
  - Select **Top 10 rules (sorted by lift)** for business insights  
- **Key Insight**:  
  - Management professionals with university degrees → suitable for **premium banking products**  
  - Customers with no loans & no defaults → **low-risk, high potential**  
  - Repeated rejectors → **avoid retargeting** unless strong incentive  

### 2. Customer Segmentation  
- **Algorithm**: KMeans Clustering  
- **Data Preparation**: One-hot encoding, standardization  
- **Cluster Selection**: Elbow Method → **k=5**  
- **Validation Metrics**:  
  - Silhouette Score = 0.166 (weak separation, expected overlap)  
  - Davies-Bouldin Index = 1.906 (moderate overlap)  
- **Cluster Profiles**:  
  - 📊 **Cluster 0**: Young, low default, moderate literacy → Cross-sell + joining incentives  
  - 📊 **Cluster 1**: Blue-collar, moderate literacy, housing loans → Cross-sell, entry offers  
  - 📊 **Cluster 2**: Highly literate professionals → Target with advanced products (investment, insurance)  
  - 📊 **Cluster 3**: Technicians, high literacy, housing loans → Target with premium & financial products  
  - 📊 **Cluster 4**: Older, mixed literacy, varying income → Awareness + retirement-focused campaigns  

---

## 💡 Key Business Insights  
- **High-lift, high-confidence rules** → Best for campaign targeting  
- **Cellular contact** is consistently more reliable than telephone  
- **Management/university-educated customers** → prime for premium offers  
- **No loan + no default customers** → safest to target  
- **Avoid repetitive rejectors** to save marketing spend  

---

## 📂 Repository Structure  
```
├── 01_Market_Basket_Analysis.ipynb   # Apriori algorithm, association rules, insights
├── 02_Customer_Segmentation.ipynb    # KMeans clustering, profiling, insights
├── 03_report.pdf                     # Final detailed report
└── README.md                         # Project overview & documentation
```

---

## 📊 Tools & Libraries  
- **Python**: pandas, numpy, matplotlib, seaborn  
- **ML**: mlxtend (Apriori), scikit-learn (KMeans, validation metrics)  
- **Visualization**: matplotlib, seaborn  

---

## ✅ Conclusions  
- **MBA** uncovered non-obvious but high-value customer patterns  
- **Segmentation** highlighted distinct personas for tailored campaigns  
- **Business takeaway**: Banks can enhance conversion by **targeting low-risk, high-literacy, and highly reachable segments**, while reducing waste on repetitive rejectors  

---

## 📢 Future Work  
- Test alternative clustering methods (DBSCAN, hierarchical clustering)  
- Deploy predictive models to forecast campaign success  
- Build a dashboard for real-time analytics  

