"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

from collections import defaultdict
calling_duration_dict = defaultdict(int)
for call in calls:
    caller, receiver, seconds = call[0], call[1], int(call[-1])
    calling_duration_dict[caller] += seconds
    calling_duration_dict[receiver] += seconds

number_with_longest_time = max(calling_duration_dict, key=calling_duration_dict.get)
longest_calling_time = calling_duration_dict[number_with_longest_time]
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number_with_longest_time, str(longest_calling_time)))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

