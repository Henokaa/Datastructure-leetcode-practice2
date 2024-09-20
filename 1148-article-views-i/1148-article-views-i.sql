# Write your MySQL query statement below
# ,sort ID asc
Select Distinct author_id as id
From Views
where author_id = viewer_id
Order by author_id 