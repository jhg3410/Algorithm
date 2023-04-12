SELECT count(USER_ID) as USES
FROM USER_INFO
where JOINED like '2021%' and 20 <= AGE and AGE <= 29
