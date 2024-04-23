SELECT animal_type, count(animal_id) as "count"
from ANIMAL_INS
group by animal_type
having ANIMAL_TYPE in ("Cat", "Dog")
order by animal_type