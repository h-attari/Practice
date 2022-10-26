# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
Delete temp1
From Person temp1, Person temp2
Where temp1.id > temp2.id
And temp1.email = temp2.email;