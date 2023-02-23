-- Script creates database 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
--use data base creaeted
USE `hbtn_0d_usa`;
-- Script creates table 'states' in database 'hbtn_0d_usa' created
-- id colun in table 'states is given 'AUTO', 'NOT NULL'  and 'PRIMARY KEY' constraints
CREATE TABLE IF NOT EXISTS states(id INT AUTO NOT NULL PRIMARY KEY,name VARCHAR(256));
