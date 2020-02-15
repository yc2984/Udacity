# Sam records when they wake up every morning. Assuming Sam always wakes up in the same hour, use bubble sort to sort by earliest to latest.
wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]

def bubble_sort_1(l): # [Yay]
#     # TODO: Implement bubble sort solution
    for i in range(len(l) - 1):  # index 0, len(l) - 1
        for j in range(len(l) - 1):
            first = l[j]
            second = l[j + 1]
            if first > second:  # switch
                l[j] = second
                l[j + 1] = first
    return l


bubble_sort_1(wakeup_times)
print(bubble_sort_1(wakeup_times))
print ("Pass" if (wakeup_times[0] == 3) else "Fail")


# Sam doesn't always go to sleep in the same hour. Given the following times Sam has gone to sleep, sort the times from latest to earliest.

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l): # [Yay]
    # TODO: Implement bubble sort solution

    for i in range(len(l) - 1):  # index 0, len(l) - 1
        for j in range(len(l) - 1):
            first = l[j]
            second = l[j + 1]
            if first[0] < second[0] or (first[0] == second[0] and first[1] < second[1]):  # switch when the hour is bigger or when hour is the same and minute is bigger
                l[j] = second
                l[j + 1] = first

    return l

print(bubble_sort_2(sleep_times))
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")