def triple(x):
    return x *3

size = int (input("Enter size :"))
lst=[]
for i in range (size):
    lst_input=int(input(f"Enter your Value {i+1} :"))
    lst.append(lst_input)
print("Sample list :",lst)

res=list(map(triple,lst))
print("Tripled of list numbers :",res)