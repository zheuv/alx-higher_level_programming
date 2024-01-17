-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- cat 16-shows_by_genre.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT
	tv_shows.title,
	tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON
	tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON
	tv_genres.id = tv_show_genres.genre_id
ORDER BY
	tv_shows.title
	AND
	tv_genres.name
	ASC;
