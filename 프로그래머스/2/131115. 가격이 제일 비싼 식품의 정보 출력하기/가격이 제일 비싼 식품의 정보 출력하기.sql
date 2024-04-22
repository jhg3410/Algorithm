with max_product as (
    select max(price) as price from food_product
)

select product_id, product_name, product_cd, category, food_product.price from food_product, max_product where food_product.price = max_product.price