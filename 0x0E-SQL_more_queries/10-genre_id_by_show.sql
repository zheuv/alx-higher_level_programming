-- Import the database dump from hbtn_0d_tvshows
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- cat 10-genre_id_by_show.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT 
	tv_shows.title,
	tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON
	tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title,
	tv_show_genres.genre_id 
	ASC;
