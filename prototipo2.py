import random
import time
from timeit import default_timer

def multiplicar(): #4
    ini = default_timer()
    t = random.randint(1,100)
    for i in range(1,t):
        a = random.randint(0,100)
        b = random.randint(0,100)
        r = a * b
        time.sleep(0.2)
        print("Multiplicando:", a," * ",b," => ", r)
    fin = default_timer()
    print("Estuvo ejecutandose durante: ", fin - ini)

def dividir():  #3
    ini = default_timer()
    t = random.randint(1,100)
    for m in range (1,t):
        a = random.randint(1,100)
        b = random.randint(1,100)
        r = a / b
        time.sleep(0.2)
        print("Dividiendo:", a," / ",b, " =>",r)
    fin = default_timer()
    print("Estuvo ejecutandose durante: ", fin - ini)
        
def sumar():  #2
    ini = default_timer()
    t = random.randint(1,100)
    for n in range (1,t):
        a = random.randint(1,100)
        b = random.randint(1,100)
        r = a + b
        time.sleep(0.2)
        print("Sumando:",a," + ",b," =>", r)
    fin = default_timer()
    print("Estuvo ejecutandose durante: ", fin - ini)

def restar():  #1
    ini = default_timer()
    t = random.randint(1,100)
    for j in range (1,t):
        a = random.randint(1,100)
        b = random.randint(1,100)
        r = a - b
        time.sleep(0.2)
        print("Restando:",a," - ",b," => ", r)
    fin = default_timer()
    print("Estuvo ejecutandose durante: ", fin - ini)
        

def ejecucion():
    restar()
    sumar()
    dividir()
    multiplicar()
    
def ejecucion1():
    print("Regresando")
    multiplicar()
    dividir()
    sumar()
    restar()
    
ejecucion()
ejecucion1()
    
    

