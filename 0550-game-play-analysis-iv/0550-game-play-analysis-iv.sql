# Write your MySQL query statement below
select round(
    (
        select count(distinct e1.player_id) 
        from Activity e1 
        join Activity e2 
        on e1.player_id= e2.player_id 
        where datediff(e1.event_date,e2.event_date)=1
        -- Make sure e2.event_date is first login
        and e2.event_date = (
            select min(event_date)
            from Activity
            where player_id = e1.player_id
        )
    )
        /count(distinct player_id)
        ,2)
        as fraction
from Activity