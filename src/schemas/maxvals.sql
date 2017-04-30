DROP TABLE if exists MaxValues;


CREATE TABLE MaxValues(
  id SERIAL PRIMARY KEY,
  coin_name VARCHAR(255) not null,
  max_val FLOAT
);
