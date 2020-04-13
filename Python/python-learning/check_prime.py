## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through check prime array
for num in check_prime:
    # iterating through the number from 2 to the number itself
    for i in range(2, num):
        # if the number in array can be divided by the current num then it is NOT a prime number
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}.".format(num, i, num))
            break
        # if current number is equal to the num then declare it prime
        if i == num-1:
            print("{} IS a prime number.".format(num))
