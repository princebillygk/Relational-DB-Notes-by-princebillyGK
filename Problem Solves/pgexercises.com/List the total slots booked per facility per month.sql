ELECT
facid,
EXTRACT(MONTH from starttime) as month,
sum(slots) AS "Total Slots"
FROM cd.bookings
WHERE
EXTRACT (year FROM starttime) = 2012
GROUP BY facid, month ORDER BY facid, month; 

