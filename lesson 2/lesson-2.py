contact_information = {
    "Amar":{
        "phone_number": "123-123",
        "email" : "amar@gmail.com",
        "home_adress" : "bregu i diellit",
        "birthday" : "03/02/2003"
    },

    "Filani": {
        "phone_number": "123-321",
        "email": "filanfisteku@gmail.com",
        "home_adress": "qaty dikun",
        "birthday": "08/09/1998"
    },
    "Hasani": {
        "phone_number": "123-131",
        "email": "hasani@gmail.com",
        "home_adress": "qaty dikun",
        "birthday": "19/08/1997"
    }
}

print(contact_information)


amar_information = contact_information["Amar"]
print(amar_information)

contacts = {
    "Amar" : ("123-123","amar@gmail.com"),
    "Filani" : ("123-321","filanfisteku@gmail.com"),
    "Hasani" : ("123-131","hasani@gmail.com")
}

amar_info = contacts["Amar"]
phone_number = amar_info[0]
print(phone_number)
email = amar_info[1]
print(email)


phone_number, email = contacts["Amar"]