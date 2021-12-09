1) UPDATE Personals SET birthday = SUBSTR(birthday, 7, 4) || '-' || SUBSTR(birthday, 4, 2) || '-' ||SUBSTR(birthday, 1, 2);
2) ---- 
3) SELECT DISTINCT(birthday) FROM Personals;
4) SELECT SUM(ProductCount) AS 'total_products' FROM PickUpPoints;
5) Средняя дата продавцов, чей возраст не меньше 19:
SELECT avg(age) AS "sr_age"
FROM Personals
WHERE age >= 19;
