from scipy.integrate import quad

# 積分する関数
def f(x):
    return -2199*x**2+3.676*x+0.6194

# 積分区間
a, b = -0.015, 0.015

# 積分
result, error = quad(f, a, b)

# 結果の表示
print("積分結果:", result)
print("誤差:", error)
