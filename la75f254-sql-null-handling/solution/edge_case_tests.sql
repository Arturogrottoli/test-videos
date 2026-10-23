-- Test 1: edge cases for the final price formula (every row must say PASS).
WITH test_cases (test_name, price, discount_pct, expected) AS (
    VALUES ('NULL discount', 100.0, NULL, 100.0),
           ('Zero discount', 100.0, 0, 100.0),
           ('Normal discount', 80.0, 25, 60.0),
           ('Full discount', 50.0, 100, 0.0),
           ('Zero price', 0.0, 10, 0.0)
)
SELECT test_name, price, discount_pct, expected,
       ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) AS actual,
       CASE WHEN ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) = expected
            THEN 'PASS' ELSE 'FAIL' END AS result
FROM test_cases;

-- Test 2: no product may have a NULL final price (expected: 0).
SELECT COUNT(*) AS null_final_prices
FROM products
WHERE ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) IS NULL;

-- Test 3: every final price must be between 0 and the original price (expected: 0).
SELECT COUNT(*) AS out_of_range
FROM products
WHERE ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) NOT BETWEEN 0 AND price;
