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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
start = time.time()
call_num = [[calls[i][ii] for i in range(len(calls))] for ii in range(2)]
text_num = [[texts[i][ii] for i in range(len(texts))] for ii in range(2)]
total_num = call_num[0]+call_num[1]+text_num[0]+text_num[1]
unique_count = len(list(set(total_num)))
end = time.time()
print("There are {} different telephone numbers in the records".format(unique_count))

print("------------------------------------------------------")
print("Executation time is {0:.2f} microsecond".format((end-start)*(10**6)))
print("------------------------------------------------------")
print("Big O notation = n^2")