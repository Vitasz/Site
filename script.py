import sqlite3

connection = sqlite3.connect('SiteDB.db')

cursor = connection.cursor()

def DB_init():
    cursor.executescript(
        '''
CREATE TABLE Personals(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   FIO string NOT NULL,
   age int NOT NULL,
   Wage int NOT NULL,
   gender bool NOT NULL,
   birthday date NOT NULL,
   PlaceOfResidence string NOT NULL
   );
CREATE TABLE PickUpPoints(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   Place string NOT NULL,
   WorkTime int NOT NULL,
   personal_id INTEGER NOT NULL,
   Buys int NOT NULL,
   ProductCount int NOT NULL,
   FOREIGN KEY (personal_id) REFERENCES Personals(id)
   );
CREATE TABLE Providers(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   Place string NOT NULL,
   Prices int NOT NULL,
   Buys int NOT NULL,
   ProductCount int NOT NULL
   );
CREATE TABLE VideoCards(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   ProductionDate date NOT NULL,
   Model string NOT NULL,
   provider_id INT NOT NULL,
   Price int NOT NULL,
   PickupPoint int NOT NULL,
   FOREIGN KEY (PickupPoint) REFERENCES PickUpPoints,
   FOREIGN KEY (provider_id) REFERENCES Providers(id)
   );

   ''')

def GetProvidersAndVideocards():
    cursor.execute('SELECT * FROM Providers LEFT JOIN VideoCards ON Providers.id = VideoCards.provider_id;')
    print(*cursor.fetchall(), sep='\n')

def GetWorkersOnPickUpPoints():
    cursor.execute('SELECT * FROM PickUpPoints LEFT JOIN Personals ON PickUpPoints.personal_id = Personals.id')
    print(*cursor.fetchall(), sep='\n')
def GetProvidersByVideocardModel(model):
    cursor.execute('''SELECT DISTINCT
	(SELECT id FROM Providers WHERE id=provider_id) AS Provider_ID,
	(SELECT Place FROM Providers WHERE id = provider_id) AS Place
        FROM VideoCards
        WHERE VideoCards.provider_id = (SELECT provider_id FROM VideoCards WHERE Model = \''''+model +'\')')
    print(*cursor.fetchall(), sep='\n')
def GetProvidersByVideocardPrice(price):
    cursor.execute('''SELECT DISTINCT
	(SELECT id FROM Providers WHERE id=provider_id) AS Provider_ID,
	(SELECT Place FROM Providers WHERE id = provider_id) AS Place
        FROM VideoCards
        WHERE VideoCards.provider_id = (SELECT provider_id FROM VideoCards WHERE Price = \''''+price+'\')')
    print(*cursor.fetchall(), sep='\n')
def GetProvidersByVideocardPickUpPoint(PickUpPoint):
    cursor.execute('''SELECT DISTINCT
	(SELECT id FROM Providers WHERE id=provider_id) AS Provider_ID,
	(SELECT Place FROM Providers WHERE id = provider_id) AS Place
FROM VideoCards
WHERE VideoCards.provider_id = (SELECT provider_id FROM VideoCards WHERE PickUpPoint = \''''+PickUpPoint+'\')''')
    print(*cursor.fetchall(), sep='\n')
#DB_init()
GetProvidersAndVideocards()
print()
GetWorkersOnPickUpPoints()
print()
GetProvidersByVideocardModel("RTX4000")
print()
GetProvidersByVideocardPrice('3500')
print()
GetProvidersByVideocardPickUpPoint('1')
print()
connection.close()
