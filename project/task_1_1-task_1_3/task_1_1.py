import sys
print("Версия Python: ", sys.version.split()[0])
print("Интерпретатор: ", sys.executable)

print('Количество путей: ', len(sys.path))
for n in sys.path[:4]:
    print("  ", n)

import math, random
print("math.pi=", math.pi)
print("random.random()=", random.random())

mods = sorted(sys.modules)
print("Всего загруженных модулей: ", len(mods))
print("Пример: ", mods[:5])

# TODO 1
public = [i for i in dir(math) if not n.startswith('__')]
print('Публичных имён в math: ', len(public))
print('Первые 8: ', public[:8])

# TODO 2
print('Мой__name__ =', __name__)

# Если назвать свою библиотеку так же, как встроенный модуль `random`, возникнет конфликт имён. 
# Дело в том, что и в главном модуле (`__main__`), и в библиотеке будет выполняться импорт модуля `random` 
# И в итоге везде будет использоваться именно стандартная библиотека, а не функции.