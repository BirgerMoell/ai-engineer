# 
## make a funciotn that takes a list of numbers and returns the sum of the squares of the numbers
def sum_of_squares(numbers):
    sum = 0
    for number in numbers:
        sum += number * number
    return sum