# basics of python assignment

listOfNumbers = input("Enter numbers separated by spaces: ")

# split by whitespace, create list of strings
numberList = listOfNumbers.split()
# print(numberList)

# utilize list comprehension: first arg is action or each item, num is iteration variable (like i) in numberList points to list
# for each number in the string list, change "number" to integer
numberListInit = [int(num) for num in numberList]

# calculate max, min, average

maxValue = max(numberListInit)
minValue = min(numberListInit)
avgValue = sum(numberListInit) / len(numberListInit)


# print
print("STATS for LIST...")
print("AVERAGE VALUE IS: " + str(avgValue))
print("MAX VALUE IS: " + str(maxValue))
print("MIN VALUE IS: " + str(minValue))



# pretty basic, but learned spliting by white space function, list behavior and list comprehension