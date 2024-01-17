-- lists all cities contained in the database hbtn_0d_usa
-- echo 'SELECT * FROM states;' | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'SELECT * FROM cities;' | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa
-- cat 9-cities_by_state_join.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa
SELECT 
	cities.id,
	cities.name,
	states.name
FROM cities
JOIN states on
	cities.state_id = states.id
ORDER BY cities.id ASC
