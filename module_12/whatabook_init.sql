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
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;

-- create the book table 
CREATE TABLE book (
    book_id     INT             NOT NULL        AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    details     VARCHAR(500)            ,
    author      VARCHAR(200)    NOT NULL,
    PRIMARY KEY (book_id)
); 

-- create the store table 
CREATE TABLE store (
    store_id    INT             NOT NULL,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY (store_id)
); 

-- create the user table 
CREATE TABLE user (
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
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id)
);

-- insert book records
INSERT INTO book(book_name, details, author)
    VALUES('How to Make Cookies', 'ISBN 12345', 'Liza Small');
INSERT INTO book(book_name, details, author)
    VALUES('My Planet', 'ISBN 23456', 'Tim Robertson');
INSERT INTO book(book_name, details, author)
    VALUES('Wild Animals', 'ISBN 34567', 'Anna Sholtz');
INSERT INTO book(book_name, details, author)
    VALUES('Cars', 'ISBN 45678', 'Viktoria Taylor');
INSERT INTO book(book_name, details, author)
    VALUES('Tractors', 'ISBN 56789', 'Mama Mia');
INSERT INTO book(book_name, details, author)
    VALUES('A Love Story', 'ISBN 54321', 'Anthony Big');
INSERT INTO book(book_name, details, author)
    VALUES('Karate for Beginners', 'ISBN 65432', 'Tom Jackson');
INSERT INTO book(book_name, details, author)
    VALUES('New York Visitor Guide', 'ISBN 76543', 'Bruce Strong');
INSERT INTO book(book_name, details, author)
    VALUES('Lovely Cats', 'ISBN 87654', 'Donald Hopkins');

-- insert store records
INSERT INTO store(store_id, locale)
    VALUES(1, '123 6th Avenue, New York, NY, 10101');

-- insert user records 
INSERT INTO user(first_name, last_name)
    VALUES('Andrew', 'Jackson');
INSERT INTO user(first_name, last_name)
    VALUES('Bob', 'Smith');
INSERT INTO user(first_name, last_name)
    VALUES('Nick', 'Johnson');

-- insert wishlist records
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Andrew'), 
        (SELECT book_id FROM book WHERE book_name = 'Lovely Cats')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Bob'), 
        (SELECT book_id FROM book WHERE book_name = 'Tractors')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Nick'), 
        (SELECT book_id FROM book WHERE book_name = 'A Love Story')
    );



