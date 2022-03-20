# @Author: Ozan YILDIZ@2022
# Assigning Multiple Values to Multiple Variables
def defineVars1():
    userName, userSurName, phone, age, salary = "Ozan", "Yildiz", "+xx xxx xxx xxx", 28, 3.2
    print("User Information\n")
    print("User Name:", userName, " ,User Surname:", userSurName, " ,Phone:", phone, " ,Age:", age, " ,Salary:", salary)


def defineVars2():
    userTitle1 = userTitle2 = userTitle3 = "Senior"
    print("First User's Title:", userTitle1, " ,Second User's Title::", userTitle2, " ,Third User's Title::",
          userTitle3)


USER_CONSTANT = "Constant_User"
if __name__ == '__main__':
    defineVars1()
    defineVars2()
