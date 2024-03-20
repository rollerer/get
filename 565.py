K=int(input())
num=-1
kol=0
n=int(input())
kolik=n
N = [int(i) for i in input().split()]
while kol <=n-1:
    kol+=1
    num=-1
    while num<n-kol:
        num+=1
        wer=0
        suma=0
        number = num
        while wer<kol:
            suma += N[number]
            number+=1
            wer+=1
        if suma==K and kol< kolik:
            kolik=kol
            
print(kol)
