def listCreate(lst,n):
    for i in range(n):
        num=int(input("Enter input : "))
        lst.append(num)
    return lst


def listRemove(lst):
    inp=input("Delete the List [Y/N] : ")
    if inp in 'yY':
        lst.remove()
    else:
        pass

def listUpdate(lst,lim):
    inp=input("Want to update the value : ")
    if inp in 'yY':
        idx=int(input("Enter the Position you want to update : "))
        while(idx>=lim):
            print("Try Again!")
        else:
            num=int(input("Enter input : "))
            lst[idx]=num

    else:
        pass
    return lst


lst=[]
lim=int(input("Enter the Limit : "))

listCreate(lst,lim)
listRemove(lst)
listUpdate(lst,lim)

print("Finalised result : ", lst)
