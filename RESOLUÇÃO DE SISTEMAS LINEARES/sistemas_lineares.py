def resolve_sistema():
    n=int(input('defina o tamanho do sistema: '))
    a=[]
    c=[0 for x in range(0,n)]
    
    print("Entrada da matriz:")
    for i in range(0,n):
        a.append(input().split())
        b=a[i]
        a[i]=[int(x) for x in b]

    for k in range(0,n-1):
        for i in range(k+1,n):
            for j in range(k+1,n+1):
                a[i][j]=a[k][k]*a[i][j]-a[i][k]*a[k][j]
                if j==n: a[i][k]=0

    for i in range(n-1,-1,-1):
        c[i]=a[i][n]
        for j in range(n-1,i,-1):
            c[i]=c[i]-a[i][j]*c[j]
        c[i]=c[i]/a[i][i]

    print('\n')
    for i in range(0,len(c)):
        print('X%d = %.4f' %(i+1,c[i]))
                
resolve_sistema()
