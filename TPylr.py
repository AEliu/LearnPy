class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return ("{} is {} years old!".format(self.name, self.age))
    __repr__ = __str__
    def __del__(self):
        print('Oop! I died!')
    def __getattr__(self, item):
        if item == 'sex':
            print("{} is a boy!".format(self.name))
        raise AttributeError('has no this attr')
    def __setattr__(self, key, value):
        pass


xming = student('Xiao ming', 18)
print(xming)
xming.sex
xming.diao = 4
del xming
