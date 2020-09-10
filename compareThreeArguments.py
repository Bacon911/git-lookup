def compare_three_numbers(a, b, c):
    if (a + b) > c:
        print('Сумма первых двух чисел больше 3-го.')
    else:
        print('Третье число больше или равно сумме первых двух.')


compare_three_numbers(1, 5, 2)
compare_three_numbers(1, 2, 100)
compare_three_numbers(1, 2236423, 104230)
compare_three_numbers(1, 2526354, 1032230)
compare_three_numbers(0, 1, 1032230)
