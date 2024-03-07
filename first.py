def listCreate(lst,n):
    for i in range(n):
        num=int(input("Enter input : "))
        lst.append(num)
    return lst


def listRemove(lst):
    inp=input("Delete the List [Y/N] : ")
    if inp in 'yY':
        lst.remove()
    return lst


lst=[]
lim=int(input("Enter the Limit : "))

listCreate(lst,lim)
listRemove(lst)