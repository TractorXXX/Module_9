# Речь идет о простых и составных числах. Они принадлежат множеству натуральных чисел, а значит и числа
# a, b, c также должны быть из этого множества

def is_prime(func):
    
    def wrapper(a, b, c):
        result_func = func(a, b, c)
        flag_prime = True # Флаг простого числа

# Минимальная сумма трех натуральных чисел равна 3, поэтому цикл начинаем с 3.

        for i in range(3, result_func):
            if result_func % i == 0:
                flag_prime = False
                break
            else:
                flag_prime = True

        if flag_prime:
            print('Простое')
        else:
            print('Составное')

        return result_func

    return wrapper


@ is_prime
def sum_three(a, b, c):
    summa = a + b + c
    return summa


result = sum_three(2, 3, 6)
print(result)