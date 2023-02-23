-- Script creates database 'hbtn_0d_usa'
-- Script creates table 'states' in database 'hbtn_0d_usa' created
-- id colun in table 'states is given 'AUTO', 'NOT NULL'  and 'PRIMARY KEY' constraints
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO NOT NULL,
    name VARCHAR(256)
);
