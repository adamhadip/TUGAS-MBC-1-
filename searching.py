if search_term in name:
    index = name.index(search_term)
    phone_number = nohp.[index]
    print("Name: {}, Phone Number: {}".format(search_term, nohp))

else:
    print("Name Not Found")