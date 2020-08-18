SELECT name, CASE WHEN level   = 1 THEN 'high' WHEN level                                   = 2 THEN 'average' ELSE 'low' END as revenue
FROM (
        SELECT f.name, ntile(3)
        OVER (
                order by sum( CASE WHEN memid = 0 THEN guestcost * slots ELSE membercost * slots END) DESC
        ) as level
        FROM cd.facilities f, cd.bookings b
        WHERE f.facid                 = b.facid
        GROUP BY f.facid
) t
order by level, name;
