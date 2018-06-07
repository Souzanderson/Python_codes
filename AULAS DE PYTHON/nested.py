#usando funções nested para criar um software que chama funções

#euler

def exp():
    e = 2.7182818284590452353602874713526624977572470
    print('f(x)=e^x')
    def power(x):
        a=[]
        print(x)
        for i in range(0,len(x)):
            a.append(e**x[i])
        return a
    return power

f=exp()
x=input('x = ').split()
x=(int(i) for i in x)
t=f(x)
print(t)
#print('f(%d) = %.5f' %(x,f(x)))
