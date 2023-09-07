from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface method """
    

class Person(IPerson):

    def person_method(self):
        print('I am a person')


class ProxyPerson(Person):

    def __init__(self):
        self.person = Person()
    
    def person_method(self):
        print("Proxy functionality added ...")
        return self.person.person_method()
    

if __name__ == '__main__':
    p1 = ProxyPerson()
    p1.person_method()