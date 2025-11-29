-- 5-unique_id.sql
-- Creates the table unique_id with id INT default 1 and unique, and name VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
