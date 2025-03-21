-- sales_etl_schema.sql

-- Create Sales Transactions Table in AWS Redshift
CREATE TABLE sales_transactions (
    row_id INT PRIMARY KEY,
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    country_region VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code INT,
    region VARCHAR(50),
    product_id VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255),
    sales DECIMAL(12,2),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(12,2),
    profit_margin DECIMAL(5,2),
    processing_time_days INT
);

-- Create Indexes for faster query performance
CREATE INDEX idx_order_date ON sales_transactions(order_date);
CREATE INDEX idx_customer_id ON sales_transactions(customer_id);
CREATE INDEX idx_product_id ON sales_transactions(product_id);

-- Transformation: Calculate total sales and profit per region
SELECT region, SUM(sales) AS total_sales, SUM(profit) AS total_profit
FROM sales_transactions
GROUP BY region
ORDER BY total_sales DESC;

-- Identify top-selling products
SELECT product_name, SUM(sales) AS total_sales, SUM(quantity) AS total_quantity
FROM sales_transactions
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;
