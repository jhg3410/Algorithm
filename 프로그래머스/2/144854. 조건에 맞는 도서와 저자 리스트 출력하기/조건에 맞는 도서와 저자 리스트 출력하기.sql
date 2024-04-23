-- 코드를 입력하세요
SELECT book.book_id, author.author_name, DATE_FORMAT(book.published_date, "%Y-%m-%d") as PUBLISHED_DATE
from book join author using(AUTHOR_ID)
where book.category = '경제'
order by 3