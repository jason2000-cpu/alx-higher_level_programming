--Script creates a database 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Script to use the database created
USE hbtn_0d_usa;
-- Script to create table 'cities' in the database 'hbtn_0d_usa';
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL, state_id INT NOT NULL FOREIGN KEY (states(id)), name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
