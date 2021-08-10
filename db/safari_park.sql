DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS staffs;

CREATE TABLE staffs (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    animal_type VARCHAR(255),
    staff_id INT REFERENCES staffs(id)
);