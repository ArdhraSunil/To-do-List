
list = []
def addlist():
    
    item = input("ENTER THE NEW ITEM")
    list.append(item)
    print(f"{item} added to the list")

def displayitem():
    i=len(list)
    for j in range(i):
        print(f"{j+1}) {list[j]}")
        
def removeitem():
    print("ENTER THE ITEM NO. TO REMOVE ELEMENT")
    n = int(input())
    if 0<= n< len(list):
        removed = list.pop(n)
        print("REMOVED ITEM IS "+removed)
    else:
        print("INVALID")    

print("*_*_"*5)
print("TO-DO LIST")
print("*_*_"*5)
print("1) ADD ITEM TO THE LIST")
print("2) DISPLAY LIST")
print("3) REMOVE ITEM FROM LIST")
print("4) EXIT")
while True:    
    choice = int(input("ENTER THE CHOICE"))

    if choice == 1:
        print("ADD ITEM ")
        addlist()
    elif choice == 2:
        print("DISPLAY ITEMS") 
        displayitem()   
    elif choice == 3:
        print("REMOVE ITEM FROM LIST")
        removeitem()
    elif choice == 4:
        print("EXIT")
        break
    else:
        print("INVALID CHOICE")

