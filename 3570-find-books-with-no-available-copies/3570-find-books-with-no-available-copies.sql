# Write your MySQL query statement below
select
    a.book_id as book_id,
    title,
    author,
    genre,
    publication_year,
    current_borrowers
from library_books a
join (
    select 
        book_id,
        count(record_id) as current_borrowers
    from borrowing_records
    where return_date is null
    group by book_id
) as b
on a.book_id = b.book_id
where b.current_borrowers = total_copies
order by current_borrowers desc, title;