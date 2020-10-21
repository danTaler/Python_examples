
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

#times_tables() == [x for x in range(10) y for y in range(10)]



number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)


time = [[x for x in range(10)] for y in range(10)]
print(time)