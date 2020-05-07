class Student(object):
    __name = ""

    __age = 0

    __ID = "000001"
    def __init__(self,id,name,age):
        self.__ID = id
        self.__name = name
        self.__age = age

    def printStudent(self):
        print("name = " + self.__name + " age = " + str(self.__age))
