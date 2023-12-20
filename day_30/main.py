#FileNotFound

# try:
#     file = open("data.txt")
#     print("A")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError as error_message:
#     file = open("data.txt", "w")
#     print("B")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("this is madeup error")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 2.5 or height < 0.4:
    raise ValueError("Check You height")

bmi = weight / height ** 2
print(f"BMI= {bmi}")