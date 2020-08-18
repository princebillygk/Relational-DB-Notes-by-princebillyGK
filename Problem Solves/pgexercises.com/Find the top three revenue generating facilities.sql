SELECT *
FROM (
        SELECT name, rank()
        OVER (
                ORDER BY sum( CASE WHEN memid = 0 THEN guestcost * slots ELSE membercost * slots END) DESC
        ) AS rank
        FROM cd.bookings b, cd.facilities f
        WHERE b.facid                 = f.facid
        GROUP BY f.facid
) t
WHERE rank                    < 4;
