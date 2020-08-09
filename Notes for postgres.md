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



## Querying: 

General wrong use of query:

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

   