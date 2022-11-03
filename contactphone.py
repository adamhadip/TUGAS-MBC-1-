nohp = []
name = [] 
numbers = 3 

for k in range(numbers) : 
    yourname = input("Nama : ")
    phone_numb = int(input("No Phone : "))

    name.append(yourname)
    nohp.append(phone_numb)

print ("\n Name \t\t\t No Phone \n")

for i in range(numbers):
    print("{}\t\t\t{}".format(name[i], nohp[i]))

search_term = input("\nEnter search term: ")

print("Search result:")
if search_term in name:
    index = name.index(search_term)
    phone_number = nohp.[index]
    print("Name: {}, Phone Number: {}".format(search_term, nohp))

else:
    print("Name Not Found")