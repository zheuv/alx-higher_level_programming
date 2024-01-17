--  lists all shows contained in the database hbtn_0d_tvshows
-- cat 11-genre_id_all_shows.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT
	tv_shows.title,
	tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON 
	tv_shows.id = tv_shows_genres.show_id
ORDER BY
	tv_shows.title 
	AND
	tv_show_genres.genre_id
	ASC
