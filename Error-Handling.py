def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print ("Zero division is not defined")

print(divide(1, 0))
print("End of program")