"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

unique_1 = set([text[0] for text in texts])
unique_2 = set([text[1] for text in texts])
unique_3 = set([call[0] for call in calls])
unique_4 = set([call[1] for call in calls])

unique = set(list(unique_1) + list(unique_2) + list(unique_3) + list(unique_4))

print("There are {} different telephone numbers in the records".format(len(unique)))


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
