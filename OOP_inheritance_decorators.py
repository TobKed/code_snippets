# OOP inheritance
# decorators: getters, setters, deleters


class Person(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    @property
    def email(self):
        return '{}.{}@regular.com'.format(self.first, self.last)

    def reveal_identity(self):
        print("My name is {}".format(self.first))

    def __repr__(self):
        return "Person({}, {})".format(self.first, self.last)

    def __str__(self):
        return "Person: {}, {}".format(self.fullname, self.email)


class SuperHero(Person):
    def __init__(self, first, last, hero_name):
        # super(SuperHero, self).__init__(name)     # Python 2
        super().__init__(first, last)                       # Python 3
        self.hero_name = hero_name

    @property
    def email(self):
        return '{}.{}@superhero.com'.format(self.first, self.last)

    def reveal_identity(self):
        # super(SuperHero, self).reveal_identity()  # Python 2
        super().reveal_identity()                   # Python 3
        print("...And I am {}".format(self.hero_name))

    def __repr__(self):
        return "Person({}, {}, {})".format(self.first, self.last, self.hero_name)

    def __str__(self):
        return "{}. Superhero {}".format(super().__str__(), self.hero_name)


print('> Creating first person')
jan = Person('Jan', 'Kowalski')
print('print:\t', jan)
print('str:\t', str(jan))
print('repr:\t', repr(jan))
print('mail:\t', jan.email)
print('> reveal_identity:')
jan.reveal_identity()
print('fullname:\t', jan.fullname)
print('email:\t', jan.email)
print('> change name')
jan.fullname = "John Smith"
print('print', jan)
print('> reveal_identity:')
jan.reveal_identity()
print('> delete fullname')
del jan.fullname

print()
print('> Creating first superhero')
clark = SuperHero('Clark', 'Kent', 'Superman')
print('print:\t', clark)
print('str:\t', str(clark))
print('repr:\t', repr(clark))
print('mail:\t', clark.email)
print('> reveal_identity:')
clark.reveal_identity()
print('fullname:\t', clark.fullname)
print('email:\t', clark.email)
print('> change name')
clark.fullname = "Bruce Wayne"
print('print', clark)
print('> reveal_identity:')
clark.reveal_identity()
print('> delete fullname')
del clark.fullname
