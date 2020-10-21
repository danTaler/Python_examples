import re

text = "This is a good day"

#search looks for some pattern and returns BOOLEAN
if re.search("good",text):
    print("found")
else:
    print("Not found")

#the findall() and split() functions will parse the string for us and return chunks:
text = "Amy works diligently. Amy gets good grades. Our student Amy is successful."
result = re.split("Amy",text)
print(result)

# Find all occurances 
result = re.findall("Amy",text)
print(result)

#complex patters, finding patterns
# 
print(re.search("^Amy",text))


sometext = "asd adfdghtdx sfgdhgtd edit"
print(re.findall("[\w ]*edit",sometext))

#Groups:
for t in re.findall("[\w ]*edit",sometext):
    print(re.split("...",t)[0])

#for item in re.finditer("",sometext):
#    print(item.group(1))
   




# https://www.coursera.org/learn/python-data-analysis/programming/4Wy6F/lab

# assignment1
#----------------------------------------
# Part A
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    result = re.findall("Amy|Mary|Ruth|Peter",simple_string)
    return result
    raise NotImplementedError()

assert len(names()) == 4, "There are four names in the simple_string"

# Part B
'''
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()
        
        #Ronald Mayr: A
        #Simon Loidl: B 
        #Bell Kassulke
        #Simon Loidl
        
        #print(re.split('\s+',grades))
        return re.findall("\w+\s\w+: B",grades)

    raise NotImplementedError()

assert len(grades()) == 16
'''

print('-------------Part C ----------\n')
# Part C
def logs():
    mylist = []
    counter = 0
    with open("logdata.txt", "r") as file:
        logdata = file.readline()
        print(type(logdata))
        #146.204.224.152 - feest6811 [21/Jun/2019:15:45:24 -0700] "POST /incentivize HTTP/1.1" 302 4622
        
        while logdata:
            log_list = (re.split("\s",logdata))
            mydict= {}
            mydict['host'] = log_list[0]
            mydict['user_name'] = log_list[2]
            #remove '[' ']'
            str_with_brackets = (' '.join(log_list[3:5]))   # 'time': '[21/Jun/2019:15:45:24 -0700]'
            mydict['time'] = str_with_brackets[1:-1]
            
            str_with_quotes =  (' '.join(log_list[5:8])) 
            mydict['request'] = str_with_quotes[1:-1]                  #'request': ['"POST', '/incentivize', 'HTTP/1.1"']
            #print(mydict)
            mylist.append(mydict)
            counter = counter +1
            logdata = file.readline()
        print(counter)
    return mylist
    raise NotImplementedError()

assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"
