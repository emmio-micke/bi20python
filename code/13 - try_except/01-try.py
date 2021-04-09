try:
    print(1/0)
except NameError:
    print("ooups")
except ZeroDivisionError:
    print("Tried to divide a number by 0")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("This always runs")

print("hello")
