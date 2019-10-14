"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import time

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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

start = time.time()
out_call = []
in_call = []
out_text = []
in_text = []
tele = []

out_call = [calls[i][0] for i in range(len(calls))]
in_call = [calls[i][1] for i in range(len(calls))]
out_text = [texts[i][0] for i in range(len(texts))]
in_text = [texts[i][1] for i in range(len(texts))]

for call in out_call:
    if (call not in in_call) & (call not in out_text) & (call not in in_text):
        tele.append(call)
end = time.time()

print("These numbers could be telemarketers: ")

nums_to_print = sorted(list(set(tele)))
for num in nums_to_print:
    print(num)

print("------------------------------------------------------")
print("Executation time is {0:.2f} microsecond".format((end-start)*(10**6)))
print("------------------------------------------------------")
print("Big O notation = n")