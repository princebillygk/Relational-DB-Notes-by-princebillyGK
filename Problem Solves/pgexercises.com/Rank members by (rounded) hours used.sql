SELECT firstname, surname, round(sum(slots * 0.5) / 10) * 10 as hours, rank()
                  over (
                 ORDER BY round(sum(slots * 0.5) / 10) * 10 DESC
       )
  FROM cd.bookings b, cd.members m
 WHERE b.memid = M.memid
 GROUP BY m.memid
 order by rank, surname;
