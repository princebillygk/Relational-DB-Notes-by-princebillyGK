> # Get Started with PostgreSQL 
>
> **by princbillyGK**

<hr>
<!-- START doctoc -->
<!-- END doctoc -->


## Download & installation:

1. ### Download and install psql:

   (**https://www.postgresql.org/download/**)

2. ### Download and install pgAdmin: 

   (**https://www.pgadmin.org/download/**)

   

## Configuration

### First time connect to psql and configure for development linux:

Help Command

```shell
psql --help	
```

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



### Connect to psql after configuration

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



### Good Practice:

1. While writing SELECT statements for making softwares or tools for users avoid using  * (as it can be dynamic) rather specify the columns that you will only need.
2. Never use **money** type to store currency (it is left for historical reasons) neither use float or any float like data types (can give incorrect result sometime) rather use **int** or **numeric with forced 2 unit precision**.
3. Write Keywords in uppercases and names in lowercases. 



## Right or Wrongs:

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

3. We cannot use output column in `ORDER BY`  expression: 

   ```diff
   - SELECT (totalwords + totalparagraphs) AS twp, year FROM work ORDER BY (twp + year);
   + SELECT (totalwords + totalparagraphs) AS twp, year FROM work ORDER BY (totalwords+ totalparagraphs + year);
       --or
   +  SELECT * FROM (select (totalwords + totalparagraphs) as twp, year from work) t order by (twp + year);
   ```

   

## Advance Features

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
**Output:**

![Output](https://i.ibb.co/vcxTF0L/image.png) 



**We can also create views upon other views:**

```sql
CREATE VIEW max_temp_city 
AS 
  SELECT * 
  FROM   weather_with_cities 
  WHERE  temp_hi = (SELECT Max(temp_hi) 
                    FROM   weather); 
```

**Output:**

![output](https://i.ibb.co/sjnhWmQ/image.png) 



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

**OVER: ** Clause that determines windows (a set of rows) **(PARTITION BY:** Splits the result set into partitions where the result set is applied. (can be compared to group by function when using aggregate function)**,** **ORDER BY**: Set the order of virtual tables **)**

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

**Example using ORDER BY:**

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
Output:

![output](https://i.ibb.co/rHMrMqN/image.png) 

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
**Output:**

![output](https://i.ibb.co/VCfzsb1/image.png)

### Table Inheritance:

Lets assume this classes:

```typescript
class Member {
    id: number;
    readonly username: string;
    firstname: string;
    lastName: string;
    birthDay: Date;
    joinedAt: Date;
}

class Student extends Member{
    roll: number;
    class: number;
    section: string;
}

class Teacher extends Member {
    teacherId: number;
    postion: string;
    department: string;
}
```



We can implement this is in Postgres database using the inheritance feature without managing multiple tables and avoid extra efforts in writing query;

```sql
create table members (
  id BIGSERIAL primary key, 
  username varchar(50) not null unique, 
  firstname varchar(50) not null, 
  lastName varchar(50) not null, 
  birthday date not null, 
  joindate date not null default current_date
);

create table students (
  roll bigserial primary key, 
  class int not null check (
    class between 1 
    and 12
  ), 
  section varchar(1)
) inherits (members);

create table teachers (
  teacherid bigserial primary key, 
  department varchar(50) not null
) INHERITS (members);

```

**Query**: 

```sql
SELECT * FROM members; --select all members (included teachers and students);
SELECT * FROM students; --select all students;
SELECT * FROM teachers; --select all teachers;
SELECT * FROM ONLY members; --select only members (teachers and students not included)
```

**Output:**

![output](https://i.ibb.co/6X13SMP/Peek-2020-08-11-19-07.gif)



## Some Important Notes

### Constraints

##### Check Constraints: 

Example: 

```sql
/* Most simple form */
CREATE TABLE xyz (
price numeric CHECK (price > 0) 
...);

/* Specify name */
CREATE TABLE xyz (
...
price numeric CONSTRAINT positive_price CHECK (price > 0)
...);

/*In new line */
CREATE TABLE xyz (
...
CHECK (discounted_price > 0 AND price > discounted_price)
...);
```

##### Unique Constraints

##### Primary Key

##### Foreign key

```sql
--Triggers
ON DELETE RESTRICT 
/* both no action and RESTRICT prevent deletion of referenced row */
ON DELETE CASCADE 
/* deletes referencing row when the reference row is deleted */
ON DELETE SET NULL 
/* set the foreign key value to null on delete of reference row */
ON DELETE SET DEFAULT 
/*set default value on delete of reference row */

--Triggers
ON UPDATE RESTRICT 
/* both no action and RESTRICT prevent from updating of referenced row */
ON UPDATE CASCADE 
/* updates referencing row when the reference row is updated */
ON UPDATE SET NULL 
/* set the foreign key value to null on update of reference row */
ON UPDATE SET DEFAULT 
/*set default value on update of reference row */
```

**A foreign key must refer either a primary key or a unique constraint**



### Single Quote vs double quote: 

| Use of Double Quote                                          | Use of Single Quote                                          | Use of Dollar Quoted String                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Used to specify identifier. eg. Column name, table name, database name. | Used to specify string constant                              | Used to Specify string constant. Generally used for writing function definition. |
| Example: `SELECT * FROM "Tom's Table";`                      | Example: `UPDATE TABLE mytable SET firstname = 'TOM' WHERE id = 1;` | Example:  **String constant without tag =>** $$Tom's House$$ . **String constant without tag =>** $mystring$Hello 1234 ' '' \\\ $$ddfd $mystring$ ![outpput](https://i.ibb.co/bdjhJvW/image.png) |



### Generated Column

A generated column is automatically generated based on other columns values

```sql
CREATE TABLE person (
  firstname VARCHAR(50) NOT NULL, 
  lastname VARCHAR(50) NOT NULL, 
  fulllname VARCHAR(100) GENERATED ALWAYS AS (firstname || ' ' || lastname) STORED
);

```

**We cannot insert or update values into generated columns. A Generated column can only use immutable functions. A generation expression cannot reference to another generated column or system column**

Output

![output](https://i.ibb.co/WpWXgfW/image.png)



### The Returning keyword

Sometimes it is needed to know some information about most recent manipulated row. To avoid an extra query to get that information we can use `RETURNING [select_list]` with `INSERT`. `UPDATE` or `DELETE` keyword:

```sql
INSERT INTO ACTOR (first_name, last_name) VALUES ('PRINCE', 'NICHOLAS'), ('BILLY', 'VEVO')  RETURNING actor_id;
```

Output:

```
 actor_id 
----------
      203
      204
```



### `Lateral` vs non lateral sub queries

<table>
    <tr>
        <th></th>
    	<th>
        	Lateral
        </th>
    	<th>
        	Non lateral
        </th>
    </tr>
    <tr>
    	<td>
            1
        </td>
    	<td>
            Starts with <code>LATERAL</code> keyword
        </td>
        <td>
        	Doesn't starts with any specific keyword
        </td>
    </tr>
    <tr>
    	<td>2</td>
    	<td>
			Can use refrence from any other columns by preceding <code>FROM</code></code> items
    	</td>
    	<td>
           Works as a independent query. Can't use any refernce from any other <code>FROM</code> items
    	</td>
	</tr>
	<tr>
	<td>
        3
     </td>
     <td>
     	Example: <code>SELECT * FROM table1 t1, LATERAL (SELECT * FROM table2 t WHERE t1.id = t.id) t2;</code> 
         <b>Here t1.id is a referenced column from preceding <code>FROM</code> item table1 which is aliased as t1 </b>
     </td>
     <td>
         <code>SELECT * FROM fdt WHERE c1 IN (SELECT c1 FROM t2)</code>
     </td>
</tr>
</table>


### Group by `GROUPING SETS` => shorthand `ROLLUP` vs `CUBE`:

#### `ROLLUP` 

<table>
    <tr>
        <th><code>ROLLUP</code> => </th>
        <th><code>GROUPING SETS</code></th>
    </tr>
    <tr>
 	   	<td>
    		<pre>
ROLLUP ( e1, e2, e3, ... )
    		</pre>   
​   	</td>
        	   	<td>
    		<pre>
GROUPING SETS (
    ( e1, e2, e3, ... ),
    ...
    ( e1, e2 ),
    ( e1 ),
    ( )
)
    		</pre>   
​   	</td>
    </tr>
</table>
#### `CUBE`

<table>
    <tr>
        <th><code>ROLLUP</code> => </th>
        <th><code>GROUPING SETS</code></th>
    </tr>
    <tr>
 	   	<td>
    		<pre>
CUBE ( a, b, c )
    		</pre>   
   	</td>
        	   	<td>
    		<pre>
GROUPING SETS (
    ( a, b, c ),
    ( a, b    ),
    ( a,    c ),
    ( a       ),
    (    b, c ),
    (    b    ),
    (       c ),
    (         )
)
    		</pre>   
   	</td>
    </tr>
</table>



### Combining result sets (`UNION`, `INTERSECT`, `EXCEPT`)

|  `UNION`  | `INTERSECT` | `EXCEPT`  |
| :-------: | :---------: | :-------: |
| **A ∪ B** |  **A ∩ B**  | **A - B** |

**Duplicates are removed automatically if `UNION ALL`, `INTERSECT ALL` `EXCEPT ALL`  is not used.**

### Use of `VALUES`

to generate constant table: 

```sql
SELECT * FROM (VALUES ('pi', '3.1416'), ('g', '9.8')) AS t (constant,value);
```

**Output**:

```sql
 constant | value  
----------+--------
 pi       | 3.1416
 g        | 9.8

```

### Use of `WITH`

**To much to keep in mind**

better go here:  https://www.postgresql.org/docs/12/queries-with.html



### `ILIKE` vs `LIKE` 

`ILIKE` is not case sensitive whereas `LIKE` is case sensitive matching operator

### `SIMILAR TO` reg_exp

Here is my notes on reg_exp

https://gist.github.com/princebillyGK/c4b3f55c858a5c0d17f9049b6095fb8c



### `BETWEEN SYMMETRIC x AND Y` vs `BETWEEN x AND y`

`BETWEEN X AND Y` here x is always less than or equal to y.     **x < y** or **x = y**

**Example:** `BETWEEN 5 and 10` `BETWEEN 5 and 5`

`BETWEEN x AND y` here x and y values are not depended to each other. **x < y** or **x > y** or **x = y**

**Example:** `BETWEEN 5 and 10` `BETWEEN 5 and 5``BETWEEN 10 and 5`

### `<>` or `!=` vs`IS DISTINCT FROM`  and `=` vs `IS NOT DISTINCT FROM`



```sql
/* <> OR != */
SELECT null <> null; --returns null
SELECT 5 != null; --returns null

/* =  */
SELECT null = null; --returns null
SELECT 5 = null; --returns null

/* DISTINCT */
SELECT 4 IS DISTINCT FROM null; --returns true
SELECT null IS DISTINCT FROM null; --return false

/* IS NO DISTINCT */
SELECT 4 IS NOT DISTINCT FROM null; --returns false
SELECT null IS NOT DISTINCT FROM null; --return true
```

### CASE Syntax

```plsql
CASE WHEN condition THEN result
     [WHEN ...]
     [ELSE result]
END
```

### `COALESCE` Syntax

```sql
COALESCE ('if it is not null then print it other wise next parameter', 'if it is not null then print it other wise check next parmeter', ...);
```

### NULLIF

```
NULLIF(col, 'if col matched with this value then return null')
```

### `GREATEST` and `LEAST`

```sql
GREATEST(value [, ...]) --finds the greatest value	
LEAST(value [, ...]) --finds the least value
```



# Important functions and operators

### Mathematical operator

|       |                                                  |             |       |
| ----- | ------------------------------------------------ | ----------- | ----- |
| `+`   | addition                                         | `2 + 3`     | `5`   |
| `-`   | subtraction                                      | `2 - 3`     | `-1`  |
| `*`   | multiplication                                   | `2 * 3`     | `6`   |
| `/`   | division (integer division truncates the result) | `4 / 2`     | `2`   |
| `%`   | modulo (remainder)                               | `5 % 4`     | `1`   |
| `^`   | exponentiation (associates left to right)        | `2.0 ^ 3.0` | `8`   |
| `|/`  | square root                                      | `|/ 25.0`   | `5`   |
| `||/` | cube root                                        | `||/ 27.0`  | `3`   |
| `!`   | factorial                                        | `5 !`       | `120` |
| `!!`  | factorial (prefix operator)                      | `!! 5`      | `120` |
| `@`   | absolute value                                   | `@ -5.0`    | `5`   |
| `&`   | bitwise AND                                      | `91 & 15`   | `11`  |
| `|`   | bitwise OR                                       | `32 | 3`    | `35`  |
| `#`   | bitwise XOR                                      | `17 # 5`    | `20`  |
| `~`   | bitwise NOT                                      | `~1`        | `-2`  |
| `<<`  | bitwise shift left                               | `1 << 4`    | `16`  |
| `>>`  | bitwise shift right                              | `8 >> 2`    | `2`   |

### String Operators

| Operator | Description                                    | Example              | Result       |
| -------- | ---------------------------------------------- | -------------------- | ------------ |
| \|\|     | String concatenation                           | `'Post' || 'greSQL'` | `PostgreSQL` |
|          | String concatenation with one non-string input | `'Value: ' || 42`    | `Value: 42`  |

### Window Functions

| Function              | Return Type              | Description                                                  |
| --------------------- | ------------------------ | ------------------------------------------------------------ |
| `row_number()`        | `bigint`                 | number of the current row within its partition, counting from 1 |
| `rank()`              | `bigint`                 | rank of the current row with gaps; same as `row_number` of its first peer |
| `dense_rank()`        | `bigint`                 | rank of the current row without gaps; this function counts peer groups |
| `percent_rank()`      | `double precision`       | relative rank of the current row: (`rank` - 1) / (total partition rows - 1) |
| `cume_dist()`         | `double precision`       | cumulative distribution: (number of partition rows preceding or peer with current row) / total partition rows |
| `first_value(column)` | `same type as *`value`*` | returns *`value`* evaluated at the row that is the first row of the window frame |
| `last_value(column)`  | `same type as *`value`*` | returns *`value`* evaluated at the row that is the last row of the window frame |
| `nth_value(col, n)`   | `same type as *`value`*` | returns *`value`* evaluated at the row that is the *`nth`* row of the window frame (counting from 1); null if no such r |

### Sub query Expressions

```sql
EXISTS (subquery) --returns true if any element exists
expression IN (subquery) --returns true if expresion value exists in subquery
expression NOT IN (subquery) --returns true if expresion value not exists in subquery
expression operator ANY (subquery) / 
expression operator SOME (subquery) --returns any operation returns true
row_constructor operator ALL (subquery) -- returns false if any operation returns false
```