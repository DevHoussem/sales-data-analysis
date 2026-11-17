
CREATE DATABASE IF NOT EXISTS sales_analytics;

USE sales_analytics;

CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(50),
    order_date DATE,
    customer_name VARCHAR(150),
    region VARCHAR(50),
    category VARCHAR(100),
    sub_category VARCHAR(100),
    sales DECIMAL(12, 2),
    quantity INT,
    discount DECIMAL(6, 3),
    profit DECIMAL(12, 2)
);
