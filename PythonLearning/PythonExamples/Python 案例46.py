class Student:
    def __init__(self, name):
        self.name = name
        self.courses = set()

    def enroll(self, course):
        self.courses.add(course)

    def drop(self, course):
        self.courses.remove(course)

    def show_courses(self):
        print(f'{self.name} 选择的课程如下：')
        for course in self.courses:
            print(course)


# 创建学生
imaitian = Student('imaitian')
immmmmmt = Student('immmmmmt')

# 创建课程集合
courses = {"Math", "English", "Science", "History"}

# 学生选课
imaitian.enroll('Math')
imaitian.enroll('History')
immmmmmt.enroll('English')
immmmmmt.enroll('Science')

# 显示学生选课情况
imaitian.show_courses()
immmmmmt.show_courses()

# 学生退课
imaitian.drop('Math')

# 显示学生最新选课情况
imaitian.show_courses()

