import AnalyzeTools.MACD as macd
import AnalyzeTools.MA as ma

dic = {0:["0","1"],1:["1","2"]}
print(dic[0])
dic[0].append("2")
print(dic)
dic[0].remove("0")
print(dic)


class Student:
    __name = None

    __age = 0

    __ID = 0

    def __init__(self,name,age,id):
        self.__age = age
        self.__name = name
        self.__ID = id

    def print_dic(self):
        print(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


frank = Student("frank",42,1)
frank.print_dic()

students = [frank]
frank1 = Student("frank",42,1)
print(students.__contains__(frank1))



