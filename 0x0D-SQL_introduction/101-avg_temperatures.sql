-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
--	$ mysql -u root -p hbtn_0c_0 < temperatures.sql
-- Script that displays the average temperature (Fahrenheit) by city
--  ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
