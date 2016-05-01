import csv

dates = []
impoundNum = []
breedName = []
loc = []

with open('C:\\Users\\jdotmurphy\\Desktop\\Lost__found__adoptable_pets.csv','r') as csvfile:
    csvfileReader = csv.reader(csvfile, delimiter = ',')
    next (csvfileReader, None)
    for row in csvfileReader:
        animalID = row[1]
        breed = row[10]
        date = row[12]
        location = row[23]

        dates.append(date)
        impoundNum.append(animalID)
        breedName.append(breed)
        loc.append(location)

    print(dates)
    print(impoundNum)
    print(breedName)
    print(loc)