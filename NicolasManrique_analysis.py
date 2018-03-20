import numpy as np
import scipy.optimize.curve_fit as spc

def normal_dist(x,mean,sigma):
    y=(1.0/(sigma*np.sqrt(2.0*np.pi)))*np.exp(-((x-mean)*(x-mean))/(2.0*sigma*sigma))
    return y



def get_fit(nombre):
    datos=np.genfromtxt(nombre)
    freqs,bins=np.histogram(datos,normed=true)
    x=0.5*(bins[:-1]+bins[1:])
    
