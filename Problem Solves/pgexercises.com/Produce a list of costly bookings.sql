SELECT m.firstname || ' ' || m.surname as member, name as facility, CASE WHEN m.memid =  0 THEN f.guestcost* b.slots ELSE f.membercost* b.slots END as cost
  FROM cd.members m
 INNER 
  JOIN cd.bookings b
    ON m.memid                                                                        =  b.memid
 INNER 
  JOIN cd.facilities f
    ON b.facid                                                                        =  f.facid
 WHERE b.starttime::date                                                              =  '2012-09-14'
   AND (
               (
                       m.memid                                                                        =  0
           AND b.slots * f.guestcost                                                          >  30
               )
            or (
                       m.memid                                                                        != 0
           AND b.slots * f.membercost                                                         >  30
       )
       )
 ORDER BY cost DESC;

