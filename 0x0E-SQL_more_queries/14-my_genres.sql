-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- cat 14-my_genres.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT
	tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON
	tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON
	tv_shows.id = tv_show_genres.show_id
WHERE
	tv_shows.title = 'Dexter'
ORDER BY 
	tv_genres.name
	ASC;
