# Ruby's working code

class Students:
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def avg_score(self, testscore1, testscore2, testscore3):
        return (testscore1 + testscore2 + testscore3) / 3

John = Students("John", "21", "Maths")

print(f"{John.name} is {John.age} years old and he is studying {John.class_}.")
print(John.avg_score(50, 50, 50))