from itertools import combinations  # Функция combinations() из пакета itertools создает кортежи
                                    # со всеми возможными комбинациями элементов входной последовательности

def all_variants(text):
    for n in range(len(text)): # Перебор длин комбинаций
        variant = combinations(text, n + 1) # Длина комбинаций начинается с 1
        for item in variant:
            variant_str = ''.join(item) # Преобразуем кортеж комбинаций в строку
            yield variant_str


# Вариант текста из трех символов
a = all_variants('abc')
for i in a:
    print(i)

print()

# Вариант текста из восьми символов
a = all_variants('abcdefjh')
for i in a:
    print(i)