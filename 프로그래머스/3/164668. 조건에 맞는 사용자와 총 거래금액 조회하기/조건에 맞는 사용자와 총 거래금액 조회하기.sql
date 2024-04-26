# 일단 총 금액의 합이 70이 넘는 애들만 뽑자 writer_id 로

with rollerty as (
    select writer_id, sum(price) as sum_price
    from used_goods_board
    where status = "DONE"
    group by writer_id
    having sum(price) >= 700000
)


select USED_GOODS_USER.user_id, USED_GOODS_USER.nickname, rollerty.sum_price as "TOTAL_SALES"
from USED_GOODS_USER  join rollerty on used_goods_user.user_id = rollerty.writer_id
order by 3