SELECT m1.firstname, m1.surname
FROM
cd.members m1, (SELECT DISTINCT recommendedby FROM cd.members) m2 
WHERE
m2.recommendedby = m1.memid ORDER BY surname, firstname;
