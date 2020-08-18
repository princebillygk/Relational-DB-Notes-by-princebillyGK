SELECT facid, EXTRACT(month FROM starttime) as month, sum(slots) as "Total Slots" 
FROM cd.bookings
WHERE EXTRACT(year FROM  starttime) = 2012
GROUP BY 
ROLLUP (facid, EXTRACT(month FROM starttime)) ORDER BY facid, month;
																		 
