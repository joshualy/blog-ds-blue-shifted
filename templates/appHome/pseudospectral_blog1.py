import numpy as np
from scipy.interpolate import BarycentricInterpolator
import matplotlib.pyplot as plt

def f(x):
    return x*np.cos(5*x**2 +2*x+1)
	
X = np.linspace(-1,1,200)
plt.plot(X,f(X),'-k')
plt.ylabel("$f$")
plt.xlabel("$x$")
plt.savefig('pseudospectral_blog1_fig0.jpg')
plt.show()


N = 5
x =  np.cos((np.pi/(N-1))*np.linspace(0,N-1,N))

plt.plot(X,f(X),'-k')
plt.plot(x,f(x),'*k')
plt.savefig('pseudospectral_blog1_fig1.jpg')
plt.show()


N = 5
x1 =  np.cos((np.pi/N)*np.linspace(0,N,N+1))
interp = BarycentricInterpolator(x1,f(x1))
u1 = interp.__call__(X)

N = 10
x2 =  np.cos((np.pi/N)*np.linspace(0,N,N+1))
interp = BarycentricInterpolator(x2,f(x2))
u2 = interp.__call__(X)

N = 15
x3 =  np.cos((np.pi/N)*np.linspace(0,N,N+1))
interp = BarycentricInterpolator(x3,f(x3))
u3 = interp.__call__(X)

plt.plot(X,f(X),'-k',label="$f$")
plt.plot(x1,f(x1),'*g')
plt.plot(X,u1,'-g',label="$p_5$")

plt.plot(x2,f(x2),'*b')
plt.plot(X,u2,'-b',label="$p_{10}$")
plt.ylabel("$y$")
plt.xlabel("$x$")
plt.legend()
plt.savefig('pseudospectral_blog1_fig2.jpg')
plt.show()


plt.plot(X,(u1-f(X)),'-g',label="$E_5$")
plt.plot(X,(u2-f(X)),'-b',label="$E_{10}$")
plt.plot(X,(u3-f(X)),'-r',label="$E_{15}$")
plt.ylabel("Error")
plt.xlabel("$x$")
plt.legend()
plt.savefig('pseudospectral_blog1_fig3.jpg')
plt.show()


