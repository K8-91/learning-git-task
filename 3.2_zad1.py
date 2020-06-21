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

products_q=[]
for key, value in lista_zakupow.items():
    products_q.append(len(lista_zakupow[key]))
print("W sumie kupuje", sum(quantity for quantity in products_q), "produktow")

print(lista_zakupow["piekarnia"])
