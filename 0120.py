# 10.1
# class Thing():
#     pass
# print(Thing)
#
# class Thing():
#     pass
# example = Thing()
# print(Thing)



#10.2
# class Thing2():
#      pass
# example=Thing2()
# example.letters = "abc"
# print(Thing2)


# 10.3
# class Thing3:
#     def __init__(self, letters):
#         self.letters = letters
#
# cat = Thing3('xyz')
# print(cat.letters)

# class Element:
#     def __init__(self,name):
#         self.__name__ = name
# name = Element('Hydrogen')


class element():
    def __init__(self, name, symbol, number):
        self.__name__=name
        self.__symbol__=symbol
        self.__number__=number

    def __str__(self):
        f = ('Hydrogen', 'H', 1)
        return ('Hydrogen', 'H', 1)

inst = element('Hydrogen', 'H', 1)
print(inst)
