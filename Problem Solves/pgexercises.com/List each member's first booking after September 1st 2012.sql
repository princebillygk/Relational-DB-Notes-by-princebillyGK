SELECT surname, firstname, m.memid, min(starttime)
FROM cd.bookings b, cd.members m 
WHERE b.memid = m.memid and starttime >= '2012-09-01'
GROUP BY m.memid ORDER BY memid;
