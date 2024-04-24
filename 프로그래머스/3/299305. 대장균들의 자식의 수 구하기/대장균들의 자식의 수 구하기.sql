select parent.id, count(child.parent_id) as "CHILD_COUNT"
from ECOLI_DATA as parent left join ECOLI_DATA as child
on parent.id = child.parent_id
group by parent.id
order by parent.id