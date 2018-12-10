print('-' * 60)
print('100th Birthday Program: ')
print()
print('Description: This program asks you for your current age and tells you the year that you will turn 100.')
print()

agetoday = input('What is your age today? ')
years = 100 - int(agetoday)
answer = 2018 + int(years)

print('You will turn 100 in the year ' + str(answer))
print('-' * 60)