import numpy as np
from scipy.special import iv
from scipy.optimize import root
from itertools import product
import sympy as s

# R2 Ising: independently construct the original spin-pair transfer matrix.
a,b,c,z=s.symbols('a b c z')
G=lambda z:(1+(c-a)*z)/(1-a*z+b*z*z)
N=1+a*a-b*b-2*a*c+(c*(1+b)-a)*(z+1/z)
assert s.simplify((G(z)+G(1/z)-1)*(1-a*z+b*z*z)*(1-a/z+b/z**2)-N)==0
for K1,K2 in [(0.2,-0.1),(1,-.3),(2,-1.2)]:
    states=list(product([-1,1],repeat=2))
    T=np.array([[np.exp(K1*y*w+K2*x*w) if y==v else 0 for v,w in states] for x,y in states])
    l,U=np.linalg.eig(T); j=np.argmax(l.real); L=l[j].real; v=U[:,j].real
    l2,U2=np.linalg.eig(T.T); u=U2[:,np.argmin(abs(l2-L))].real; u/=u@v
    D=np.diag([x for x,y in states])
    C=np.array([u@D@np.linalg.matrix_power(T/L,r)@D@v for r in range(200)])
    A=2*np.exp(K2)*np.sinh(K1)/L
    B=(np.exp(-2*K2)-np.exp(2*K2))/L**2
    cc=np.sinh(K1)/np.sqrt(np.sinh(K1)**2+np.exp(-4*K2))
    assert abs(C[1]-cc)<1e-12
    assert np.max(abs(C[2:]-A*C[1:-1]+B*C[:-2]))<1e-10
    for Q in [0,.3,1.2,3.14]:
        x=np.cos(Q)
        num=1+A*A-B*B-2*A*cc+2*(cc*(1+B)-A)*x
        den=(1-B)**2+A*A-2*A*(1+B)*x+4*B*x*x
        assert abs(num/den-(1+2*np.dot(C[1:],np.cos(Q*np.arange(1,len(C))))))<1e-8
    print('R2 Ising checked',K1,K2)
for t in [.1,.2,1,3,10]:
    h=np.sinh(1/t)
    k=t/4*np.log((h*h+2+h*np.sqrt(5*h*h+4))/2)
    y=np.exp(-4*k/t)
    err=(h**4-1)*y*y+(h*h+2)*y-1
    assert abs(err)<1e-12
    print('boundary',t,k,err)

# R2 XY: Fourier matrix elements vs direct quadrature.
K1,K2=4,-2
p=2*np.pi*np.arange(256)/256
T=np.exp(K1/2*(np.cos(p[:,None])+np.cos(p[None,:]))+K2*np.cos(p[:,None]+p[None,:]))
errs=[]
for m,n in product(range(-3,4),repeat=2):
    direct=np.exp(-1j*m*p)@T@np.exp(1j*n*p)/len(p)**2
    ell=np.arange(-40,41)
    formula=np.sum(iv(m-ell,K1/2)*iv(n+ell,K1/2)*iv(ell,K2))
    errs.append(abs(direct-formula))
assert max(errs)<1e-10
print('XY Fourier max error',max(errs))

# Clock R1: Fourier folding versus circulant matrix.
for q in [2,3,5,12,40]:
    K=5; p=2*np.pi*np.arange(q)/q
    T=np.exp(K*np.cos(p[:,None]-p[None,:]))
    actual=np.fft.fft(T[0]); ell=np.arange(-40,41)
    expected=np.array([q*np.sum(iv(m+ell*q,K)) for m in range(q)])
    assert np.max(abs(actual-expected))<1e-10
print('Clock folding passed')

# Multiproduct logit.
weights=np.array([np.exp(2)+np.exp(1)+1,np.exp(1)])
for B in [weights[:1],weights]:
    def fun(m):
        v=B*np.exp(-m)
        return m-1/(1-v/(1+v.sum()))
    sol=root(fun,np.ones(len(B))*2,tol=1e-12)
    assert sol.success
    v=B*np.exp(-sol.x)
    assert np.max(abs(fun(sol.x)))<1e-10
    print('firm',sol.x,v/(1+v.sum()),np.max(abs(fun(sol.x))))
