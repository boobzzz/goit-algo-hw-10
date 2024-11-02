# Порівняльний аналіз результатів методу Монте-Карло та функції quad

### Опис завдання
Задача полягає у знаходженні визначеного інтегралу функції `f(x) = sin(x)` на інтервалі [0, π] за допомогою методу Монте-Карло та функції `quad` з бібліотеки SciPy. 

### Результати
- **Метод Монте-Карло**:
  - Результат: 1.9998 (може варіюватися через випадковий характер алгоритму)
- **Метод quad**:
  - Результат: 2.0 (точне значення інтегралу)

### Порівняння
- **Метод Монте-Карло**:
  - Переваги: Простий у реалізації, добре працює для багатовимірних інтегралів.
  - Недоліки: Висока варіативність результатів, потребує великої кількості семплів для досягнення високої точності.
  
- **Метод quad (SciPy)**:
  - Переваги: Висока точність, швидкість виконання для одномірних інтегралів.
  - Недоліки: Може бути складним у реалізації для багатовимірних інтегралів, потребує більше обчислювальних ресурсів.

### Висновок
Метод Монте-Карло може бути корисним для швидких наближених розрахунків інтегралів, особливо для багатовимірних задач. Проте, для одномірних інтегралів функція `quad` з бібліотеки SciPy забезпечує високу точність та швидкість. Таким чином, вибір методу залежить від конкретних вимог до задачі та доступних обчислювальних ресурсів.