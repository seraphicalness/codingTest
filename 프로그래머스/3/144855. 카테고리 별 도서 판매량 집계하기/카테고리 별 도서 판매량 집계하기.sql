-- 코드를 입력하세요
SELECT A.CATEGORY, SUM(B.SALES) AS TOTAL_SALES
FROM BOOK A, BOOK_SALES B 
WHERE A.BOOK_ID = B.BOOK_ID AND DATE_FORMAT(B.SALES_DATE, '%Y-%m-%d')
LIKE '%2022-01%'
GROUP BY A.CATEGORY 
ORDER BY A.CATEGORY ASC;

# SELECT a.category, sum(b.sales) as total_sales
# from book a, book_sales b
# where a.book_id=b.book_id and date_format(b.sales_date, '%Y-%m-%d') 
# like '2022-01%'
# group by a.category
# order by a.category