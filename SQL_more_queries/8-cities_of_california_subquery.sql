-- LISTS ALL CITIES OF CALI FOUND IN DATABASE
SELECT cities.id, cities.name FROM cities WHERE cities.state_id = (
    SELECT states.id FROM states WHERE states.name = 'California'
)
ORDER BY cities.id ASC;