-- Query Optimization Techniques

-- 1
-- Try to decrease the number of columns called to improve query performance since data is stored in columnar format

select *
from imdb_title_basics
where startYear between 1850 and 1900
and titleType = 'movie'

-- vs

select originalTitle, startYear
from imdb_title_basics
where startYear between 1850 and 1900
and titleType = 'movie'

-- 2
-- Use CTEs to simplify



-- 3
-- Filter early



-- 4
-- Use Window Functions

