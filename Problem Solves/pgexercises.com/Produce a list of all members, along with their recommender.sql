SELECT m1.firstname as memfname, m1.surname as memsname, m2.firstname as recfname, m2.surname as recsname
  FROM cd.members m1
  LEFT 
  JOIN cd.members m2
    ON m1.recommendedby = m2.memid
 ORDER BY memsname, memfname;
