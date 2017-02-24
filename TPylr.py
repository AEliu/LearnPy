class studen():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return ("{} is {} years old!".format(self.name, self.age))
    def __del__(self):
        print('Oop! I died!')

xming = studen('Xiao ming', 18)
print(xming)
del xming