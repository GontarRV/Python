Задания 7.3.
7.3.1.
SELECT (Discount * 100) AS Percent_Discount
FROM [Order Details]

7.3.2.
SELECT * FROM [Order Details]
WHERE ProductId IN (SELECT ProductID FROM Products WHERE UnitsInStock > 40)

Задание 7.3.3.
SELECT * FROM [Order Details]
WHERE ProductId IN (SELECT ProductID FROM Products WHERE UnitsInStock > 40)
AND OrderID IN (SELECT OrderID FROM Orders WHERE Freight >= 50)

