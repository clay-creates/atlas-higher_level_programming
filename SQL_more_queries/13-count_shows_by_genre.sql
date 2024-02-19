-- LIST ALL GENRES AND DISPLAY NUMBER OF SHOWS LINKED TO EACH
SELECT tv_show_genres, COUNT(*) AS number_of_shows
FROM hbtn_0d_tvshows
GROUP BY tv_show_genres
HAVING COUNT(*) > 0
ORDER BY number_of_shows ASC;