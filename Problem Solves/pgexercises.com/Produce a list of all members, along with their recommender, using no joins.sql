SELECT DISTINCT firstname || ' ' || surname as member, (
                SELECT firstname || ' ' || surname AS recommender
                  FROM cd.members m2
 WHERE m2.memid = m.recommendedby
       ) AS recommender
  FROM cd.members m
 ORDER BY member;
