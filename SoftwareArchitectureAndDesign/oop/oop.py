## Classes
# Structuring data
import numpy as np


# data = np.array([[1., 2., 3.],
#                  [4., 5., 6.]])
#
# patients = [
#     {
#         "name": "Alice",
#         "data": [1., 2., 3.],
#     },
#     {
#         "name": "Bob",
#         "data": [4., 5., 6.],
#     }
# ]
#
#
# def attach_name(data, names):
#     patients_list = []
#
#     if len(data) != len(names):
#         raise Exception("Data and names must have the same length")
#
#     for i in range(len(data)):
#         patient_data = {"name": names[i], "data": data[i]}
#         patients_list.append(patient_data)
#
#     return patients_list
#
#
# def attach_name1(data, names):
#     """Create data structure containing patient records."""
#     output = []
#     for i in range(len(data)):
#         output.append({"name": names[i],
#                        "data": data[i]})
#
#     return output
#
#
# output = attach_name(data, ["Alice", "Bob"])
# print(output)
#
# output1 = attach_name1(data, ["Alice", "Bob"])
# print(output1)
#
# def attach_name2(data, names):
#     """Create data structure containing patient records."""
#     assert len(data) == len(names)
#     output = []
#
#     for data_row, name in zip(data, names):
#         output.append({"name": name,
#                        "data": data_row})
#
#     return output
#
# output2 = attach_name2(data, ["Alice", "Bob"])
# print(output2)
#
# # Classes in Python
#
# my_list = [1,2,3]
# my_dict = {'a':1,'b':2,'c':3}
# my_set = {1,2,3}
#
# print(type(my_list))
# print(type(my_dict))
# print(type(my_set))

# Encapsulating data
#
# class Patient:
#     def __init__(self, name):
#         self.name = name
#         self.observations = []
#
# alice = Patient('Alice')
# print(alice.name)

# Encapsulating behaviour
#
# class Patient:
#     """a patient in an inflammation study."""
#     def __init__(self, name):
#         self.name = name
#         self.observations = []
#
#     def add_observation(self, value, day=None):
#         if day is None:
#             try:
#                 day = self.observations[-1]["day"] + 1
#
#             except IndexError:
#                 day = 0
#
#         new_observation = {
#             "day": day,
#             "value": value,
#         }
#
#         self.observations.append(new_observation)
#         return new_observation
#
#     def __str__(self):
#         return self.name
#
#     @property
#     def last_observation(self):
#         return self.observations[-1]

# alice = Patient("Alice")
# print(alice)
#
# observation = alice.add_observation(3)
# print(observation)
# print(alice.observations)

# Class and Static Methods

# Dunder methods

# A Basic Class
# class Book:
#     """A class to represent a book."""
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#
#     def __str__(self):
#         return self.title + " by " + self.author

# book = Book("A Book", "Me")
# print(book)

# Properties
# alice = Patient("Alice")
#
# alice.add_observation(3)
# alice.add_observation(4)
#
# obs = alice.last_observation
# print(obs)
#

################################################################
## Inheritance and Composition
# Relationships between classes
# class Observation:
#     def __init__(self, day, value):
#         self.day = day
#         self.value = value
#
#     def __str__(self):
#         return str(self.value)
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# class Patient(Person):
#     """A patient in an inflammation study."""
#
#     def __init__(self, name):
#         super().__init__(name)
#         self.observations = []
#
#     def add_observation(self, value, day=None):
#         if day is None:
#             try:
#                 day = self.observations[-1].day + 1
#             except IndexError:
#                 day = 0
#
#         new_observation = Observation(day, value)
#
#         self.observations.append(new_observation)
#         return new_observation


# alice = Patient("Alice")
# print(alice)
#
# obs = alice.add_observation(3)
# print(obs)


# Inheritance
# bob = Person("Bob")
# print(bob)

# obs = bob.add_observation(4) # AttributeError: 'Person' object has no attribute 'add_observation'
# print(obs)

# Mixin classes

# class NameMixin:
#     def __str__(self):
#         return self.name
#
#
# class PatientWithMixin(NameMixin):
#     def __init__(self, name):
#         self.name = name
# No need to redefine __str__ here, it will use the mixin's method


# print(PatientWithMixin("Sevada"))

# Composition vs Inheritance
# class Machine:
#     pass
#
# class Printer(Machine):
#     pass
#
# class Scanner(Machine):
#     pass
#
# class Copier(Printer, Scanner):
#     # Copier is a Printer and is a Scanner
#     pass
#
# class Machine:
#     pass
#
#
# class Printer(Machine):
#     pass
#
#
# class Scanner(Machine):
#     pass
#
#
# class Copier:
#     def __init__(self):
#         # Copier has a Printer and has a Scanner
#         self.printer = Printer()
#         self.scanner = Scanner()


# Multiple Inheritance
# """Tests for the Patient model"""
#
#
# def test_create_patient():
#     """Check a patient is created correctly given a name."""
#     from inflammation.models import Patient
#     name = "Alice"
#     p = Patient(name=name)
#     assert p.name == name
#
#
# def test_create_doctor():
#     """Check a doctor is created correctly given a name."""
#     from inflammation.models import Doctor
#     name = "Sheila Wheels"
#     doctor = Doctor(name=name)
#     assert doctor.name == name
#
#
# def test_doctor_is_person():
#     """Check if a doctor is a person."""
#     from inflammation.models import Doctor, Person
#     doctor = Doctor("Sheila Wheels")
#     assert isinstance(doctor, Person)
#
#
# def test_patient_is_person():
#     """Check if a patient is a person."""
#     from inflammation.models import Patient, Person
#     patient = Patient("Alice")
#     assert isinstance(patient, Person)
#
#
# def test_patients_added_correctly():
#     """Check patients are being added correctly by a doctor."""
#     from inflammation.models import Patient, Doctor
#     doc = Doctor("Sheila Wheels")
#     patient = Patient("Alice")
#     doc.add_patient(patient)
#     assert doc.patients is not None
#     assert len(doc.patients) == 1
#
#
# def test_no_duplicate_patients():
#     """Check adding the same patient to the same doctor twice does not result in duplicates."""
#     from inflammation.models import Patient, Doctor
#     doc = Doctor("Sheila Wheels")
#     alice = Patient("Alice")
#     doc.add_patient(alice)
#     doc.add_patient(alice)
#     assert len(doc.patients) == 1
#
#
# class Person:
#     """A person."""
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# class Patient(Person):
#     """A patient in an inflammation study."""
#
#     def __init__(self, name):
#         super().__init__(name)
#         self.observations = []
#
#     def add_observation(self, value, day=None):
#         if day is None:
#             try:
#                 day = self.observations[-1].day + 1
#             except IndexError:
#                 day = 0
#
#         new_observation = Observation(day, value)
#         self.observations.append(new_observation)
#         return new_observation
#
#
# class Doctor(Person):
#     """A doctor in an inflammation study."""
#
#     def __init__(self, name):
#         super().__init__(name)
#         self.patients = []
#
#     def add_patient(self, new_patient):
#         # A crude check by name if this patient is already looked after
#         # by this doctor before adding them
#         for patient in self.patients:
#             if patient.name == new_patient.name:
#                 return
#         self.patients.append(new_patient)
#
#

####################################################################################
## Polymorphism

class Person:
    """A person."""

    def __init__(self, name):
        self.name = name
        self.id = None

    def __str__(self):
        return self.name

    def set_id(self, id):
        raise NotImplementedError("set_id not implemented")

    def get_id(self):
        return self.id


class Patient(Person):
    """A patient in an inflammation study."""

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "Patient: " + super().__str__()

    def set_id(self, id):
        self.id = "P" + str(id).zfill(4)


class Doctor(Person):
    """A doctor in an inflammation study."""

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "Doctor: " + super().__str__()

    def set_id(self, id):
        self.id = "D" + str(id).zfill(4)


alice = Doctor("Alice")
bob = Patient("Bob")
alice.set_id(1)
bob.set_id(1)
print(alice)
print(bob)

people = [alice, bob]
for person in people:
    print(person)


class Administrator:
    """An administrator in an inflammation study."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Administrator: " + self.name

    def set_id(self, id):
        self.id = "A" + str(id).zfill(4)

    def get_id(self):
        return self.id


# A trial full of People
class Trial:
    """A trial full of people."""

    def __init__(self):
        self.people = []

    def add_person(self, person):
        if isinstance(person, Person):
            self.people.append(person)
        elif hasattr(person, "get_id"):
            person_id = person.get_id()
            if person_id[0] == "D":
                person = Doctor(person_id)
            elif person_id[0] == "P":
                person = Patient(person_id)
            elif person_id[0] == "A":
                person = Administrator(person_id)
            else:
                raise TypeError("could not recognise person id, should start with D, P or A.")
            self.people.append(person)
        else:
            raise TypeError("person must be of type Person or have a get_id method.")

    def print_people(self):
        for person in self.people:
            print(person)

    def set_id(self, id):
        for i, person in enumerate(self.people):
            person.set_id(i + 1)
