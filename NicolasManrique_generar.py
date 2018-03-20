import numpy as np

def sample_1(N):                    #Funcion que recibe entero N, retorna array de N datos aleatorios segun el enunciado
    v=[-10.0,-5.0,3.0,9.0]
    pr=[0.1,0.4,0.2,0.3]
    return np.random.choice(a=v,size=N,p=pr)

def sample_2(N):                  #Funcion que recibe entero N, retorna array de N datos aleatorios que siguen distribucion exponencial con beta = 0.5
    beta=0.5
    return np.random.exponential(beta,N)

def get_mean(sampling_fun,N,M):  #Funcion que devuelve M promedios de N datos aleatorios que siguen una distribucion de probabilidad sampling_fun
    res=np.array([])
    for i in range(M):
        prom=np.sum(sampling_fun(N))/N
        res=np.append(res,prom)
    return res


N=[10,100,1000]                 #Arreglo de numero de datos

dataS1=np.array([])             #Arreglo vacio al que se adjuntaran promedios de sample_1 con N contenido en arreglo anterior
dataS2=np.array([])             #Arreglo vacio al que se adjuntaran promedios de sample_2 con N contenido en arreglo anterior

for i in N:                       #Iteracion de 10000 promedios para i muestras de sampleo
    s1=get_mean(sample_1,i,10000)
    dataS1=np.append(dataS1,s1)
    s2=get_mean(sample_2,i,10000)
    dataS2=np.append(dataS2,s2)

for i in range(3):                          #Escribe archivos de texto
    nombre1="sample_1_"+str(N[i])+".txt"
    np.savetxt(nombre1,dataS1, delimiter=',')
    nombre2="sample_2_"+str(N[i])+".txt"
    np.savetxt(nombre2,dataS2, delimiter=',')



























