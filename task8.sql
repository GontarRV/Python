Задания 7.3.
Задание 8.3.1.
SELECT Products.ProductName, Categories.CategoryName
FROM Products, Categories
WHERE Products.CategoryID = Categories.CategoryID

Задание 8.3.2.
SELECT [Order Details].UnitPrice, Products.ProductName
FROM Products, [Order Details]
WHERE Products.ProductID = [Order Details].ProductID AND [Order Details].UnitPrice < 20

Задание 8.3.3.
SELECT [Order Details].UnitPrice, Products.ProductName, Categories.CategoryName
FROM Products, [Order Details], Categories
WHERE Products.ProductID = [Order Details].ProductID AND [Order Details].UnitPrice < 20
	AND Categories.CategoryID = Products.CategoryID