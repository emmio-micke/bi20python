# test_file = open("demofile.txt", "w")
test_file = open("demofile.txt", "a")
test_file.write("Lorem ipsum")
test_file.close()


test_file = open("demofile.txt", "r")
print(test_file.read())
test_file.close()
