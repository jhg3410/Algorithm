SELECT mcdp_cd as "진료과 코드", count(apnt_no) as "5월예약건수"
from appointment
where year(apnt_ymd) = '2022' and month(apnt_ymd) = '5'
group by mcdp_cd
order by 2, 1