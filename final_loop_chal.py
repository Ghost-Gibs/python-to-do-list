number = 1

while number <= 30:
    if number > 25:
        break
    if number % 3 == 0:
        number += 1
        continue
    print(number)
    number += 1