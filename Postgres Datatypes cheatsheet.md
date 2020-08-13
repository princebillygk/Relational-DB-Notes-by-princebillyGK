# Numeric Types

| Name               | Storage Size | Description                     | Range                                                        |
| ------------------ | ------------ | ------------------------------- | ------------------------------------------------------------ |
| `smallint`         | 2 bytes      | small-range integer             | -32768 to +32767                                             |
| `integer`          | 4 bytes      | typical choice for integer      | -2147483648 to +2147483647                                   |
| `bigint`           | 8 bytes      | large-range integer             | -9223372036854775808 to +9223372036854775807                 |
| `numeric`          | variable     | user-specified precision, exact | up to 131072 digits before the decimal point; up to 16383 digits after the decimal point |
| `real`             | 4 bytes      | variable-precision, inexact     | 6 decimal digits precision                                   |
| `double precision` | 8 bytes      | variable-precision, inexact     | 15 decimal digits precision                                  |
| `smallserial`      | 2 bytes      | small autoincrementing integer  | 1 to 32767                                                   |
| `serial`           | 4 bytes      | autoincrementing integer        | 1 to 2147483647                                              |
| `bigserial`        | 8 bytes      | large autoincrementing integer  | 1 to 9223372036854775807                                     |



# String / Character Types

| Name         | Description                |
| ------------ | -------------------------- |
| `varchar(n)` | fixed-length, blank padded |
| `text`       | variable unlimited length  |



# Binary Data Type

| Name    | Size                                       | Description                   |
| ------- | ------------------------------------------ | ----------------------------- |
| `bytea` | 1 or 4 bytes plus the actual binary string | variable-length binary string |

# Date/ Time Types

| Name         | Description                                                  | Example                                                      |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `timestamp`  | Timestamp without timezone                                   | **1999-01-08 04:05:06**                                      |
| `timestampz` | Timestamp with timezone                                      | **January 8 04:05:06 1999 PST**\| **1999-01-08 04:05:06 -8:00** |
| `time`       | With and without timestamp                                   | without time time zone: **04:05:06.789**  with timezone **2003-04-12 04:05:06 America/New_York** |
| `date`       | Date                                                         | **1999-01-08**                                               |
| `interval`   | **Add one of these (mandatory):** `YEAR` `MONTH` `DAY` `HOUR``MINUTE` `SECOND` `YEAR TO MONTH` `DAY TO HOUR` `DAY TO MINUTE` `DAY TO SECOND` `HOUR TO MINUTE` `HOUR TO SECOND` `MINUTE TO SECOND` | **Y**	Years<br/>**M**	Months (in the date part)<br/>**W**	Weeks<br/>**D**	Days<br/>**H**	Hours<br/>**M**	Minutes (in the time part)<br/>**S**	Seconds |

# Boolean Types

| Name      | Storage Size | Description            |
| --------- | ------------ | ---------------------- |
| `boolean` | 1 byte       | state of true or false |



# Enum Types

To use `ENUM` we have to create one first:

```SQL
CREATE TYPE gender AS ENUM ('male', 'female', 'others');
```

```sql
CREATE TABLE person (
    name varchar(50),
   	gender gender			
);
```



# **UUID TYPES**

```
A0EEBC99-9C0B-4EF8-BB6D-6BB9BD380A11
{a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11}
a0eebc999c0b4ef8bb6d6bb9bd380a11
a0ee-bc99-9c0b-4ef8-bb6d-6bb9-bd38-0a11
{a0eebc99-9c0b4ef8-bb6d6bb9-bd380a11}
```



# Other Types

**Geometric Types:** https://www.postgresql.org/docs/12/datatype-geometric.html

**Network Types: **https://www.postgresql.org/docs/12/datatype-net-types.html