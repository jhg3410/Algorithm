select concat(Quarter(differentiation_date), "Q") as "QUARTER", count(id) as "ECOLI_COUNT"
from ecoli_data
group by QUARTER
order by QUARTER 