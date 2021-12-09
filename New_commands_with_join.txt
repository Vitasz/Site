//use-case 
//Получить все товары от поставищков
SELECT * FROM Providers LEFT JOIN VideoCards
ON Providers.id = VideoCards.provider_id
//Получить работников на пунктах выдачи
SELECT * FROM PickUpPoints LEFT JOIN Personals
ON PickUpPoints.personal_id = Personals.id
//Получить поставщиков по модели видеокарты
SELECT 
	(SELECT id FROM Providers WHERE id=provider_id) AS Provider_ID,
	(SELECT Place FROM Providers WHERE id = provider_id) AS Place
FROM VideoCards
WHERE VideoCards.provider_id = (SELECT provider_id FROM VideoCards WHERE Model = 'RTX5000')
//Получить поставщиков по цене
SELECT 
	(SELECT id FROM Providers WHERE id=provider_id) AS Provider_ID,
	(SELECT Place FROM Providers WHERE id = provider_id) AS Place
FROM VideoCards
WHERE VideoCards.provider_id = (SELECT provider_id FROM VideoCards WHERE Price = 3500)
//Получить поставщиков по пункту выдачи
SELECT 
	(SELECT id FROM Providers WHERE id=provider_id) AS Provider_ID,
	(SELECT Place FROM Providers WHERE id = provider_id) AS Place
FROM VideoCards
WHERE VideoCards.provider_id = (SELECT provider_id FROM VideoCards WHERE PickUpPoint =1)