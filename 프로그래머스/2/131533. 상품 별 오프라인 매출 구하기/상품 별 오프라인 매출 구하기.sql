SELECT product_code, sum((product.price * offline_sale.sales_amount)) as "SALES"
from product join offline_sale
where product.product_id = offline_sale.product_id
group by product_code
order by 2 desc, 1