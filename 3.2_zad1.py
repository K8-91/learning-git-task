lista_zakupow={
    "piekarnia" : ["chleb", "bulki", "paczek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

print("Idę do sklepu")
for key, value in lista_zakupow.items():
    print("Idę do", key.capitalize(), "i kupuje tam", end =" ")
    capitalize_value=[]
    for element in value:
        capitalize_value.append(element.capitalize())
    print(capitalize_value)
