import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pointFive =np.loadtxt('pointfive.csv', delimiter=',', skiprows=1) 

#print(pointFive)
#print(pointFive[0])

count1 = np.sum((pointFive > 600) & (pointFive < 800))
count2 = np.sum((pointFive > 1300) & (pointFive < 1500))

print(count1)
print(count2)



plt.hist(pointFive, bins=500)

plt.title("0.5 Gy Dosis")
plt.savefig("pointfive.jpg")
plt.show()


Five =np.loadtxt('five.csv', delimiter=',', skiprows=1) 

#print(Five)
#print(Five[0])

count1 = np.sum((Five > 600) & (Five < 800))
count2 = np.sum((Five > 1300) & (Five < 1500))

print(count1)
print(count2)



plt.hist(Five, bins=500)

plt.title("5 Gy Dosis")
plt.savefig("five.jpg")
plt.show()



Zero =np.loadtxt('Zero.csv', delimiter=',', skiprows=1) 

#print(Zero)
#print(Zero[0])

count1 = np.sum((Zero > 600) & (Zero < 800))
count2 = np.sum((Zero > 1300) & (Zero < 1500))

print(count1)
print(count2)



plt.hist(Zero, bins=500)

plt.title("0 Gy Dosis")
plt.savefig("Zero.jpg")
plt.show()

