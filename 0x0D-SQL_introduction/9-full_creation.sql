-- creates a table 'second_table' in the database hbtn_0c_0 in the MySQL server
-- and add multiple rows.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
VALUES 
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 1),
	(4, "George", 8);
