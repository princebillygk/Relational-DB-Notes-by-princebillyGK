SELECT name, sum(CASE WHEN memid = 0 THEN guestcost ELSE membercost END * slots) AS revenue
  FROM cd.facilities f, cd.bookings b
 WHERE f.facid                   = b.facid
 GROUP BY f.facid
 ORDER BY revenue;
