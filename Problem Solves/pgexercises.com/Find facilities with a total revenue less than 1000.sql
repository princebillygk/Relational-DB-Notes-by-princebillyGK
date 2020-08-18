iSELECT max(name), sum(revenue) as revenue FROM (SELECT f.facid, name, CASE WHEN memid = 0 THEN guestcost ELSE membercost END * slots AS revenue
	  FROM cd.facilities f, cd.bookings b
	 WHERE f.facid = b.facid) T    
 GROUP BY facid HAVING sum(revenue) < 1000
 ORDER BY revenue 
