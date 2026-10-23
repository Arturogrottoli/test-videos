-- Final price per product.
-- Policy: a NULL discount means "no discount", so the product is sold at full price.
SELECT id, name, price, discount_pct,
       ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) AS final_price
FROM products;
