SELECT ingredient_type, sum(total_order) as TOTAL_ORDER
from first_half join icecream_info
where first_half.flavor = icecream_info.flavor
group by ingredient_type
order by TOTAL_ORDER