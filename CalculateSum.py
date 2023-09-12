# - calculate sum of numbers in string list, if 'stop' then finish calclulation
# - 1 argument is array of strings that are exp
# - print results
def calculate_sum_until_stop(numbers):
    sum = 0
    for number in numbers:
        try:
            sum += int(number)
        except ValueError:
            print("stop")
            break
    return sum


print(calculate_sum_until_stop(["1", "2", "3", "non-integer-string", "4"]))
