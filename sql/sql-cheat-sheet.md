# SQL Cheat Sheet

Resource: [www.sqltutorial.org](https://www.sqltutorial.org/)

- **SELECT**

Tablodan data sorgulamak için kullanılır. Sütun veya satırları seçebilir, sorgulanan dataları gruplayabilir, tabloları birleştirebilir ve basit hesaplamalar yapabilir.

```
SELECT select_list
FROM table_name;
```

- **ORDER BY**

Sorgulanan sonuca göre artan veya azalan olarak satırları sıralar.

```
SELECT 
    column1, column2
FROM
    table_name
ORDER BY column1 ASC , 
         column2 DESC;
```

- **DISTINCT**

Sorguda tekrar eden değerleri benzersiz hale getirir.

```
SELECT DISTINCT
    column1, column2, ...
FROM
    table1;
```

- **WHERE**

Belirli satırları sorgulamak için kullanılır.

```
SELECT 
    column1, column2, ...
FROM
    table
WHERE
    condition;
```

- **LIMIT**

Belirli sayıda satır almak için LIMIT, kaçıncı satırdan itibaren alınmak istenirse OFFSET kullanılır.

```
SELECT 
    column_list
FROM
    table1
ORDER BY column_list
LIMIT row_count OFFSET offset;
```