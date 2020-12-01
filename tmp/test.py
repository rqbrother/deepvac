


class test(object):
    def __init__(self, age, grade):
        self.age = age
        self.grade = grade
        self.init(120)

    def init(self, num):
        self.num = num

student = test(10, 90)
# student.init(120)
print(student.__dict__)