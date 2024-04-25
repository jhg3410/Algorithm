with best_board as(
    select board_id
    from used_goods_board
    where views = (select max(views) from used_goods_board) 
)


SELECT concat(concat("/home/grep/src/",BOARD_ID, "/", concat(file_id, file_name)), file_ext) as "FILE_PATH"
from USED_GOODS_FILE join best_board using(board_id)
order by file_id desc
