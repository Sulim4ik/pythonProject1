n = int(input("Введите целое число: "))
rev_number = 0
n_1 = n % 10
n_2 = n // 10 % 10
n_3 = n // 100 % 10

rev_number = n_3 + n_2*10 + n_1*100

print('"Обратное" ему число:', rev_number)