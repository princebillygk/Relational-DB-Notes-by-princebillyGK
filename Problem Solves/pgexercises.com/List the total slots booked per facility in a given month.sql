SELECT
facid,
sum(slots) AS "Total Slots"
FROM 
cd.bookings 
WHERE
EXTRACT(month FROM starttime) = 9
AND EXTRACT (year FROM starttime) = 2012
GROUP BY facid ORDER BY "Total Slots" 
