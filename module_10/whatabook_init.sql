/*
    Title: whatabook_init.sql
    Author: Andrey Alexandrov
    Date: February 20, 2022
    Description: WhatABook database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant this user all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop tables if they are present
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS stores;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS wishlist;

-- create the books table 
CREATE TABLE books (
    book_id     INT             NOT NULL        AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    details     VARCHAR(500)            ,
    author      VARCHAR(200)    NOT NULL,
    PRIMARY KEY (book_id)
); 

-- create the stores table 
CREATE TABLE stores (
    store_id    INT             NOT NULL,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY (store_id)
); 

-- create the users table 
CREATE TABLE users (
    user_id     INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    PRIMARY KEY (user_id)
); 

-- create the wishlist table 
CREATE TABLE wishlist (
    wishlist_id INT             NOT NULL        AUTO_INCREMENT,
    user_id     INT             NOT NULL,
    book_id     INT             NOT NULL,
    PRIMARY KEY (wishlist_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- insert book records
INSERT INTO books(book_id, book_name, details, author)
    VALUES(1, 'How to Make Cookies', 'ISBN 12345', 'Liza Small');
INSERT INTO books(book_id, book_name, details, author)
    VALUES(2, 'My Planet', 'ISBN 23456', 'Tim Robertson');
INSERT INTO books(book_id, book_name, details, author)
    VALUES(3, 'Wild Animals', 'ISBN 34567', 'Anna Sholtz');
INSERT INTO books(book_id, book_name, details, author)
    VALUES(4, 'Cars', 'ISBN 45678', 'Viktoria Taylor');
INSERT INTO books(book_id, book_name, details, author)
    VALUES(5, 'Tractors', 'ISBN 56789', 'Mama Mia');
INSERT INTO books(book_id, book_name, details, author)
    VALUES(6, 'A Love Story', 'ISBN 54321', 'Anthony Big');
INSERT INTO books(book_id, book_name, details, author)
    VALUES(7, 'Karate for Beginners', 'ISBN 65432', 'Tom Jackson');
INSERT INTO books(book_id, book_name, details, author)
    VALUES(8, 'New York Visitor Guide', 'ISBN 76543', 'Bruce Strong');
INSERT INTO books(book_id, book_name, details, author)
    VALUES(9, 'Lovely Cats', 'ISBN 87654', 'Donald Hopkins');

-- insert store records
INSERT INTO stores(store_id, locale)
    VALUES(1, '123 6th Avenue, New York, NY, 10101');

-- insert user records 
INSERT INTO users(user_id, first_name, last_name)
    VALUES(1, 'Andrew', 'Jackson');
INSERT INTO users(user_id, first_name, last_name)
    VALUES(2, 'Bob', 'Smith');
INSERT INTO users(user_id, first_name, last_name)
    VALUES(3, 'Nick', 'Johnson');

-- insert wishlist records
INSERT INTO wishlist(wishlist_id, user_id, book_id)
    VALUES(1, 1, 9);
INSERT INTO wishlist(wishlist_id, user_id, book_id)
    VALUES(2, 2, 5);
INSERT INTO wishlist(wishlist_id, user_id, book_id)
    VALUES(3, 3, 6);



