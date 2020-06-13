from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.JsonFomatterModule.JsonTest.Entities.Person import Person


class Test:
    @staticmethod
    def serialize_test():
        person: Person = Person(13, "Max")
        json = JsonFormatter.serialize(person)
        person_val = JsonFormatter.deserialize(json, Person)
        print(person_val)


if __name__ == '__main__':
    Test.serialize_test()
