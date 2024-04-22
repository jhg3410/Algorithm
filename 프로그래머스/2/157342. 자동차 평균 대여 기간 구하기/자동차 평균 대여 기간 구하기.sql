with durations as  (
    select car_id, DATEDIFF(end_date, start_date) + 1 as duration
    from car_rental_company_rental_history
)


select car_id as CAR_ID, round(avg(duration),1) as AVERAGE_DURATION
from durations
group by car_id
having avg(duration) >= 7
order by 2 desc, 1 desc