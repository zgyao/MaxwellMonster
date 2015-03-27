import math
import numpy as np

BoltzmanConstant = 1.3806488e-23
ProtonMass = 1.67262178e-27
Mass = 39.8*ProtonMass
Temperature = 300.

Sigma = math.sqrt(Mass*BoltzmanConstant*Temperature)
NumPtcls = 20000
Px = np.random.normal(0.,Sigma,NumPtcls)
Vx = Px/Mass

XRange = 10.
X = np.random.uniform(-XRange/2.,XRange/2.,NumPtcls)

VxMax = max(Vx.min(), Vx.max(), key = abs)
NDX = 50
DX = XRange/NDX
DT = XRange/NDX/abs(VxMax)
NumSteps = 2000

VMark = 700.
TotalMonster = 0
for i in range(0,NumSteps):
    Monster = 0
    LeftEk = 0.
    RightEk = 0.
    LeftNum = 0
    RightNum = 0
    for j in range(0,NumPtcls):
        if X[j] < 0:
            LeftEk = LeftEk + 0.5*Mass*Vx[j]*Vx[j]
            LeftNum = LeftNum + 1
        else:
            RightEk = RightEk + 0.5*Mass*Vx[j]*Vx[j]
            RightNum = RightNum + 1
        X[j] = X[j] + Vx[j]*DT
        if abs(abs(X[j])-XRange/2.) < DX and Vx[j]*X[j] > 0:
            Vx[j] = -Vx[j];
        elif abs(X[j]) < DX and Vx[j]*X[j] < 0 and abs(Vx[j]) > VMark:
            Vx[j] = abs(Vx[j])
            Monster = Monster + 1
    TotalMonster = TotalMonster + Monster
    if i == 0 or (i+1)%(NumSteps/10) == 0:
        LeftT = LeftEk/LeftNum/0.5/BoltzmanConstant - 273.15
        RightT = RightEk/RightNum/0.5/BoltzmanConstant - 273.15
        print str((i+1)/(NumSteps/10)*10) + "%, " + str(LeftT) + ", " + str(RightT)
print LeftT, RightT, TotalMonster, NumSteps*DT
