# SQL Cheat Sheet

Resource: [www.sqltutorial.org](https://www.sqltutorial.org/)

**SELECT**

To query data from a table, you use the SQL SELECT statement. The SELECT statement contains the syntax for selecting columns, selecting rows, grouping data, joining tables, and performing simple calculations.

```
SELECT select_list
FROM table_name;
```

**ORDER BY

To specify exactly the order of rows in the result set, you add use an ORDER BY clause in the SELECT statement.

```
SELECT 
    column1, column2
FROM
    table_name
ORDER BY column1 ASC , 
         column2 DESC;
```

**DISTINCT**

To remove duplicates from a result set, you use the DISTINCT operator in the SELECT clause.

```
SELECT DISTINCT
    column1, column2, ..
FROM
    table1;
```