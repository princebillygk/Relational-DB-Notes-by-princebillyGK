SELECT starttime FROM cd.bookings b, cd.members m where b.memid = m.memid and m.firstname = 'David' and m.surname = 'Farrell';
