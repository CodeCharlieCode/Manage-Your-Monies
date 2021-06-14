DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS profiles;


CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    budget FLOAT
);


CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    category_id INT REFERENCES categories(id) ON DELETE CASCADE,
    description VARCHAR(255),
    amount FLOAT,
    date DATE
);

CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    balance FLOAT,
    total_budget FLOAT

);