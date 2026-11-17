
USE sales_analytics;

-- 1. Total sales
SELECT SUM(sales) AS total_sales
FROM sales;

-- 2. Total profit
SELECT SUM(profit) AS total_profit
FROM sales;

-- 3. Total orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales;

-- 4. Total customers
SELECT COUNT(DISTINCT customer_name) AS total_customers
FROM sales;

-- 5. Sales by category
SELECT
    category,
    SUM(sales) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- 6. Profit by category
SELECT
    category,
    SUM(profit) AS total_profit
FROM sales
GROUP BY category
ORDER BY total_profit DESC;

-- 7. Sales by region
SELECT
    region,
    SUM(sales) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- 8. Top 10 subcategories
SELECT
    sub_category,
    SUM(sales) AS total_sales
FROM sales
GROUP BY sub_category
ORDER BY total_sales DESC
LIMIT 10;

-- 9. Monthly sales
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(sales) AS monthly_sales
FROM sales
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;

-- 10. Profit by discount
SELECT
    discount,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY discount
ORDER BY discount;
