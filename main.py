import json
def one():

    f = open("products.json", mode="r", encoding="UTF8")
    k = json.load(f)
    for i in range(0, len(k["products"])):
        data = k["products"][i]
        print("Название:", data["name"], "\n", "Цена:", data["price"], "\n", "Вес:", data["weight"])
        if data["available"] == True:
            print(" В наличии")
        else:
            print(" Нет в наличии!")
    f.close()

def two():

    new_product = {}
    new_product["name"] = input("Введите название продукта: ")
    new_product["price"] = input("Введите цену продукта: ")
    new_product["weight"] = input("Введите вес продукта: ")
    available = input("Есть ли он в наличии (да/нет): ")
    if available == "да":
        new_product["available"] = True
    else:
        new_product["available"] = False

    f = open("products.json", mode="r", encoding="UTF8")
    k = json.load(f)
    k["products"].append(new_product)
    f.close()

    f = open("products.json", mode="w", encoding="UTF8")
    json.dump(k, f)
    f.close()

    f = open("products.json", mode="r", encoding="UTF8")
    k = json.load(f)
    for i in range(0, len(k["products"])):
        data = k["products"][i]
        print("Название:", data["name"], "\n", "Цена:", data["price"], "\n", "Вес:", data["weight"])
        if data["available"] == True:
            print(" В наличии")
        else:
            print(" Нет в наличии!")
    f.close()

def three():
    with open ("en-ru.txt","r") as file:
        l = file.readlines()

    d = {}

    for line in l:
        eng = line.split(" - ")[0].strip()
        ru = line.split(" - ")[1].strip().split(', ')
        for word in ru:
            if word not in d:
                d[word] = [eng]
            else:
                d[word].append(eng)
    with open("ru-en.txt","w") as file:
        for ru,eng in sorted(d.items()):
            file.write(f"{ru} - {', '.join(eng)}\n")

# one()
# two()
# three()