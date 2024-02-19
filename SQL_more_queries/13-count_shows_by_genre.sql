-- LIST ALL GENRES AND DISPLAY NUMBER OF SHOWS LINKED TO EACH
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;