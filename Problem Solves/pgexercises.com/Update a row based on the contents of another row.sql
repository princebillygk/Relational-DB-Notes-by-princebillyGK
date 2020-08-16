  WITH it AS (
                SELECT membercost * 1.1 as nmc, guestcost * 1.1 as ngc
                  FROM cd.facilities
 WHERE facid        = 0
       )
UPDATE cd.facilities
   SET membercost   = (
                SELECT nmc
  FROM it
       ), guestcost = (
                SELECT ngc
  FROM IT
       )
 WHERE facid        = 1;
