import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
import matplotlib.patches as patches
#import japanize_matplotlib



R = 0.0125  # 磁場半径[m]
B = 0.5  # 磁束密度[T]

# positions リストをループ外で初期化
positions = []

for i in range(1, 4):
    p = 1.1 + 0.3 * i  # 運動量[MeV/c]
    rho = p / (300 * B)  # P[GeV/c]=0.3*B[T]*r[m]から曲率半径の導出

    # 軌跡の座標を計算
    y = -2 * R * (R**2 - rho**2) / (3 * R**2 - rho**2)
    x = -4 * rho * R**2 / (3 * R**2 - rho**2)

    # 座標を positions リストに追加
    positions.append([x, y])

    # 描画
    #plt.plot(x, y, label=f'p = {p} MeV/c')

# 磁場の円を描画
circle = plt.Circle((0, 0), R, fill=True, edgecolor='black', facecolor='lightblue')
plt.gcf().gca().add_artist(circle)

# positions リストを使って焦点を描画
x_focus, y_focus = zip(*positions)
plt.plot(x_focus, y_focus, 'ro', label='focus')

plt.plot(0, -2 * R, 'bo', label='radiation source')

plt.xlabel("X[m]")
plt.ylabel("Y[m]")
plt.axis('equal')
plt.xlim(-0.05,0.05)
plt.ylim(-0.05,0.05)
plt.legend()
plt.grid(True)
plt.show()
