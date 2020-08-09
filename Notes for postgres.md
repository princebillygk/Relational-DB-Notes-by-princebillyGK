# Get Started with PostgreSQl 

###### by princbillyGK

### Download & installation:

1. Download and install psql:

   (**https://www.postgresql.org/download/**)

2. Download and install pgAdmin: 

   (**https://www.pgadmin.org/download/**)

   

### Help Command

```shell
psql --help #for help
```



### Configuration

#### First time connect to psql and configure for development linux:

Open the terminal:

```shell
sudo su postgres
psql
```

```sql
\password --to change psql postgres user password
```

Then enter your new password twice and type: 

```sql
\q		--quit from psql
```

```shell
cd /etc/postgresql/
ls #check your versions
cd 12 #into the folder 12 for me
vim pg_hba.conf

```

Change from peer to md5:

```conf
- local   all             all                                     peer
+ local   all             all                                     md5
```

Restart psql:

```shell
sudo service postgresql restart
```

<kbd>CTRL</kbd>+<KBD>d</kbd>  to go back to normal mode.



#### Connect to psql after configuration

```shell
psql -U postgres
```



##### How to write comments: 

Single line comments: 

```sql
--this is a single line comment
```

Multi line comments:

```sql
/* This is a 
multi line
comment */
```

##### Some helpful command to get started: 

```sql
\? --show psql commands
\h --show sql commands
\q --quit terminal
```



## Get started

Create and drop database

```sql
CREATE DATABSE mydb; --creates a new database
DROP DATABASE mydb; --removes a database
```

Connect to database directly from terminal

```shell
psql dbname
```

Switch database inside psql promt:

```sql
\c dbname
```



## Good Practice:

1. Never use **money** type to store currency (it is left for historical reasons) neither use float or any float like data types (can give incorrect result sometime) rather use **int** or **numeric with forced 2 unit precision**.

## Querying: 

#### Right or Wrongs:

1. Aggregate function are not allowed in where clause:

```diff
- SELECT * FROM weather WHERE temp_hi = max(temp_hi); --wrong
+ SELECT * FROM weather where temp_hi = (SELECT max(temp_hi) FROM weather); 
```

2. You cannot use HAVING keyword without GROUP BY.

   Difference between WHERE and HAVING keyword:

   | Where                                                        | Having                                                       |
   | ------------------------------------------------------------ | ------------------------------------------------------------ |
   | **`WHERE` selects input rows before groups and aggregates are computed** | **`HAVING` selects group rows after groups and aggregates are computed** |
   | `WHERE` clause must not contain aggregate functions          | `HAVING` clause contains aggregate functions most of the time |
   | You can use `WHERE` without group by clause.                 | You cannot use `HAVING` without group by clause.             |



#### Creating Views: 

We can create view to encapsulate details of a query. 

```sql
CREATE VIEW weather_with_cities 
AS 
  SELECT city, 
         temp_lo, 
         temp_hi, 
         prcp, 
         location date 
  FROM   weather, 
         cities 
  WHERE  city = NAME; 
```

```sql
SELECT * FROM weather_with_cities;
```

> Output:
>
> ```powershell
>      city      | temp_lo | temp_hi | prcp |    date    
> ---------------+---------+---------+------+------------
>  San Francisco |      46 |      50 | 0.25 | 1994-11-27
>  San Francisco |      41 |      55 |    0 | 1994-11-29
>  San Francisco |      41 |      55 |    0 | 1994-11-29
> ```

We can also create views upon other views:

```sql
CREATE VIEW max_temp_city 
AS 
  SELECT * 
  FROM   weather_with_cities 
  WHERE  temp_hi = (SELECT Max(temp_hi) 
                    FROM   weather); 
```

> Output:
>
> ```powershell
>      city      | temp_lo | temp_hi | prcp |    date    | location  
> ---------------+---------+---------+------+------------+-----------
>  San Francisco |      41 |      55 |    0 | 1994-11-29 | (-194,53)
> 
> ```



### Transaction: 

> **Important!**

Transaction is a way grouping of multiple statements that does a specific job. If one of the statements failed to execute of that group then none of the statements take effect at all. When the transaction is on progress all changes are invisible to other operations.  So the changes will take effect only when all operation of the transaction have successfully finished. 

A transaction begins with `BEGIN;`  and ends with `COMMIT;`  We can include as many statements as we want to include in transaction.

```sql
BEGIN;
UPDATE accounts SET balance = balance - 5000 WHERE id = 3;
UPDATE accounts SET balance = balance + 5000 WHERE id = 4;
COMMIT;
```

