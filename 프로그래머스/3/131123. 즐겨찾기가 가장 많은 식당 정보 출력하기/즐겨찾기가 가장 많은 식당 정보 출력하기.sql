with max_favorite as (
    select food_type, max(favorites)
    from rest_info
    group by food_type
)

select food_type, rest_id, rest_name, favorites
from rest_info
where (food_type, favorites) in (select * from max_favorite)
order by food_type desc