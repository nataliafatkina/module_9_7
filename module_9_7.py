def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        for i in range(2, number + 1):
            if number % i > 0 or number == i:
                return 'Простое'
            elif number % i == 0:
                return 'Составное'
        else:
            return 'Число ни простое, ни составное'

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(-2, 3)
print(result)
