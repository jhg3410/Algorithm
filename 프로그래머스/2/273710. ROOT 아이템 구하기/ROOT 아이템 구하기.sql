-- 코드를 작성해주세요
select item_id, item_name
from item_info join item_tree using(item_id)
where item_tree.parent_item_id is NULL