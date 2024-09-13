Задания 11.5.
Задание 11.5.1
SELECT * FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.CustomerID IS NULL

Задание 11.5.2
SELECT ContactName, City, Country, 'Customer' AS Type FROM Customers
UNION
SELECT ContactName, City, Country, 'Supplier' AS Type FROM Suppliers