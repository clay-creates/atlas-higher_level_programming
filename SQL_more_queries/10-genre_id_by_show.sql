-- LIST SHOWS IN HBTN_0D_TVSHOWS
SELECT tv_shows.title, tv_show_genres.genre.id 
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show.state_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre.id ASC;