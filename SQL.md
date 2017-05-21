# SQL 이란. 

- Structured Query Language
- 관계형 데이터베이스 관리 시스템(RDBMS : Relational Database Management System)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다.
- ANSI (American National Standards Institute) 표준이다.
- 여러 데이터베이스에 접근할 수 있다.
- server-side scripting language


### table

- row(가로줄)와 column(세로)으로 이루어짐
- 1개의 row가 1개의 record를 담고 있음

### SQL Statement

- 데이터를 가공하는 명령어

예: `SELECT * FROM Customers;`
--> Customers 테이블의 데이터를 다 가지고 온다.

- 대소문자를 가리지 않음
- 명령어 마지막에 `;`

##### 자주 쓰는 SQL 명령어

|명령어|설명|
|---|---|
|SELECT|데이터베이스에서 데이터를 추출|
|UPDATE|데이터베이스의 데이터를 업데이트|
|DELETE|데이터베이스의 데이터를 삭제|
|INSERT INTO|데이터베이스에 데이터를 추가|
|CREAT DATABASE|데이터베이스를 생성|
|ALTER DATABASE|데이터베이스의 구조를 수정|
|CREATE TABLE|데이터베이스 안에 테이블을 생성|
|ALTER TABLE|테이블의 구조를 바꿈|
|DROP TABLE|데이터베이스의 테이블을 삭제|
|CREATE INDEX|데이터의 인덱스 생성|
|DROP INDEX|데이터의 인덱스 삭제|

### 데이터 가져오기 statement

#### SELECT

- 데이터를 가지고 온다
- 가지고온 데이터는 ASP나 PHP로 가공할 수 있다.

```sql
SELECT [column_name], [column_name], ...
FROM [table_name];
```

```sql
SELECT * FROM [table_name];
```


#### SELECT DISTINCT

- 데이터를 가지고 오면서 중복된 값을 없애준다.

```sql
SELECT DISTINCT [column_name] FROM [table_name];
```

#### WHERE 구문

- 특정한 조건에 맞는 데이터만 가지고 온다.
- 조건이 텍스트일 경우 `'``'`로 감싸준다. (대부분은 큰따옴표도 가능)
- 조건이 숫자일 경우에는 필요없다.

```sql
SELECT [column_name], [column_name], ...
FROM [table_name]
WHERE [조건];
```

|조건연산자|설명|
|---|---|
|=|같다|
|<> or !=|다르다|
|>|~보다 크다|
|<|~보다 작다|
|>=|이상|
|<=|이하|
|BETWEEN|두 값의 사이|
|LIKE|패턴 검색|
|IN|일부 조건으로 검색|

#### HAVING 구문

- 집계함수와 GROUP BY와 같이 사용된다. (집계함수에 WHERE는 함께 사용할 수 없다.)
- 특정한 조건에 맞는 데이터만 가지고 온다.

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5
ORDER BY COUNT(CustomerID) DESC;

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM (Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 10;
```

#### AND, OR, NOT

- a AND b : a 이면서 b인 데이터
- a OR b : a 이거나 b인 데이터
- NOT a : a가 아닌 데이터

#### ORDER BY

- 데이터를 가지고 올때 데이터의 순서를 정해준다.
- ASC : 내림차순 (기본값)
- DESC : 오름차순

```sql
SELECT [column_name], [column_name], ...
FROM [table_name]
ORDER BY [column_name], [column_name], ... ASC or DESC;
```

#### GROUP BY

- COUNT, MAX, MIN, SUM, AVG와 함께 사용하여 집계 범위를 정한다.

```sql
SELECT column_name(s), 집계함수(column_name)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);

SELECT Shippers.ShipperName, 
COUNT(Orders.OrderID) AS NumberOfOrders 
FROM Orders
LEFT JOIN Shippers 
ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName;
```

#### SELECT INTO

- 하나의 테이블로부터 데이터를 복사하여 새로운 테이블로 옮긴다.
- 새로운 테이블을 생성함.

```sql
# 모든 데이터
SELECT *
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;

# 일부 columns
SELECT column1, column2, column3, ...
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;

# Customers 테이블을 복사하여 백업을 만든다.
SELECT * INTO CustomersBackup2017
FROM Customers;

# Backup.mdb라는 데이터베이스 안에 Customers 테이블을 복사하여 백업을 만든다.
SELECT * INTO CustomersBackup2017 IN 'Backup.mdb'
FROM Customers;

# 기존 테이블과 함께 조작
SELECT Customers.CustomerName, Orders.OrderID
INTO CustomersOrderBackup2017
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

# 기존 테이블의 구조만 복사하여 새로운 테이블을 만든다. (데이터는 가지고 오지 않음)
SELECT * INTO newtable
FROM oldtable
WHERE 1 = 0;
```

#### INSERT INTO SELECT

- 하나의 테이블로부터 데이터를 가지고 와서 이미 존재하는 테이블에 데이터를 추가한다.
- 기존 데이터들에 영향을 주지 않는다.

```sql
# table2에서 모든 데이터를 가지고 와서 table1에 추가해준다.
INSERT INTO table2
SELECT * FROM table1
WHERE condition;

# table2에서 특정 column의 데이터를 가지고 와서 table1에 추가해준다.
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;

# Country의 값이 Germany인 데이터
INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM Suppliers
WHERE Country='Germany';
```

### 데이터 추가, 수정

#### INSERT INTO

- 데이터 추가
- 데이터를 지정해주지 않은 column에는 null 값이 들어간다.

```sql
# 테이블에 데이터(value)를 컬럼 순서대로 넣어준다.
INSERT INTO tablename
VALUES (value1, value2, ...);

# 테이블에 데이터(value)를 언급된 컬럼 순서대로 넣어준다.
INSERT INTO tablename (column1, column2, ...)
VALUES (value1, value2, ...);

```

#### NULL 값

- 필드에 데이터가 없음 (비어있음)
- 0이 아니다. 0과 비교 불가능.

```sql
# 값이 없는 데이터를 불러온다.
SELECT column_names
FROM table_name
WHERE column_name IS NULL;

# 값이 있는 데이터를 불러온다.
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```

#### UPDATE 

- 레코드를 수정한다.
- **WHERE를 사용하지 않으면 해당 테이블의 전체 레코드가 변경되므로 주의!!!**

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

```sql
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;
```

#### DELETE

- 레코드 삭제
- **WHERE를 사용하지 않으면 해당 테이블의 전체 레코드가 삭제되므로 주의!!!**

```sql
DELETE FROM table_name
WHERE condition;
```

```sql
DELETE FROM Customers
WHERE CustomerName='Alfreds Futterkiste'
```

- Mysql 등의 경우, `TRUNCATE TABLE table_name;`으로 테이블 전체 데이터 삭제 가능. 테이블 자체를 날리고 다시 만드는 것이기 때문에 속도가 빠르다.


#### SELECT TOP 구문

- 가져오는 데이터의 수를 제한한다.
- 데이터가 많을때 유용하다.

```sql
# SQL Server
SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;

# Mysql
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;

# Oracle
SELECT column_name(s)
FROM table_name
WHERE ROWNUM <= number;
```

```sql
SELECT TOP 3 * FROM Customers;

SELECT TOP 50 PERCENT 20 * FROM Customers;
```


### 내장함수

#### MIN() MAX()

- SELECT로 선택된 데이터의 가장 작은 값 또는 가장 큰 값을 가지고 온다.

```sql
SELECT MIN(column_name)
FROM table_name
WHERE condition;

SELECT MAX(column_name)
FROM table_name
WHERE condition;
```

#### COUNT(), AVG(), SUM()

- COUNT() 선택된 데이터의 개수를 반환한다.
- AVG() 선택된 데이터의 평균을 반환한다.
- SUM() 선택된 데이터의 합을 반환한다.

```sql
# COUNT()
SELECT COUNT(column_name)
FROM table_name
WHERE condition;

SELECT COUNT(ProductID)
FROM Products;

# AVG()
SELECT AVG(column_name)
FROM table_name
WHERE condition;

SELECT AVG(Price)
FROM Products;

# SUM()
SELECT SUM(column_name)
FROM table_name
WHERE condition;

SELECT SUM(Quantity)
FROM OrderDetails;
```

#### LEN()

- 특정 column의 텍스트 길이

```sql
SELECT LEN(column_name) FROM table_name;

SELECT CustomerName, LEN(Address) AS LenthOfAddress
FROM Customers;
```

#### ISNULL(), NVL(), IFNULL(), COALESCE()

```sql
SELECT ProductName,UnitPrice*(UnitsInStock+UnitsOnOrder)
FROM Products

# UnitsOnOrder 컬럼 값이 null이면 0으로 대체하여 계산
# MS Access : ISNULL()
SELECT ProductName,UnitPrice*(UnitsInStock+IIF(ISNULL(UnitsOnOrder),0,UnitsOnOrder))
FROM Products

# SQL Server : ISNULL()
SELECT ProductName,UnitPrice*(UnitsInStock+ISNULL(UnitsOnOrder,0))
FROM Products

# Oracle : NVL()
SELECT ProductName,UnitPrice*(UnitsInStock+NVL(UnitsOnOrder,0))
FROM Products

# MySQL : IFNULL(), COALESCE()
SELECT ProductName,UnitPrice*(UnitsInStock+IFNULL(UnitsOnOrder,0))
FROM Products

SELECT ProductName,UnitPrice*(UnitsInStock+COALESCE(UnitsOnOrder,0))
FROM Products
```

### Operator

#### LIKE / NOT LIKE

- WHERE 이하에 사용하여 가져올 데이터의 패턴을 정해준다.
- Wildcard 참고

```sql
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;

# Customers 테이블에서 CustomerNAme이 a로 시작되는 모든 데이터
SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';

# Customers 테이블에서 Country에 land가 포함되지 않은 모든 데이터
SELECT * FROM Customers
WHERE Counrty NOT LIKE '%land%';
```

##### Wildcard

- LIKE와 함께 사용하여 패턴을 정의한다.

|사용 예|결과|
|---|---|
|LIKE 'a%'|a로 시작하는 값|
|LIKE '%a'|a로 끝나는 값|
|LIKE '%or%'|or이 포함된 값|
|LIKE '\_r%'|두번때 글자가 r인 값|
|LIKE 'a\_%\_%'|a로 시작하면서 최소 3글자 이상인 값|
|LIKE 'a%o'|a로 시작해서 o로 끝나는 값|
|LIKE '[a-c]%'|a, b, c로 시작되는 모든 값|
|LIKE '[rfg]%'|r, f, g로 시작되는 모든 값|

#### IN

- WHERE 이하에 사용하여 IN 이하에 언급된 값들을 가지고 온다.

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);

SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT STATEMENT);

# Customers 테이블에서 Country가 'Germany'이거나 'France'이거나 'UK'인 모든 데이터
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');

# Custmers 테이블에서 Suppliers 테이블의 Country 값들과 같은 값을 가진 모든 데이터
SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);
```

#### BETWEEN

- WHERE 이하에 사용하여 가지고 올 값의 범위를 정해준다.

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;

# Products 테이블에서 Price가 10에서 20사이인 모든 데이터
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;

# Products 테이블에서 Price가 10에서 20사이가 아닌 모든 데이터
SELECT * FROM Products
WHERE Price NOTBETWEEN 10 AND 20;

# Products 테이블에서 Price가 10에서 20사이인 데이터 중, CategoryID가 1 또는 2 또는 3인 모든 데이터
SELECT * FROM Products
WHERE (Price BETWEEN 10 AND 20)
AND NOT CategoryID IN (1,2,3);

# Products 테이블에서 ProductName을 내림차순 정렬했을때 'Carnarvon Tigers'와 'Mozzarella di Giovanni' 사이의 모든 데이터
SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;
```

#### ANY, ALL ??

- WHERE 이하 HAVING 이하에 사용한다.
- ANY : 조건에 맞는 데이터가 하나라도 있을때 True를 리턴
- ALL : 모든 데이터가 조건에 맞을때 True를 리턴 

```sql
# OrderDetails.Quantity가 10인 데이터가 1개라도 있으면 True를 반환하여 Quantity가 10인 OrderDetails.ProductID와 같은 ProductID를 가진 Products.ProductName을 보여준다.
SELECT ProductName
FROM Products
WHERE ProductID = ANY (SELECT ProductID FROM OrderDetails WHERE Quantity = 10);

# 모든 OrderDetails.Quantity 데이터가 10이면 True를 반환하여 Quantity가 10인 OrderDetails.ProductID와 같은 ProductID를 가진 Products.ProductName을 보여준다.
SELECT ProductName
FROM Products
WHERE ProductID = ALL (SELECT ProductID FROM OrderDetails WHERE Quantity = 10);
```

#### Aliases

- 테이블이나 컬럼의 별명을 부를때 쓴다.
- 테이블 이나 컬럼의 이름이 길거나, 여러개를 선택해야 할때..
- 가지고온 데이터에도 별명이 계속 사용된다.
- 여러개의 이름을 묶을때도 사용한다.
- 가독성을 높이기 위해 사용하기도 한다.

```sql
# Column에 이름 붙이기
SELECT column_name AS alias_name
FROM table_name;

# Table에 이름 붙이기
SELECT column_name(s)
FROM table_name AS alias_name;

# column 이름을 줄인다.
SELECT CustomerID as ID, CustomerName AS Customer
FROM Customers

# 여러개의 column을 합쳐 준다. (별명에 공백이 있으면 "" 나 [] 로 묶어준다
SELECT CustomerName AS Customer, ContactName AS [Contact Person]
FROM Customers;

# 여러개의 column을 합쳐 준다.
SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country AS Address
FROM Customers;
```

### JOIN

- 2개 이상의 테이블에서 데이터를 합칠때 사용한다.
- INNER JOIN
- outter join : LEFT JOIN, RIGHT JOIN, FULL JOIN

```sql
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers 
ON Orders.CustomerID=Customers.CustomerID;
```

#### INNER JOIN

- 교집합
- 일치하는 컬럼이름 기준으로 데이터를 가지고 온다.

```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2 ON table1.column_name = table2.column_name;

SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers 
ON Orders.CustomerID = Customers.CustomerID;
```

#### LEFT JOIN

- table1에 해당하는 테이블의 모든 데이터와 조건에 맞는 table2 데이터를 가지고 온다.

```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2 
ON table1.column_name = table2.column_name;

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders 
ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;
```

#### RIGHT JOIN

- table2에 해당하는 테이블의 모든 데이터와 조건에 맞는 table1 데이터를 가지고 온다.

```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2 
ON table1.column_name = table2.column_name;

SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees 
ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;
```

#### FULL OUTER JOIN

- table1과 table2의 데이터를 모두 가지고 오면서 조건에 맞는 값은 중복되지 않게 가지고 온다.
- MySql은 지원하지 않는다. (LEFT JOIN과 RIGHT JOIN을 UNION해서 해결)

```sql
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2 ON table1.column_name = table2.column_name;

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders 
ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName;
```

#### Self JOIN

- 같은 table 내에서 JOIN

```sql
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;

SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City 
ORDER BY A.City;
```

#### UNION

- 각각의 SELECT가 가지고 온 데이터들을 합쳐준다.
- column의 수가 같아야 한다.
- 데이터 타입이 유사해야된다.
- 각각의 SELECT는 정렬 순서가 같아야 한다.
- 같은 데이터는 중복되게 가지고 오지 않는다.

```sql
# UNION
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;

# UNION ALL - 중복된 데이터도 다 가지고 온다.
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;

# 사용 예
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;
```

### ..

#### EXISTS

- 가지고 올 데이터가 존재하는지 테스트 하기 위해 사용한다.
- 데이터가 있으면 True를 반환한다.

```sql
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
```

#### 주석 --

- \-\- : 주석이 1줄일때
- /\* ... \*/ : 여러줄 주석일때

```sql
--Select all:
SELECT * FROM Customers;

/*Select all the columns
of all the records
in the Customers table:*/
SELECT * FROM Customers;

SELECT * FROM Customers WHERE (CustomerName LIKE 'L%'
OR CustomerName LIKE 'R%' /*OR CustomerName LIKE 'S%'
OR CustomerName LIKE 'T%'*/ OR CustomerName LIKE 'W%')
AND Country='USA'
ORDER BY CustomerName;
```


### DATABASE

#### CREATE DATABASE

- 데이터베이스를 생성한다.
- 왠만해서는 해볼 일이 없다.

```sql
CREATE DATABASE databasename;
```

#### DROP DATABASE

- 데이터베이스를 삭제한다.

```sql
DROP DATABASE databasename;
```

#### CREATE TABLE

- 데이터베이스 내에 테이블을 생성한다.
- 테이블 이름이 꼭 필요하다.
- 테이블 내에 column들을 만들어준다. 데이터타입 (컬럼의 데이터 사이즈를 지정)

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);

CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255) 
);
```

#### DROP TABLE

- 테이블을 삭제한다.


```sql
DROP TABLE table_name;

DROP TABLE Shippers;

# 테이블을 완전히 삭제하고 같은 구조로 다시 만든다.
TRUNCATE TABLE table_name;
```

#### ALTER TABLE

- 이미 만들어진 테이블에서 데이터를 추가하거나, 삭제하거나 변경할때 사용

```sql
-- add column
ALTER TABLE table_name
ADD column_name datatype;

-- drop column
ALTER TABLE table_name
DROP COLUMN column_name;

-- alter/modify column
-- SQL Server / MS Access
ALTER TABLE table_name
ALTER COLUMN column_name datatype;

-- My SQL / Oracle (prior version 10G)
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;

-- Oracle 10G and later
ALTER TABLE table_name
MODIFY column_name datatype;
```

### Constraints

- 컬럼에 유일한 값을 입력한다.

```sql
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
    ....
);
```

#### NOT NULL 

- Ensures that a column cannot have a NULL value
- 비어있는 경우를 허용하지 않는다.
- INSERT INTO로 데이터를 입력할때 NOT NULL이 설정된 필드 데이터가 비어있으면 에러가 발생한다.

```sql
# ID, LastName, FirstName 필드가 비어있는 경우를 허용하지 않음.
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Age int
);
```

#### UNIQUE 

- Ensures that all values in a column are different
- 유일한 값을 갖게 한다.
- 1 테이블 내에 여러개의 유니크 값을 가질 수 있다.
- 하나 이상의 컬럼에 유니크를 지정할 수 있다.

```sql
# 1개의 컬럼에 유니크를 지정할 경우
# SQL Server / Oracle / MS Access
CREATE TABLE Persons (
    ID int NOT NULL UNIQUE,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

# MySQL
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    UNIQUE (ID)
);

# 여러 컬럼에 유니크를 지정할 경우
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT UC_Person UNIQUE (ID,LastName)
);

# 만들어진 테이블의 1개의 칼럼에 유니크를 지정할 경우
ALTER TABLE Persons
ADD UNIQUE (ID);

# 만들어진 테이블의 여러개의 칼럼에 유니크를 지정할 경우
ALTER TABLE Persons
ADD CONSTRAINT UC_Person UNIQUE (ID,LastName);

# 유니크 설정을 drop할 경우
# MySQL
ALTER TABLE Persons
DROP INDEX UC_Person;

# SQL Server / Oracle / MS Access
ALTER TABLE Persons
DROP CONSTRAINT UC_Person;
```

#### PRIMARY KEY 

- A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
- null 값을 가질 수 없다.
- table당 PK는 1개

```sql
# MySQL
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);

# SQL Server / Oracle / MS Access
CREATE TABLE Persons (
    ID int NOT NULL PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

# 여러개의 컬럼에 PK 설정을 할 경우
# PK는 하나(PK_Person), PK 값은 ID, LastName에 입력된다.
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT PK_Person PRIMARY KEY (ID,LastName)
);

# 이미 만들어진 테이블에 PK 설정을 할 경우
# 이미 PK가 지정된 테이블일 겨우 적용되지 않음.
# NULL 값이 들어있는 컬럼에 PK를 지정해야할 경우, NULL 값을 지우고 지정해야함.
ALTER TABLE Persons
ADD PRIMARY KEY (ID);

# PK 설정 해제
# MySQL
ALTER TABLE Persons
DROP PRIMARY KEY;

# SQL Server / Oracle / MS Access
ALTER TABLE Persons
DROP CONSTRAINT PK_Person;
```

#### FOREIGN KEY 

- Uniquely identifies a row/record in another table
- 외래키, 다른 데이터베이스와의 연결을 위한 키
- 다른 테이터베이스의 PK와 연결됨

```sql
# Persons.PersonID의 값을 참조하여 FK 설정
# MySQL
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);

# SQL Server / Oracle / MS Access
CREATE TABLE Orders (
    OrderID int NOT NULL PRIMARY KEY,
    OrderNumber int NOT NULL,
    PersonID int FOREIGN KEY REFERENCES Persons(PersonID)
);

# FK에 이름을 부여할 경우
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    CONSTRAINT FK_PersonOrder FOREIGN KEY (PersonID)
    REFERENCES Persons(PersonID)
);

# 이미 만들어진 테이블에 FK 설정을 할 경우
ALTER TABLE Orders
ADD FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);

# 이미 만들어진 테이블에 FK에 이름을 붙여 설정할 경우
ALTER TABLE Orders
ADD CONSTRAINT FK_PersonOrder
FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);

# FK 설정 해제
# MySQL
ALTER TABLE Orders
DROP FOREIGN KEY FK_PersonOrder;

# SQL Server / Oracle / MS Access
ALTER TABLE Orders
DROP CONSTRAINT FK_PersonOrder;
```

#### CHECK 

- Ensures that all values in a column satisfies a specific condition
- 특정 컬럼에 입력되는 데이터의 범위를 한정한다.
- 데이터 입력 시 설정된 범위에 맞지 않을 경우 에러가 발생

```sql
# Persons.Age 값은 18보다 커야한다.
# MySQL
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);

# SQL Server / Oracle / MS Access
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int CHECK (Age>=18)
);

# 여러개의 조건으로 제한. Persons.Age가 18이상, City가 Sandnes이어야 한다.
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255),
    CONSTRAINT CHK_Person CHECK (Age>=18 AND City='Sandnes')
);

# 이미 만들어진 테이블의 컬럼에 데이터 범위를 제한할 경우
ALTER TABLE Persons
ADD CHECK (Age>=18);

# 이미 만들어진 테이블에 데이터 범위 제한을 이름을 붙여 설정할 경우
ALTER TABLE Persons
ADD CONSTRAINT CHK_PersonAge CHECK (Age>=18 AND City='Sandnes');

# 제한 해제
# MySQL
ALTER TABLE Persons
DROP CHECK CHK_PersonAge;

# SQL Server / Oracle / MS Access
ALTER TABLE Persons
DROP CONSTRAINT CHK_PersonAge;
```

#### DEFAULT 

- Sets a default value for a column when no value is specified
- 특정 컬럼에 사용자의 입력이 없을 경우 자동으로 입력될 값을 정해준다.
- 시스템값을 자동으로 입력되게 설정할 수 있다.

```sql
# Persons.City에 값이 없을 경우 자동으로 'Sandnes'가 입력된다.
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255) DEFAULT 'Sandnes'
);

# 시스템값을 자동으로 입력할 수 있다. (GETDATE() : 날짜 입력)
CREATE TABLE Orders (
    ID int NOT NULL,
    OrderNumber int NOT NULL,
    OrderDate date DEFAULT GETDATE()
);

# 이미 만들어진 테이블에 설정
# MySQL
ALTER TABLE Persons
ALTER City SET DEFAULT 'Sandnes';

# SQL Server / MS Access
ALTER TABLE Persons
ALTER COLUMN City SET DEFAULT 'Sandnes';

# Oracle
ALTER TABLE Persons
MODIFY City DEFAULT 'Sandnes';

# 설정 해제
# MySQL
ALTER TABLE Persons
ALTER City DROP DEFAULT;

# SQL Server / Oracle / MS Access
ALTER TABLE Persons
ALTER COLUMN City DROP DEFAULT;
```

#### INDEX 
- Use to create and retrieve data from the database very quickly
- 검색이 잦은 컬럼에 인덱스를 부여하면 속도가 빨라진다.
- 업데이트가 잦은 컬럼의 경우에는 효율적이지 않다.
- 중복값이 허용된다. (유니크 인덱스일경우 중복값이 허용되지 않음)

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);

# Unique Index
CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);

# Persons.LastName 의 인덱스를 idx_lastname으로 생성한다.
CREATE INDEX idx_lastname
ON Persons (LastName);

# Persons.LastName과 FirstName의 인덱스를 idx_pnname으로 생성한다.
CREATE INDEX idx_pname
ON Persons (LastName, FirstName);

# 인덱스 삭제
# MS Access
DROP INDEX index_name ON table_name;

# SQL Server
DROP INDEX table_name.index_name;

# DB2/Oracle
DROP INDEX index_name;

# MySQL
ALTER TABLE table_name
DROP INDEX index_name;
```

#### AUTO INCREMENT

- PK와 함께 사용되어 유일한 값을 생성한다.
- 데이터가 추가될 경우 설정된 컬럼에 기본적으로 1로 시작하여 1씩 추가되어 입력된다.

```
# MySQL
CREATE TABLE Persons (
    ID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);

# 100부터 시작
ALTER TABLE Persons AUTO_INCREMENT=100;


# SQL Server
CREATE TABLE Persons (
    ID int IDENTITY(1,1) PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

# 10부터 시작하여 5씩 증가
CREATE TABLE Persons (
    ID int IDENTITY(10,5) PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);


# MS Access
CREATE TABLE Persons (
    ID Integer PRIMARY KEY AUTOINCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

# 10부터 시작하여 5씩 증가
CREATE TABLE Persons (
    ID Integer PRIMARY KEY AUTOINCREMENT(10, 5),
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

# Oracle
# 시퀀스 객체를 따로 만들어 만들어진 값을 입력
CREATE SEQUENCE seq_person
MINVALUE 1
START WITH 1
INCREMENT BY 1
CACHE 10;

# 위 시퀀스에서 생성된 값을 ID 컬럼에 입력
INSERT INTO Persons (ID,FirstName,LastName)
VALUES (seq_person.nextval,'Lars','Monsen');
```

### VIEW

- SELECT로 가져올 데이터에 대한 가상테이블
- 실제 테이블처럼 동작하기도 한다.
- 가장 최근의 데이터로 만들어준다.
- 가상테이블의 데이터로 가상테이블을 만들 수도 있다.

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
# 아래 명령으로 확인
SELECT * FROM [Current Product List];


# 사용예
CREATE VIEW [Products Above Average Price] AS
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products);
# 아래 명령으로 확인
SELECT * FROM [Products Above Average Price];

# VIEW 업데이트
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

# VIEW 삭제
DROP VIEW view_name;
```
























