import numpy as np
import matplotlib.pyplot as plt

# 1. Исходные данные
x = np.arange(0, 10.1, 0.1)
y = 0.1 * x**5 - 100 * x**4 + 700 * x**2

# 2. Нормализация x
x_norm = (x - x.min()) / (x.max() - x.min())

# 3. Обучающая выборка: только четные индексы
x_train_norm = x_norm[::2]
y_train = y[::2]

# 4. Построение полиномиальной матрицы
def build_design_matrix(x, degree=13):
    return np.vstack([x**i for i in range(degree + 1)]).T

X_train = build_design_matrix(x_train_norm)
X_full = build_design_matrix(x_norm)

# 5. Без регуляризации
w_no_reg = np.linalg.pinv(X_train.T @ X_train) @ X_train.T @ y_train
y_pred_no_reg = X_full @ w_no_reg

# 6. С регуляризацией
lambda_ = 0.1
I = np.eye(X_train.shape[1])
w_l2 = np.linalg.pinv(X_train.T @ X_train + lambda_ * I) @ X_train.T @ y_train
y_pred_l2 = X_full @ w_l2

# 7. График
plt.figure(figsize=(12, 6))
plt.plot(x, y, label='Истинная функция', linewidth=2)
plt.plot(x, y_pred_no_reg, '--', label='Без регуляризации', linewidth=2)
plt.plot(x, y_pred_l2, '--', label='L2-регуляризация (λ=0.1)', linewidth=2)
plt.scatter(x[::2], y_train, color='red', label='Обучающая выборка')
plt.title('Аппроксимация функции полиномом степени 13')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
