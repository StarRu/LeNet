import random
import time

a = -10
b = 10
pcs = 5
rnd_list =[]

tstart = time.time()
for ii in range(pcs):
    rnd_list.append(random.randint(a,b)/10)

total = sum(rnd_list)
ave = total /pcs

x = []
for ll in range(len(rnd_list)):
    x.append((ave - rnd_list[ll])**2)
sigma = (sum(x)/pcs)**0.5
tend = time.time()

print("random : ",rnd_list,"\n","total : ",total,"\n","Ave. : ",ave,"\n","sigma : ", sigma)
print(tstart, tend, (tend - tstart))