DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS categories;


CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id INT REFERENCES merchants(id),
    category_id INT REFERENCES categories(id),
    description VARCHAR(255),
    amount FLOAT,
    date DATE

);
