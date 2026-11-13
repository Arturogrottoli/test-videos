CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    discount_pct REAL
);

INSERT INTO products (id, name, category, price, discount_pct) VALUES
    (1, 'Wireless Mouse', 'Electronics', 25.00, 10),
    (2, 'USB-C Cable', 'Electronics', 12.50, NULL),
    (3, 'Desk Lamp', 'Home', 40.00, 15),
    (4, 'Coffee Mug', 'Home', 9.99, 0),
    (5, 'Board Game', 'Toys', 34.90, NULL),
    (6, 'Puzzle 1000 pcs', 'Toys', 18.00, 20),
    (7, 'Notebook Pack', 'Books', 7.50, 5),
    (8, 'Cookbook', 'Books', 29.00, NULL),
    (9, 'Bluetooth Speaker', 'Electronics', 59.99, 25),
    (10, 'Throw Pillow', 'Home', 22.00, 10),
    (11, 'Action Figure', 'Toys', 15.00, 0),
    (12, 'Mystery Novel', 'Books', 14.99, NULL);
