names = input("please enter a list of names separated by space: ")# get and process input for a list of names
assignments = input("please enter a list of # of assignments separated by space: ") # get and process input for a list of the number of assignments
grades =  input("please enter a list of # of grades separated by space: ") # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
convert_to_list = lambda x: list(x.split(' '))
names, assignments, grades = convert_to_list(names), convert_to_list(assignments), convert_to_list(grades)
print("Length of names :" + str(len(names)))
print("Length of assignments :" + str(len(assignments)))
print("Length of grades :" + str(len(grades)))
for name, assignment, grade in zip(names, assignments, grades):
    print("name: ", name)
    print("# assignment: ", str(assignment))
    print('grade: ', str(grade))
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n".format(name, str(assignment), grade, int(grade)+int(assignment)*2)
    print(message)
# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
