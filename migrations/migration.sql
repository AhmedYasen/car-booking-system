
CREATE TABLE IF NOT EXISTS customers (
    email VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(50),
    PRIMARY KEY (email)
);
