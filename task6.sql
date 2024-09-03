Задания 6.3.
6.3.1.
SELECT COUNT(ContactType) FROM Contacts
GROUP BY ContactType

6.3.2.
SELECT CategoryID, AVG(UnitPrice) as Average_price FROM Products
GROUP BY CategoryId
ORDER BY Average_price

