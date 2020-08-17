SELECT
	f.facid,
		sum(b.slots) AS "Total Slots"
		FROM 
		cd.facilities f 
		INNER JOIN cd.bookings b 
			ON f.facid = b.facid
			INNER JOIN cd.members m 
				ON m.memid = b.memid GROUP BY f.facid ORDER BY f.facid; 
