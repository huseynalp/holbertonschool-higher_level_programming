-- 16-no_links.sql
-- List all records of second_table where name is not NULL or empty, showing score and name, ordered by score descending

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
