SELECT facid, sum(slots) AS "Total Slots" 
FROM cd.bookings
GROUP BY facid
ORDER by "Total Slots" DESC LIMIT 1;

