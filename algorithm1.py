def read_line_from_file(filename):
    file_object = open(filename)
    try:
        data = file_object.readline()
    finally:
        file_object.close()
    
    line_new = []
    line = data.split(',')
    for num in line:
        try:
            num = int(num)
            line_new.append(num)
        except ValueError:
            pass
    
    return line_new

filename = "1.data"
age_list = read_line_from_file(filename)
print "original:\n", age_list
print "len(list):", len(age_list)

box_depth = input("box_depth:")

''' part(1)'''
age_list1 = []
for i in range(len(age_list)/box_depth):
    result = 0
    for j in range(box_depth):
        list_index = i*box_depth + j
        result += age_list[list_index]
        age_list[list_index] = 0
    
    result = (result)/box_depth 
    result = int(round(result))
    
    for k in range(box_depth):
        age_list1.append(result)

result = 0
box_last = []
for num in age_list:
    if num != 0:
        box_last.append(num)
last_box_len = len(box_last)

for j in range(last_box_len):
    result += box_last[j]
if last_box_len > 0:
    result /= last_box_len
    for num in box_last:
        age_list1.append(result)

print "average:\n", age_list1

''' part(2)'''
age_list = read_line_from_file(filename)
age_list2 = []
for i in range(len(age_list)/box_depth):
    b = age_list[i*box_depth+box_depth/2]
    
    result = b
    
    for j in range(box_depth):
        age_list2.append(result)
        list_index = i*box_depth + j
        age_list[list_index] = 0

box_last = []
for num in age_list:
    if num != 0:
        box_last.append(num)
last_box_len = len(box_last)
if last_box_len > 0:
    result = box_last[last_box_len/2]
    for num in box_last:
        age_list2.append(result)

print "median:\n", age_list2

''' part(3)'''
age_list = read_line_from_file(filename)
age_list3 = []
for i in range(len(age_list)/box_depth):
    a = age_list[i*box_depth]
    c = age_list[i*box_depth+box_depth-1]
    
    for num in range(box_depth):
        list_index = i*box_depth + num
        b = age_list[list_index]
        if num == 0:
            age_list3.append(a)
        elif num == box_depth - 1:
            age_list3.append(c)
        else:
            if b-a > c-b:
                age_list3.append(c)
            else:
                age_list3.append(a)
        age_list[list_index] = 0

box_last = []
for num in age_list:
    if num != 0:
        box_last.append(num)
last_box_len = len(box_last)
if last_box_len > 0:
    a = box_last[0]
    c = box_last[last_box_len-1]
    for num in range(last_box_len):
        list_index = num
        b = box_last[list_index]
        if num == 0:
            age_list3.append(a)
        elif num == box_depth - 1:
            age_list3.append(c)
        else:
            if b-a > c-b:
                age_list3.append(c)
            else:
                age_list3.append(a)
            
print "border:\n", age_list3

''' Outlier '''
age_list = read_line_from_file(filename)
print 
print 'Outlier '

limit = input("limit: ")
age_list1 = []
for i in range(len(age_list)/3):
    a = age_list[i*3]
    b = age_list[i*3+1]
    c = age_list[i*3+2]
    average = (a+b+c)/3.0
    
    box = []
    box.append(a)
    box.append(b)
    box.append(c)
    for num in box:
        if num - average > limit:
            print "box", i+1, ":", num 
        













