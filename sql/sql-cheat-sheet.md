# SQL Cheat Sheet

Kaynak: [www.sqltutorial.org](https://www.sqltutorial.org/)

- **SELECT**

Tablodan data sorgulamak için kullanılır. Sütun veya satırları seçebilir, sorgulanan dataları gruplayabilir, tabloları birleştirebilir ve basit hesaplamalar yapabilir.

```
SELECT select_list
FROM table_name;
```
---
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
---
- **DISTINCT**

Sorguda tekrar eden değerleri benzersiz hale getirir.

```
SELECT DISTINCT
    column1, column2, ...
FROM
    table1;
```
---
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
---
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
---
- **INNER JOIN**

İki veya daha fazla tabloyu kesişim kümesine göre bağlar. Örneğin A(1,2,3,4) kümesiyle B(3,4,5,6) kümesi **INNER JOIN** ile bağlandığında (3,4) kümesi oluşur. Kümeler arasındaki değerler **ON** kelimesiyle ilişkilendirilir.

![INNER JOIN](https://cdn.sqltutorial.org/wp-content/uploads/2016/03/SQL-INNER-JOIN.png)

```
SELECT
    A.n
FROM A
INNER JOIN B ON B.n = A.n;
```
---