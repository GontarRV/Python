Задания 12.3.
Задание 12.3.1
INSERT INTO Employees (FirstName, LastName, Title, TitleOfCourtesy, BirthDate, HireDate, Address,  City, Country, PostalCode, HomePhone, ReportsTo)
VALUES ('Roman', 'Gontar', 'Manager', 'Mr.', '1984-07-19T00:00:00.000', '2024-09-15T00:00:00.000', 'Centr', 'Moscow', 'Russia', '124124', '+7(499) 999-99-99', 2)

Задание 12.3.2
INSERT INTO EmployeeTerritories (EmployeeID, TerritoryID)
VALUES (10, 11111)

Задание 12.3.3
INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, RequiredDate, ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipPostalCode, ShipCountry)
VALUES ('ROMGO', 10, '2024-09-15T00:00:00.000', '2024-09-18T00:00:00.000', 2, 50, 'Suprêmes délices', 'Centr', 'Moscow',  '124124', 'Russia')