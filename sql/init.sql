CREATE DATABASE IF NOT EXISTS contacts_manager;

USE contacts_manager;

CREATE TABLE IF NOT EXISTS Contacts(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) UNIQUE
);

INSERT INTO Contacts(first_name, last_name, phone_number) VALUES ("Israel", "Israeli", "0501234567")
