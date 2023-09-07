from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
	
	@abstractstaticmethod
	def person_method():
		""" Interface Method """
	

class Student(IPerson):

	def __init__(self):
		self.name = "Default Student"
	
	def person_method(self):
		print('I am a student')


class Teacher(IPerson):

	def __init__(self):
		self.name = "Default Teacher"
	
	def person_method(self):
		print("I am a teacher")


class PersonFactory:

	@staticmethod
	def build_person(person_type):
		if person_type.lower() == 'student':
			return Student()
		elif person_type.lower() == 'teacher':
			return Teacher()
		raise Exception('Invalid person type')


if __name__ == '__main__':
	choice = input("Choose person type (student/teacher): ")
	person1 = PersonFactory.build_person(choice)
	person1.person_method()