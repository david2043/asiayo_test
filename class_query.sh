#!/bin/bash

DB_NAME="student.db"

sqlite3 "$DB_NAME" "
SELECT c.class
FROM score AS s
JOIN class AS c
    ON s.name = c.name
ORDER BY s.score DESC
LIMIT 1 OFFSET 1;
"
