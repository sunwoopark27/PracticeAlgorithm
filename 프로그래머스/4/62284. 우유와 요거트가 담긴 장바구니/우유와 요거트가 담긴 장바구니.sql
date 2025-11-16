with milk as 
(
select cart_id
from CART_PRODUCTS 
where name = 'milk'
)

select cart_id
from CART_PRODUCTS 
where cart_id in (
select cart_id
from milk
) and name='yogurt'
order by cart_id