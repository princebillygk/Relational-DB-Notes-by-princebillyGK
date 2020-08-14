SELECT firstname, surname, joindate
  FROM cd.members
 WHERE joindate = (
                SELECT max(joindate)
  FROM cd.members
       );
