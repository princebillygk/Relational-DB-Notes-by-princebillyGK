SELECT facid, sum
  FROM (
                SELECT facid, sum(slots) as sum, rank()
                                  over (
                                 ORDER BY sum(slots) DESC
                       ) AS rank
                  FROM cd.bookings
 GROUP BY facid
       ) t
 WHERE rank = 1;
