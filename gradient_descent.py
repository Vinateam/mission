# coding=utf-8
x = [[1, 1437., 3], [1, 1239., 3], [1, 2132., 4], [1, 4215., 4], [1, 2162., 4], [1, 1664., 2], [1, 2238., 3], [1, 2567., 4],
     [1, 1200., 3], [1, 852., 2], [1, 1852., 4], [1, 1203., 3]]
y = [249900, 229900, 345000, 549000, 287000, 368500, 329900, 314000, 299000, 179900, 299900, 239500]

# 将y数组进行缩小 至特征值0~5
yi = []
for i in range(len(y)):
    y[i] = float(y[i])
for i in y :
    yi.append(i/100000)
print yi


epsilon = 0.00000000000001  #收敛程度
alpha = 0.00000045          #学习速率
m = len(x)
j = 0
h = [None] * m
J = [None] * m
dJ = 0
dJ2 = 0
theta0 = 1
theta1 = 1
theta2 = 1
temp0 = 0
temp1 = 0
temp2 = 0
a = 0

while True:
    for i in range(m):
        h[i] = theta0 * x[i][0] + theta1 * x[i][1] + theta2 * (x[i][2])  # 定义预测值公式
        J[i] = h[i] - yi[i]   #代价函数
        temp0 -= (alpha * J[i] * x[i][0]) / m #同步更新theta
        temp1 -= (alpha * J[i] * x[i][1]) / m
        temp2 -= (alpha * J[i] * x[i][2]) / m
    theta0 = temp0
    theta1 = temp1
    theta2 = temp2
    for i in range(m):
        h[i] = theta0 * x[i][0] + theta1 * x[i][1] + theta2 * (x[i][2])
        J[i] = h[i] - yi[i]
        dJ += ((J[i] * J[i]) / (2 * m))

    print theta0,theta1,theta2,dJ  #输出收敛过程中 theta 变化 可有可无
    #判断是否收敛 根据epsilon的大小 可控制精确程度 也会影响运行速率
    if ((dJ-dJ2)**2) < epsilon:
        break
    else:
        dJ2 = dJ
        dJ = 0

for i in range(m):
    h[i] = (theta0 * x[i][0] + theta1 * x[i][1] + theta2 * (x[i][2]))*100000
    print h[i], x[i][1], x[i][2], y[i]












