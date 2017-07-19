import random
import time

# HW2.1 產生五個亂數，並將其輸出
print("# HW2.1 產生五個亂數，並將其輸出")
a = 1
b = 10
num1 = 5
rnd_list1 = []
#取亂數
for ii in range(num1):
    rnd_list1.append(random.randint(a, b))

print("Random 5 number between", a, "and", b, ":", rnd_list1, "\n")

# HW2.2 產生N個介於-1與1之間的亂數，計算其平均值與標準差並輸出，每個亂數的值則不用輸出。N=10**1, 10**2, 10**3, 10**4, 10**5
# HW2.3 做基本題2時，一併輸出產生每N個亂數前後的系統時間，並計算所需的時間。
print("# HW2.2 產生N個介於-1與1之間的亂數，計算其平均值與標準差並輸出，每個亂數的值則不用輸出。N=10**1, 10**2, 10**3, 10**4, 10**5")
a = -1
b = 1
num2 = 10
rnd_list = []
for n in range(1,6):
    num_ = num2**n
    tstart = time.time()
    #取亂數
    for ii in range(num_):
        rnd_list.append(random.uniform(a, b))

    total = sum(rnd_list)
    ave = total / num_
    
    #標準差
    x = []
    for ll in range(len(rnd_list)):
        x.append((ave - rnd_list[ll]) ** 2)
    sigma = (sum(x) / num_) ** 0.5
    tend = time.time()

    print("N=10**%d" %n)
    print("total:%3.3f Ave.:%3.3f sigma:%3.3f" % (total, ave, sigma))
    print(tstart, tend, "time:",(tend - tstart))


# HW2.4 自己寫一個亂數產生器。
