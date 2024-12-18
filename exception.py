x=2
try:
    print(x)
except NameError:
    print("NameError means something probably undefined.")
except Exception as error:
    print("error")
else:
    print("No error")
finally:
    print("I'am going to print with or without an error.")
