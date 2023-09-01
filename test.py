print ("hello world")
print("c'est bon")


def toto(n):
    x=0
    for i in range(1,n):
        x+=1
    return x


def toto2(n):
    if n%2==0:
        return True
    elif n%2==1:
        return False
