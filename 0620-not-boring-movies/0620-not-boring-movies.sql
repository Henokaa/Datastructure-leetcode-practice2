# movies = odd & des != boring, rating desc, 
select id, movie, description, rating
from cinema
where id%2 != 0 and description != "boring" 
Order by rating DESC