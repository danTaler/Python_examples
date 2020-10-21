#------------------------------------------------------
#  Example 1
#
people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Cho", "house":"Rav"},
    {"name":"Drac", "house":"Sly"}
]

def f(y):
    return y["name"]

people.sort(key=f)

#print(people)

#------------------------------------------------------
#  Example 2
#           Convert this function into a lambda:
people = ['Dr. Christopher Brooks', 
        'Dr. Kevyn Collins-Thompson', 
        'Dr. VG Vinod Vydiswaran', 
        'Dr. Daniel Romero']

def split_title_and_name(person):
    #print(person.split()[0] + ' ' + person.split()[-1])
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    myfunc = lambda person:split_title_and_name(person)
    #print(myfunc(person))
    print(split_title_and_name(person) == (myfunc(person)))

#option 2
p = (people[0])
myfunc = lambda people:split_title_and_name(people)
#print(myfunc(people))
#print(list(map(split_title_and_name, people)))

t = list(map(split_title_and_name, people)) == list(map(myfunc,people))
print(t)





#option 1
for person in people:
    print( (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))