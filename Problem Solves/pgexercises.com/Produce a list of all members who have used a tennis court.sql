SELECT firstname || ' ' || surname as member, 
f.name as facility
FROM cd.members m 
INNER JOIN
(SELECT DISTINCT memid, facid FROM cd.bookings) b
on m.memid = b.memid
INNER JOIN cd.facilities f on b.facid = f.facid
and f.facid in (0, 1) order by member;
