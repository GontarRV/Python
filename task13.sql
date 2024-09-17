Задания 13.3.
Задание 13.3.1
UPDATE [Order Details]
SET Discount = '0.2'
WHERE Quantity > 50

Задание 13.3.2
UPDATE Contacts
SET City = 'Piter' AND Country = 'Russia'
WHERE City = 'Berlin' AND Country = 'Germany'


Задание 13.3.3
INSERT INTO Shippers
VALUES ('DNS', '(495)-111-11-11'), ('OZON', '(499)-111-11-11')

# соответственно удаление автоматически присваеваемого ID > 3
DELETE FROM Shippers 
WHERE ShipperID > 3

