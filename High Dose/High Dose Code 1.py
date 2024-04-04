def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
n=int(input("Enter the no of consecutive integers : "))
x=2
found1=True
while found1:
    found=True
    fl=[]
    for i in range(x,x+n):
        l=[]
        j=2
        while j*j<=i:
            if i%j==0:
                l+=[j]
                i=i//j
            else:
                j+=1
        l+=[i]
        fl+=[l]
    for i in range(len(fl)):
        j=0
        while j<len(fl[i]):
            elem=fl[i][j]
            count=fl[i].count(elem)
            for a in range(count-1):
                fl[i].remove(elem)
            index=fl[i].index(elem)
            fl[i][index]=fl[i][index]**count
            j+=1
    while i<len(fl):
        j=i+1
        while j<len(fl):
            k=0
            while k<len(fl[j]):
                if fl[j][k] in fl[i]:
                    fl[i].remove(fl[j][k])
                k+=1
            j+=1
        i+=1
    for i in range(len(fl)):
        if len(fl[i])<n:
            break
    else:
        for z in range(x,x+n):
            print(z,end=' ')
        found1=False
    x+=1
        
            
            
