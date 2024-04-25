with parents as (
    select parent_item_id from item_tree
    where parent_item_id is not null
)

select item_id, item_name, rarity
from item_info
where item_id not in (select * from parents)
order by item_id desc
