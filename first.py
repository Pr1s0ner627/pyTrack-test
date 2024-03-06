def listCreate(lst,n):
    for i in range(n):
        num=int(input("Enter input : "))
        lst.append(num)
    return lst

lst=[]
lim=int(input("Enter the Limit : "))

listCreate(lst,lim)