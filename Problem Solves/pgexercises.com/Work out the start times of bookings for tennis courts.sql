SELECT starttime as start, name From 
cd.bookings b, cd.facilities f 
WHERE b.facid = f.facid AND starttime::date = '2012-09-21' AND name LIKE 'Tennis Court%' ORDER BY starttime;
