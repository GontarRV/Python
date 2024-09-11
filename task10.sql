Задания 10.4.
Задание 10.4.1
SELECT [Order Details].UnitPrice, Products.ProductName
FROM Products JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID AND [Order Details].UnitPrice < 20

Задание 10.4.2
# Выдача получилась объемнее за счёт объединения множеств 
# без фактического соответствия CustomerID.
# Встречаются значения NULL в столбце Freight для компаний Paris spécialités
# и FISSA Fabrica Inter. Salchichas S.A., т.к. отсутствуют заказы с их CustomerID.

Задание 10.4.3
# Добавить:
WHERE Employees.EmployeeID = Orders.EmployeeID

Задание 10.4.4
SELECT Products.ProductName, [Order Details].UnitPrice
FROM Products JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID