# Sales Data ETL & Data Warehouse Project

## 📌 Overview
This project extracts, transforms, and loads (ETL) sales data into an **AWS Redshift Data Warehouse**, providing insights using **SQL queries and Power BI dashboards**.

## 🔧 Technologies Used
- **Python** (Pandas, SQLAlchemy, Boto3)
- **AWS Services** (S3, Redshift)
- **SQL** (PostgreSQL/Redshift)
- **Power BI/Tableau**

## 📂 Project Structure
```
📂 Banking-Sales-ETL
 ├── 📂 scripts/                # Python ETL scripts
 │   ├── etl_pipeline.py       # Main ETL script
 │   ├── config.py             # AWS & DB credentials (dummy values)
 ├── 📂 sql/                   # SQL schema & queries
 │   ├── sales_etl_schema.sql  # Table creation & transformations
 ├── 📜 README.md              # Project documentation
```

## 🚀 How to Run the Project
### 1️⃣ Setup AWS & Redshift
- Create an **S3 bucket** for raw sales data.
- Setup an **AWS Redshift cluster**.
- Update **config.py** with credentials.

### 2️⃣ Run the ETL Pipeline
```sh
python etl_pipeline.py
```

### 3️⃣ Verify Data in Redshift
```sql
SELECT * FROM sales_transactions LIMIT 10;
```

## 📊 Power BI/Tableau Visualization
- Import the **Redshift sales data** into Power BI/Tableau.
- Create **dashboards for total sales, profit trends, top-selling products, etc.**

## 📈 Key Insights
- **Top-Selling Regions & Products**
- **Profit Margins Across Categories**
- **Discount Impact on Revenue**

