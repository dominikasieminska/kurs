def Ack(m,n):

    if m==0:
        wynik = n+1

    if m>0 and n==0:
        wynik = Ack(m-1,1)

    if m>0 and n>0:
        wynik = Ack(m-1, Ack(m,n-1))
    return wynik


print (Ack(0,2))
print (Ack(2,0))
print (Ack(1,2))