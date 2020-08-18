SELECT row_number ()
                  OVER (
                 ORDER BY joindate
       ), firstname, surname
  FROM cd.members
 ORDER BY joindate;
