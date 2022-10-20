#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE profile(
        Name VARCHAR(30),
        age INT,
    );
    INSERT INTO profile (Name, age) values
        ('adil', 39),
        ('hira', 31),
        ('Umer', 29),

EOSQL