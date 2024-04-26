select ins.animal_id, ins.name
from animal_ins as ins join animal_outs as outs using(animal_id)
order by DATEDIFF(outs.datetime, ins.datetime) desc
limit 2