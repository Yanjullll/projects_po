# Лабораторная работа №1: Git
Осваиваю базовое ПО и основы работы в терминале
## Сделано:
- [x] Освоена командная строка (CMD и PowerShell)
- [x] Зарегистрирован аккаунт на GitHub
- [x] Создан удалённый репозиторий
- [x] Изучен синтаксис разметки Markdown

```python
import numpy as np
import matplotlib.pyplot as plt

# параметр
a = 1

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

F = X**3 + Y**3 - 3*a*X*Y

plt.figure(figsize=(3, 3))
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='blue', linestyle='--', alpha=0.5)
plt.axvline(0, color='blue', linestyle='--', alpha=0.5)
plt.title('Декартов лист')
plt.contour(X, Y, F, levels=[0], colors='lightblue')
plt.show()
```
