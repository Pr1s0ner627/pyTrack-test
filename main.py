import first

print("Welcome to User App")

print("Make your Pick - ")
print("1. Create")
print("2. Read")
print("3. Update")
print("4. Delete")

chc=int(input("Enter your Choice : "))

if chc==1:
    lst=[]
    lim=int(input("Enter the Limit : "))
    first.listCreate(lst,lim)

if chc==2:
    print("Finalised result : ", lst)

if chc==3:
    first.listUpdate(lst,lim)


if chc==4:
    first.listRemove(lst)



