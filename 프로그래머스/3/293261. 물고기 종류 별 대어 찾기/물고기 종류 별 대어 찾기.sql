WITH TOP AS(
    SELECT FISH_TYPE, MAX(LENGTH) as "MAX_LENGTH" FROM FISH_INFO
    GROUP BY FISH_TYPE)
    
select id, fish_name, length
from fish_name_info join fish_info using(fish_type)
where (fish_type, length) in (select * from top)
order by id