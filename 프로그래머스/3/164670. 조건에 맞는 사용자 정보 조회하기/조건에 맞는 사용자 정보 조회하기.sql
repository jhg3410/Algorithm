-- 3명 이상인 user_id 를 뺴낸다
with more_three as (
    SELECT writer_id
    from used_goods_board
    # where status = "DONE"
    group by writer_id
    having count(*) >= 3
)

select user_id, nickname, concat(city, " ", street_address1, " ", STREET_ADDRESS2) as "전체주소", 
concat(substring(TLNO,1,3), "-", substring(TLNO,4,4), "-", substring(TLNO,8,4)) as "전화번호"
from used_goods_user
where user_id in (select * from more_three)
order by user_id desc