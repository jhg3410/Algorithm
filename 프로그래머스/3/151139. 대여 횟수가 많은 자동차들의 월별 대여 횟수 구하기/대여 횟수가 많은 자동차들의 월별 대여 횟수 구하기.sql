-- 기간동안 대여 횟수가 5회 이상인 친구들을 가져오자
with above_five as (
    SELECT car_id
    from car_rental_company_rental_history
    where Year(start_date) = 2022 and Month(start_date) between 8 and 10
    group by car_id
    having count(car_id) >= 5
)

select month(history.start_date) as "Month", history.car_id, count(history.car_id) as "RECORDS"
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as history join above_five using(car_id)
where Year(start_date) = 2022 and Month(start_date) between 8 and 10
group by Month, car_id
order by 1 asc , 2 desc