# Write your MySQL query statement below
Select id,
Case
    When p_id Is Null Then "Root"
    When id Not In (Select Distinct(p_id) from Tree Where p_id Is Not Null) Then "Leaf"
    Else "Inner"
End As type
From Tree;