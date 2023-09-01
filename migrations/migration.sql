
CREATE TABLE IF NOT EXISTS customers (
    id INT UNIQUE AUTO_INCREMENT,
    email VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(50),
    PRIMARY KEY (email)
);


CREATE TABLE IF NOT EXISTS category (
    id INT UNIQUE AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS vehicle (
    id INT UNIQUE AUTO_INCREMENT,
    category_id INT NOT NULL,
    availability BOOLEAN,
    PRIMARY KEY (id),
    FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS booking (
    id INT UNIQUE AUTO_INCREMENT,
    customer_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    hire_date DATETIME NOT NULL,
    return_date DATETIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(id) ON DELETE CASCADE
);
