# Write your MySQL query statement below
Select player_id, Min(event_date) As first_login
From Activity
Group By player_id;