CREATE DATABASE your_database_name;
USE your_database_name;

CREATE TABLE chat_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role ENUM('user', 'system'),
    content TEXT
);