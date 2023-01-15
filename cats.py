from cat import Cat

cats = [
    {
        "name": "Семён",
        "gender": "мальчик",
        "age": 5,
    }
]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(cat_obj.name)
