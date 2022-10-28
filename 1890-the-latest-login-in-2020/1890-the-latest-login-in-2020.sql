# Write your MySQL query statement below
Select user_id, Max(time_stamp) As last_stamp
From Logins
Where time_stamp > "2019-12-31 23:59:59"
And time_stamp < "2021-01-01 00:00:00"
Group By user_id;