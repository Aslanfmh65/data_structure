"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from timeit import default_timer as timer

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

start = timer()
area_codes = []
in_banga = 0
bn = []
called_by_banga = [calls[i][1] for i in range(len(calls)) if calls[i][0][0:5]=="(080)"]
for num in called_by_banga:
    if "(" in num:
        start = num.index("(")
        end = num.index(")")
        code = num[start+1:end]
        area_codes.append(code)
        
        if code == "080":
            in_banga += 1
            bn.append(num)
            
    else:
        area_codes.append(num[:4]) ## The prefix of a mobile number is its first four digits
end = timer()

print("------------------------------------------------------")
print("Part A: The numbers called by people in Bangalore have codes:")
nums_to_print = sorted(list(set(area_codes)))
for num in nums_to_print:
    print(num)


print("------------------------------------------------------")
percent_call = float(in_banga)/len(called_by_banga)*100
print("Part B: {0:.2f} % percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore".format(percent_call))

print("------------------------------------------------------")
print("Executation time is {0:.2f} microsecond".format((end-start)))

print("------------------------------------------------------")
print("Big O notation = n")