-- 코드를 입력하세요
SELECT CATEGORY, sum(SALES) as TOTAL_SALES
from (
    select b.BOOK_ID,b.CATEGORY,bs.SALES_DATE,bs.SALES
    from BOOK as b
    join BOOK_SALES as bs on b.BOOK_ID = bs.BOOK_ID
    where substring(bs.SALES_DATE,1,7) = '2022-01'
) as bs_i
group by CATEGORY
order by CATEGORY asc;