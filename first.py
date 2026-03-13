# print("hello")
# a = 10
# b = 20
# print(a + b)
# print("A :", a)
# print("B :", b)
# print(type(a))

# c = str(a)
# print(type(c))

# name = input("Enter name: ")
# print("Hello :", name)


# Age = int(input("Enter Your age :"))
# print("Your age is :-", Age)
# Name = input("Enter your name :-")
# Age = int(input("Your age is :"))
# city = input("Your city is :-")

# print("Name:-", Name)
# print("Age:-", Age)
# print("City:-", city)


# num1 = int(input("Enter a first num:-"))
# num2 = int(input("Enter s Second num:-"))

# num3 = num1 + num2
# print(num3)


# a = 10
# b = 20

# print(a > b)
# a *= 2
# print(a)


# name = "Surya"
# print("S" in name)

# num = int(input("Enter a num:"))

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Example usage
# print(factorial(5))  # Output: 120


# num = int(input("Enter a num:-"))

# if num > 50:
#     print("Number is greater than 50")
# elif num == 50:
#     print("Number is equal to 50")
# else:
#     print("Number is less than 50")


# Grade = int(input("Enter marks:-"))

# if Grade >= 90:
#     print("Grade is A+")

# elif Grade >= 70:
#     print("Grade is A")

# elif Grade >= 50:
#     print("Grade is B")

# elif Grade >= 33:
#     print("Grade is C")
# else:
#     print("Fail")


# for i in range(1, 11):
#     print(i * 2)


# for i in range(1, 11):
#     print(i * 3)


# i = 1

# while i < 10:
#     print(i)
#     i += 1


# for i in range(1, 21):
#     print(i)

# for i in range(2, 51, 2):
#     print(i)


# for i in range(1, 11):
#     print(i * 7)


# total = 0

# for i in range(1, 11):
#     total = total + i

# print("Sum =", total)

# total = 0

# for i in range(1, 101):
#     total = total + i
#     # print("Sum :-", total)

# print("Sum :-", total)

# total = 0

# for i in range(2, 51, 2):
#     total = total + i

# print("Total sum :-", total)


# for i in range(1, 10):
#     print("*" * i)


# for i in range(10, 0, -1):
#     print("*" * i)

# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*" * j)


# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
# def sum(a, b):
#     return a + b


# c = sum(9, 6)
# print(c)


# def sum(a, b):
#     print(a + b)


# sum(6, 7)


# def hell():
#     print("helo surya")


# hell()


# def sumoftwo():
#     a = 10
#     b = 20

#     return a + b


# print(sumoftwo())
# def twonum(a, b):
#     return a + b


# a = int(input("Enter a number:-"))
# b = int(input("Enter b number:-"))

# c = twonum(a, b)
# print(c)


# def multi(a, b):
#     return a * b


# print(multi(2, 3))


# def checkodd(a):
#     if a % 2 == 0:
#         print("Even")
#     else:
#         print("odd")
#     return a


# a = int(input("Enter a num:-"))
# b = checkodd(a)


# def squ(a):
#     return a * a
# a = int(input("Enter a num:-"))
# c = squ(a)
# print(c)


# def large(a, b):
#     if a > b:
#         print("A is greater than B")
#     else:
#         print("B is greater than A")


# a = int(input("Enter a num:-"))
# b = int(input("Enter b num:-"))

# c = large(a, b)
# print(c)


# def largest_three(a, b, c):

#     if a > b and a > c:
#         print("A is greatest")

#     elif b > a and b > c:
#         print("B is greatest")

#     else:
#         print("C is greatest")


# a = int(input("Enter a num:-"))
# b = int(input("Enter b num:-"))
# c = int(input("Enter c num:-"))

# largest_three(a, b, c)

# num = [10, 20, 30, 40]
# for i in num:
#     print(i)

# a = [1, 2, 8, 4]
# # print(a[1])
# # print(a[2:4])
# # print(1 in a)
# print(max(a))
# b = 0
# for i in a:
#     b = b + i

# print(b)

# a = [20, 30, 40, 60]
# print(max(a))
# print(min(a))
b = 0
# for i in a:
#     b = b + i
# print(b)

# for i in a:
#     b = b + i
#     c = b
#     d = b / 4
# print(d)


# num = [10, 15, 20, 25, 30]
# count = 0
# for i in num:
#     if i % 2 == 0:
#         count = count + 1
# print(count)
# function to calculate factorial


list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = []

for i in list1:
    merged.append(i)

for j in list2:
    merged.append(j)

print(merged)
