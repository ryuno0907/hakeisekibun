import matplotlib.pyplot as plt
import numpy as np
import glob
import math

filelist1 = glob.glob("D:/b3/*")    #線源ありの波形のフォルダ
filelist2 = glob.glob("D:/background/*")    #バックグラウンドの波形のフォルダ

nbin = 160
S1 = []
S2 = []
M1=[]
M2=[]
# 線源
for file in filelist1:
    data = np.loadtxt(file)
    time = data[:, 0]
    ch1 = data[:, 1]
    ch2 = data[:, 2]

    time_cut = time[480:540]    #波形がありそうな積分区間
    ch1_cut = ch1[450:550]
    ch2_cut = ch2[450:550]
    ch1_cut_1 = ch1[0:399]  # ゼロ点求める用(波形がなさそうな区間)
    ch2_cut_1 = ch2[0:449]

    deltaT = time_cut[1] - time_cut[0]

    #ゼロ点を求める
    mean = 0
    for i in ch1_cut_1:
        deltamean = i  / 400
        mean = mean + deltamean

    s1 = 0
    for i in ch1_cut:
        deltaS1 = -(i - mean) * deltaT
        s1 = s1 + deltaS1
    K1=s1*0.03144 #Calibration 波形の面積->運動エネルギー
    E1=K1+0.511     #エネルギー＝運動＋質量
    p1=math.sqrt(E1**2-0.511**2)    #運動量の計算
    M1.append(p1)
    S1.append(s1)

# background
for file in filelist2:
    data = np.loadtxt(file)
    time = data[:, 0]
    ch1 = data[:, 1]
    ch2 = data[:, 2]

    time_cut = time[480:540]
    ch1_cut = ch1[450:550]
    ch2_cut = ch2[450:550]
    ch1_cut_1 = ch1[0:399]  
    ch2_cut_1 = ch2[0:449]

    deltaT = time_cut[1] - time_cut[0]

    mean = 0
    for i in ch1_cut_1:
        deltamean = i  / 400
        mean = mean + deltamean

    s2 = 0
    for i in ch1_cut:
        deltaS2 = -(i - mean) * deltaT
        s2 = s2 + deltaS2
    # E の値が 0.511^2 より小さい場合の例外処理
    
    K2=s2*0.03144 
    E2=K2+0.511
    if E2 >= 0.511**2:
        p2 = np.sqrt(E2**2 - 0.511**2)
        M2.append(p2)
        S2.append(s2)
    else:
        print("E の値が不正です。")

    
    

# ヒストグラムの取得
bin_max = 3.0
bin_min = 0
hist_S1, bin_edges_S1 = np.histogram(M1, bins=nbin, range=(bin_min, bin_max))
hist_S2, bin_edges_S2 = np.histogram(M2, bins=nbin, range=(bin_min, bin_max))

# データ数の差を計算
hist_diff = hist_S1 - hist_S2

# ビンの中心を計算
bin_centers = (bin_edges_S1[:-1] + bin_edges_S1[1:]) / 2

# 差のヒストグラムを表示
plt.bar(bin_centers, hist_diff, width=bin_edges_S1[1] - bin_edges_S1[0], color='green')
plt.xlabel("Momentum")
plt.ylabel("energy spectrum")
plt.xlim(0,bin_max)
plt.grid()
plt.show()
