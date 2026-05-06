WITH milk AS 
(
SELECT cart_id
FROM CART_PRODUCTS 
WHERE name = 'milk'
)

SELECT cart_id
FROM CART_PRODUCTS 
WHERE cart_id IN (
SELECT cart_id
FROM milk
) AND name='yogurt'
ORDER BY cart_id