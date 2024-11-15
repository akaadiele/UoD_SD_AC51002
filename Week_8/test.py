# class MyTest:
#     name = "test_plan"



# obj = MyTest()

# print(type(obj))

# print(type(1))


# -------------
# class Triangle:
#     def __init__(self, base, height):
#         self.base= base
#         self.height = height
#     def __str__(self):
#         return f"Triangle(Base={self.base}, Height={self.height})"
    
# a = Triangle(3,5)

# print(a)

# ------------
# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")



# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")



# obj_ind = India()
# obj_usa = USA()



# for country in (obj_ind, obj_usa):
#     country.capital()



# ---------------

class Newspaper:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name



    # Newspaper.__str__()

# s=str(Newspaper)

myPaper=Newspaper("Computing Herald"); s=str(myPaper)

# s=Newspaper-__str(); str(Newspaper)

# myPaper=Newspaper("Computing Herald"); s=Newspaper.__str__()

# myPaper=Newspaper("Computing Herald"); s=myPaper.__str__()

print(s)