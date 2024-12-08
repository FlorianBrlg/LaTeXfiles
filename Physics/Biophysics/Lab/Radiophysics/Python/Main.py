import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = np.array([15,30,45])
y = np.array([8.364, 18.204, 27.762])
xr = np.array([-5, 15, 30, 45, 50])
reg = stats.linregress(x,y)
print(reg)

plt.scatter(x,y)
plt.plot(xr, reg.slope * xr + reg.intercept)

plt.xlabel("Irradiated time in s.")
plt.ylabel("Charge picked up in nC.")
plt.grid()
plt.savefig("PrepMeasure.png")
plt.show()



x = np.array([0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6])
y = np.array([18, 13.48, 10.36, 8.44, 6.91, 5.52, 4.74])
xr = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
reg = stats.linregress(1/(x**2),y)
print(reg)

plt.scatter(1/(x**2),y)
plt.plot(xr, reg.slope * xr + reg.intercept)


plt.xlabel("Distance in 1/cm^2")
plt.ylabel("Charge picked up in nC.")
plt.grid()
plt.savefig("InvSquare.png")
plt.show()


xr = np.array([0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8])

plt.scatter(x, y)
plt.plot(xr, reg.slope * 1/(xr**2) + reg.intercept)
plt.grid()
plt.xlabel("Distance in cm")
plt.ylabel("Charge picked up in nC")

plt.savefig("InvSquared2.png")
plt.show()


x = np.array([1.52, 2.02, 2.52, 3.02, 4.02])
y = np.array([18.0, 16.14, 14.54, 13.11, 11.05])

reg = stats.linregress(x-1.52, np.log(y*(1/18.0)))

#y = y*(1/18.0)
#y = np.log(y)

plt.scatter( x-1.52, np.log(y*(1/18.0)))
plt.plot(x-1.52, reg.slope * (x-1.52) + reg.intercept)
plt.grid()

print(reg.slope)

plt.savefig("Attenuation Coeff")
plt.show()

