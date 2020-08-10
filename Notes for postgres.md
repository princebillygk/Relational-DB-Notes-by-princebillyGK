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

```diff
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

### Right or Wrongs:

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



### Creating Views: 

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
###### Output:

###### ![Output](https://i.ibb.co/vcxTF0L/image.png) 



**We can also create views upon other views:**

```sql
CREATE VIEW max_temp_city 
AS 
  SELECT * 
  FROM   weather_with_cities 
  WHERE  temp_hi = (SELECT Max(temp_hi) 
                    FROM   weather); 
```

###### Output:

###### ![output](https://i.ibb.co/sjnhWmQ/image.png)



### Transaction: 

> **Important!**

Transaction is a way grouping of multiple statements that does a specific job. If one of the statements failed to execute of that group then none of the statements take effect at all. When the transaction is on progress all changes are invisible to other operations.  So the changes will take effect only when all operation of the transaction have successfully finished. 

A transaction begins with `BEGIN;`  and ends with `COMMIT;`  We can include as many statements as we want to include in one transaction.

```sql
BEGIN;
UPDATE accounts SET balance = balance - 5000 WHERE id = 3;
UPDATE accounts SET balance = balance + 5000 WHERE id = 4;
COMMIT;
```



### Windows Function

**Allowed in both SELECT list and ORDER BY  clause.**

A way of using aggregate functions without group by clause and without limiting results of each group to a single rows.

**OVER: ** Clause that determines windows (a set of rows),

**PARTITION BY:** Splits the result set into partitions where the result set is applied. (can be compared to group by function when using aggregate function)

Assume this query;

Select all payments of the customers with an additional column that contains the total amount of payment of that customer in each row:

Statement 1:

```sql
WITH pmt1 
     AS (SELECT customer_id, 
                Sum(amount) AS sum 
         FROM   payment 
         GROUP  BY customer_id) 
SELECT pmt2.customer_id, 
       amount, 
       sum 
FROM   payment pmt2 
       INNER JOIN pmt1 
               ON pmt1.customer_id = pmt2.customer_id 
ORDER  BY customer_id; 
```

**We can simplify this by using windows function:**

Statement 2:

```sql
SELECT customer_id, 
       amount, 
       Sum(amount) 
         OVER ( 
           partition BY customer_id) AS sum 
FROM   payment; 
```
Both results same output:

![Statement 1 & 2 ouput](https://i.ibb.co/K6sWBjj/test2.gif)

#####  Example using ORDER BY:

When `ORDER BY` is supplied then the frame consists of all rows from the start of the partition up through the current row, plus any following rows that are equal to the current row according to the `ORDER BY` clause. When `ORDER BY` is omitted the default frame consists of all rows in the partition.

Example: Select total payments with cumulative amount for each month

```sql
SELECT Sum (amount)                                   AS amount, 
       Sum (Sum(amount)) 
         OVER ( 
           ORDER BY Date_part('month', payment_date)) AS cumulitive_amount, 
       Date_part('month', payment_date)               AS month 
FROM   payment 
WHERE  Date_part('year', payment_date) = '2017' 
GROUP  BY month 
ORDER  BY month; 
```
###### Output:
###### ![output](https://i.ibb.co/rHMrMqN/image.png)



**We can also reuse the same window function behavior using `WINDOW` clause:**

The example itself is self explanatory

```sql
SELECT paragraphid, 
       wordcount, 
       (max(wordcount) OVER w - wordcount) AS deviationfromMax , 
	   (wordcount - min(wordcount) OVER w) AS deviationfromMin , 
       abs(round(avg(wordcount) OVER w) - wordcount) AS devationfromavg, 
       max(wordcount) OVER  w AS maxWordCount,
	   min(wordcount) OVER  w AS minWordCount,
       round(avg(wordcount) OVER  w) as avgWordCount
FROM   paragraph WINDOW w AS (partition BY workid) limit 10;
```
###### Output:

###### ![output](https://i.ibb.co/VCfzsb1/image.png)