with rental_oct as (
    select distinct car_id
    from car_rental_company_rental_history
    where month(start_date) = 10
)

SELECT car_id
from car_rental_company_car join rental_oct using(car_id)
where car_type = "세단"
order by 1 desc
