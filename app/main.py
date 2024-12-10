class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for peoples in people:
        Person(peoples["name"], peoples["age"])
    for peoples in people:
        result_people = Person.people[peoples["name"]]
        if "wife" in peoples and peoples["wife"] is not None:
            result_people.wife = Person.people[peoples["wife"]]

        if "husband" in peoples and peoples["husband"] is not None:
            result_people.husband = Person.people[peoples["husband"]]

    return list(Person.people.values())
