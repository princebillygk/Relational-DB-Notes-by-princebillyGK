SELECT f.facid, name, sum(slots * 0.50)
FROM cd.bookings b, cd.facilities f 
WHERE b.facid = f.facid GROUP BY f.facid ORDER BY facid;
