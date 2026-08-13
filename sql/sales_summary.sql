-- Daily sales summary

SELECT
    transaction_date,
    city,
    category,
    COUNT(DISTINCT transaction_id) AS total_transactions,
    COUNT(DISTINCT customer_id) AS total_customers,
    SUM(quantity) AS total_items_sold,
    ROUND(SUM(total_amount), 2) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_transaction_value

FROM `your_project.your_dataset.transactions`

GROUP BY
    transaction_date,
    city,
    category

ORDER BY
    transaction_date,
    total_revenue DESC;
