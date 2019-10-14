"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import time
import operator
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
start = time.time()
nums_call_spent = {}
for call in calls:
    for n in range(2):
        if call[n] in nums_call_spent:
            nums_call_spent[call[n]] += int(call[3])
        else:
            nums_call_spent[call[n]] = int(call[3])
max_num = max(nums_call_spent.items(), key=operator.itemgetter(1))[0]

print("{} spent the longest time, {} seconds, during September 2016"\
      .format(max_num, nums_call_spent[max_num]))
end = time.time()

print("------------------------------------------------------")
print("Executation time is {0:.2f} microsecond".format((end-start)*(10**6)))
print("------------------------------------------------------")
print("Big O notation = n^2")