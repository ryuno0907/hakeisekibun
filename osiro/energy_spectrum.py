import matplotlib
import math
import numpy as np
import glob
import matplotlib.pyplot as plt

filelist=glob.glob("D:/b4/*")

nbin=160
S=[]
M=[]
E=[]
for file in filelist:
    data = np.loadtxt(file)
    time = data[:,0]
    ch1 = data[:,1]
    ch2 = data[:,2]

    time_cut = time[480:540]
    ch1_cut = ch1[450:550]
    ch2_cut = ch2[480:540]
    ch1_cut_1 = ch1[0:399] #平均求める用
    ch2_cut_1 = ch2[0:449]

    deltaT = time_cut[1]-time_cut[0]

    mean = 0
    for i in ch1_cut_1:
        deltamean = i/400.0
        mean = mean + deltamean
    

    s = 0
    for i in ch1_cut:
        deltaS = -(i - mean)*deltaT
        s = s + deltaS
    K=s*0.03144 #Calibration(運動エネルギー) 波形の面積
    E=K+0.511
    p=math.sqrt(E**2-0.511**2)
    M.append(p)  #運動量
    S.append(s)  #波形の面積
    

bin_max = 80
bin_min = 0
bin_range=(bin_min, bin_max)
plt.hist(M, nbin, range = (0,3.0))
plt.xlabel("M")
plt.ylabel("entries")
plt.grid()
plt.xlim(0,3.0)
plt.show()


