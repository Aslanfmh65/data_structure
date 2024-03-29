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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

start = time.time()

first_text = texts[0]
last_call = calls[-1]
print("First record of texts, {} texts {} at time {}".format(first_text[0], first_text[1], first_text[2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds"\
      .format(last_call[0], last_call[1], last_call[2], last_call[3]))

end = time.time()

print("------------------------------------------------------")
print("Executation time is {0:.2f} microsecond".format((end-start)*(10**6)))
print("------------------------------------------------------")
print("Big O notation = 1")