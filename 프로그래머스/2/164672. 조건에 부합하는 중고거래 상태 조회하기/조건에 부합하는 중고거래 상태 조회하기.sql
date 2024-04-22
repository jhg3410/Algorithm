SELECT board_id, writer_id, title, price, 
CASE
    when used_goods_board.STATUS = "SALE" THEN "판매중"
    when used_goods_board.STATUS = "RESERVED" THEN "예약중"
    ELSE "거래완료"
    END as "STATUS"
from used_goods_board
where year(created_date) = '2022' and month(created_Date) = '10' and day(created_date) = '5'
order by board_id desc