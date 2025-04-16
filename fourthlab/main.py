import numpy as np
import matplotlib.pyplot as plt

# === 1. Генерация данных ===
x = np.arange(0, 10.1, 0.1)  # x ∈ [0; 10] с шагом 0.1
y = 0.1 * x**5 - 100 * x**4 + 700 * x**2  # Вариант 4

# === 2. Обучающая выборка (по чётным индексам) ===
x_train = x[::2]
y_train = y[::2]

# === 3. Функция для построения дизайн-матрицы полинома ===
def build_design_matrix(x, degree=13):
    return np.vstack([x**i for i in range(degree + 1)]).T

X_train = build_design_matrix(x_train)
X_full = build_design_matrix(x)

# === 4. Обычная регрессия (без регуляризации) ===
w_no_reg = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y_train
y_pred_no_reg = X_full @ w_no_reg

# === 5. L2-регуляризация ===
lambd = 0.1  # Коэффициент регуляризации (можно поэкспериментировать)
I = np.eye(X_train.shape[1])  # Единичная матрица
w_l2 = np.linalg.inv(X_train.T @ X_train + lambd * I) @ X_train.T @ y_train
y_pred_l2 = X_full @ w_l2

# === 6. Визуализация ===
plt.figure(figsize=(12, 6))
plt.plot(x, y, label='Истинная функция', linewidth=2)
plt.plot(x, y_pred_no_reg, '--', label='Без регуляризации', linewidth=2)
plt.plot(x, y_pred_l2, '--', label=f'L2-регуляризация (λ = {lambd})', linewidth=2)
plt.scatter(x_train, y_train, color='red', label='Обучающая выборка', zorder=5)
plt.title('Аппроксимация функции полиномом степени 13')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === 7. (необязательно) Оценка ошибок ===
from sklearn.metrics import mean_squared_error

print("MSE без регуляризации:", mean_squared_error(y, y_pred_no_reg))
print("MSE с L2-регуляризацией:", mean_squared_error(y, y_pred_l2))
