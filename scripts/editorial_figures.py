"""Analytic figures for the editorial revision. Run before postprocess_figures."""
from pathlib import Path
import numpy as np
from scipy.special import ellipk
from scipy.optimize import root
from figure_style import new_figure, style_axes, plot_exact, plot_approx, style_legend, save_figure, COLORS

OUT=Path(__file__).resolve().parents[1]/"public"/"figures"

def save(fig, name):
    save_figure(fig, OUT/name)

def dividing_surface():
    fig,ax=new_figure()
    x=np.linspace(.5,1.8,500)
    plot_exact(ax,x,2*x/3+1/(3*x*x))
    ax.axvline(1,color=COLORS["muted"],ls=":",lw=2)
    ax.scatter([1],[1],color=COLORS["ink"],zorder=5)
    style_axes(ax,xlabel=r"$R/R_s$",ylabel=r"$\gamma(R)/\gamma_s$")
    save(fig,"interfaces/notional-surface-tension.svg")

def diffuse():
    fig,ax=new_figure()
    z=np.linspace(-4,4,500)
    plot_exact(ax,z,np.tanh(z),label=r"$\phi/\phi_b$")
    plot_approx(ax,z,1/np.cosh(z)**4,label=r"$\Pi/\Pi(0)$")
    style_axes(ax,xlabel=r"$(z-z_0)/\ell$",ylabel="Normalized profile",zero_y=True)
    style_legend(ax,loc="upper left")
    save(fig,"interfaces/square-gradient-profile.svg")

def boundary_layer():
    fig,ax=new_figure()
    x=np.linspace(0,1,1001)
    for e,ls,color in [(0.2,"-",COLORS["accent"]),(0.05,"--",COLORS["green"]),(0.01,"-.",COLORS["ink"])]:
        ax.plot(x,-np.expm1(-x/e)/(-np.expm1(-1/e)),ls=ls,color=color,lw=3.6,label=fr"$\varepsilon={e:g}$")
    style_axes(ax,xlabel=r"$x$",ylabel=r"$y(x)$")
    style_legend(ax,loc="lower right")
    save(fig,"mathematics/boundary-layer.svg")

def pendulum():
    fig,ax=new_figure()
    theta=np.linspace(0,179,500)
    ratio=2*ellipk(np.sin(np.deg2rad(theta)/2)**2)/np.pi
    plot_exact(ax,theta,ratio,label="Exact")
    ax.axhline(1,color=COLORS["green"],ls="--",lw=3.6,label="Small amplitude")
    style_axes(ax,xlabel=r"$\theta_{\max}$ (deg)",ylabel=r"$T/T_0$")
    style_legend(ax,loc="upper left")
    save(fig,"mathematics/pendulum-period.svg")

def clock_ground_state():
    fig,ax=new_figure()
    k=np.linspace(0,1,501)
    q=16
    a=2*np.pi*np.arange(q)/q
    E=-(np.cos(a[:,None])+np.cos(a[None,:]))/2+k[:,None,None]*np.cos(a[:,None]+a[None,:])
    exact=E.min(axis=(1,2))
    uniform=np.diagonal(E,axis1=1,axis2=2).min(axis=1)
    assert np.all(exact<=uniform+1e-12)
    plot_exact(ax,k,uniform-exact)
    style_axes(ax,xlabel=r"$\kappa$",ylabel=r"$(e_{\rm uniform}-e_0)/J_1$",zero_y=True)
    save(fig,"clock-r2/uniform-twist-error.svg")

def entry():
    fig,ax=new_figure()
    B=np.array([np.exp(2)+np.exp(1)+1,np.exp(1)])
    def solve(weights):
        def residual(m):
            v=weights*np.exp(-m)
            return m-1/(1-v/(1+v.sum()))
        sol=root(residual,np.full(len(weights),2.))
        assert sol.success and np.max(np.abs(residual(sol.x)))<1e-8
        return sol.x
    pre=solve(B[:1])[0]; post=solve(B)[0]
    x=np.arange(3)
    ax.bar(x-.18,np.array([-2,-1,0])+pre,.36,color=COLORS["accent"],label="Before")
    ax.bar(x+.18,np.array([-2,-1,0])+post,.36,color=COLORS["green"],hatch="//",label="After")
    ax.set_xticks(x,["Basic","Standard","Pro"])
    style_axes(ax,ylabel=r"$Z_i$",zero_y=True)
    style_legend(ax,loc="upper left")
    save(fig,"multiproduct-competitor-repositioning/entry-reproducible.svg")

if __name__=="__main__":
    dividing_surface()
    diffuse()
    boundary_layer()
    pendulum()
    clock_ground_state()
    entry()
