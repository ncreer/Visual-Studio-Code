import csv

life_low = float('inf')
life_high = float('-inf')
life_low_country = ""
life_high_country = ""
header = []
with open(r"C:\Users\g8tor\OneDrive\Documents\BYUI\Visual_Studio_Code\cse110\info\life-expectancy.csv", 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    for row in csv_reader:
        country = row[0]
        year = row[2]
        life = float(row[3])
        if life < life_low:
            life_low = life
            life_low_country = f"{country} in {year}"
        if life > life_high:
            life_high = life
            life_high_country = f"{country} in {year}"
print(f'The overall max life expectancy is: {life_high} from {life_high_country}')
print(f'The overall min life expectancy is: {life_low} from {life_low_country}')
select_year = input('Enter the year of interest: ')
select_total_life = 0
life_count = 0
select_life_low = float('inf')
select_life_high = float('-inf')
select_life_low_country = ""
select_life_high_country = ""
with open(r"C:\Users\g8tor\OneDrive\Documents\BYUI\Visual_Studio_Code\cse110\info\life-expectancy.csv", 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    for row in csv_reader:
        country = row[0]
        year = row[2]
        life = float(row[3])
        if year == select_year:
            select_total_life += life
            life_count += 1
            if life < select_life_low:
                select_life_low = life
                select_life_low_country = f"{country}"
            if life > select_life_high:
                select_life_high = life
                select_life_high_country = f"{country}"
average_life = select_total_life / life_count
print(f'For the year {select_year}:')
print(f'The average life expectancy across all countries was {average_life:.2f}')
print(f'The max life expectancy was in {select_life_high_country} with {select_life_high}')
print(f'The min life expectancy was in {select_life_low_country} with {select_life_low}')