min_sup = 0
min_conf = 0
trans = 0
original_data = []

def read_lines_from_file(filename):
    file_object = open(filename)
    try:
        list_of_all_the_lines = file_object.readlines()
    finally:
        file_object.close()
            
    return list_of_all_the_lines

def handle_input(list_of_all_the_lines):
    global min_sup, min_conf, trans
    data = []
    trans = len(list_of_all_the_lines) - 1
    for i, line in enumerate(list_of_all_the_lines):
        line = line.replace('\n', '')
        line = line.replace(',', '')
        line = line.split()
        if i==0:
            min_sup = float(line[0])
            min_conf = float(line[1])
        else:
            line_tmp = []
            for num in line:
                line_tmp.append(int(num))
            data.append(set(line_tmp))
    
    return  data

original_data = handle_input(read_lines_from_file("2.data"))
Trans_len = len(original_data)
print original_data
print "min_sup", min_sup
print "min_conf", min_conf
print "dimension:"
dimension = input()

def create_L(C):
    C_tmp= {}
    for item in C:
        if C[item] >= min_sup * trans:
            C_tmp[item] = C[item]
    return C_tmp

def scan_for_support(items):
    sum = 0
    in_tmp = 0
    for  trans in original_data:
        for item in items:
            if item not in trans:
                in_tmp += 1
        if in_tmp == 0:
            sum += 1
        in_tmp = 0
    return sum

def create_C1(dataSet):
    C1 = {}
    C1_items = set([])
    for item in dataSet:
        C1_items = C1_items.union(item)
    for item in C1_items:  
        C1[item] = scan_for_support([item])
        
    return C1


def create_C(L2, rank):
    C3 = {}
    cut_C = []
    cut_C_tmp = []
    items = L2.keys()
    for i in range(len(items)):
        for j in range(len(items)):
            if j > i:
                if type(items[i]) == int:
                    cut_C.append([items[i], items[j]])
                else:
                    cut_C.append(set(items[i]).union(set(items[j])))  
                                     
    for item in cut_C:
        item_sum = cut_C.count(item)
        cal_sum = (rank-1 + 1)*(rank-1)/2 
        if item_sum == cal_sum and len(item) == rank:
            cut_C_tmp.append(item)  
    for items in cut_C_tmp:
        C3[tuple(items)] = scan_for_support(list(items))           
    return C3


C1 = create_C1(original_data) 
L = create_L(C1)
print "L1: ", L    

if dimension > 1:
    for i in range(dimension - 1):
        C = create_C(L, i+2) 
        L = create_L(C)
        print "L"+str(i+2)+": ", L












