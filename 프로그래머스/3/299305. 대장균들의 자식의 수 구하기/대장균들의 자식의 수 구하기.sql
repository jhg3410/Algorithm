with T as (
    select a.id, count(b.parent_id) as cnt
    from ECOLI_DATA as a left join ECOLI_DATA as b
    on a.id = b.parent_id
    group by a.id
)

select t.id, t.cnt as "CHILD_COUNT"
from T
