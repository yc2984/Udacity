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

telemarketers = []
out_going_numbers = set([call[0] for call in calls])

incoming_numbers = set([call[1] for call in calls])
out_going_text_numbers = set([text[0] for text in texts])
incoming_text_numbers = set([text[1] for text in texts])

for number in out_going_numbers:
    if (number not in incoming_numbers) and (number not in out_going_text_numbers) and (number not in incoming_text_numbers):
        telemarketers.append(number)
telemarketers.sort()

print ("These numbers could be telemarketers: ")
print("\n".join(telemarketers))
    
    
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

