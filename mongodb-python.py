import pymongo

def work_with_mongo():
    conn = pymongo.Connection('localhost', 27017)
    db = conn.mydb
    coll = db.mycoll
    doc = {"name": "Петр", "surname": "Иванов"}
    coll.save(doc)

    for men in coll.find():
        print(men)

    # выводим фамилии людей с именем Петр
    for men in coll.find({"name": "Иван"}):
        print(men["surname"])

    # подсчет количества людей с именем Петр
    print(coll.find({"name": "Петр"}).count())

    # добавляем ко всем документам новое поле sex - пол
    coll.update({}, {"$set": {"sex": "мужской"}})

    for men in coll.find():
        print(men)

    # всем Петрам делаем фамилию Новосельцев и возраст 25 лет
    coll.update({"name": "Петр"}, {"surname": "Новосельцев", "age": 25})

    for men in coll.find():
        print(men)

    # увеличиваем всем Петрам возраст на 5 лет
    coll.update({"name": "Петр"}, {"$inc": {"age": 5}})

    for men in coll.find():
        print(men)

    # сбрасываем у всех документов поле name
    coll.update({}, {"$unset": {"name": 1}})

    for men in coll.find():
        print(men)

    # удаляем все документы коллекции
    coll.remove({})

    for men in coll.find():
        print(men)


if __name__ == '__main__':
    work_with_mongo()
