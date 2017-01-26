import csv

print('\nPart 1')
new_data_dict = {}
with open("gradebook.csv", "r") as data_file:
    data = csv.DictReader(data_file, delimiter = ",")
    for row in data:
        item = new_data_dict.get(row['Student'], dict())
        item['Assn 1'] = float(row['Assn 1'])
        item['Assn 2'] = float(row['Assn 2'])
        item['Assn 3'] = float(row['Assn 3'])
        item['Final Exam'] = float(row['Final Exam'])

        new_data_dict[row['Student']] = item

if 'weight' in new_data_dict: del new_data_dict['weight']
if 'max_points' in new_data_dict: del new_data_dict['max_points']
print (new_data_dict)


print('\nPart 2')
lst_nest = []
with open('gradebook.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    new_list = your_list.pop(0)
    new_list.remove('Student')  #https://www.tutorialspoint.com/python/list_remove.htm
    lst1 = your_list.pop(-1)
    lst2 = your_list.pop(-1)
    lst_nest.append(lst1[0])
    lst_nest.append(lst2[0])
    lst1.remove('max_points')
    lst2.remove('weight')
    names= [a[0] for a in your_list]
#print(your_list)
#print (names)
#print (new_list)
#print (lst1)
#print (lst2)
#print (lst_nest)

d = {}
for i in range (4):
    d[new_list[i]] = {}
    d[new_list[i]][lst_nest[1]] = lst2[i]
    d[new_list[i]][lst_nest[0]] = lst1[i]

print(d)



print('\nPart 3')
def student_average(student_name):
    max_lst = [float(b) for b in lst1]
    weight_lst = [float(a) for a in lst2]

    for a in your_list:
        if student_name in a:
            student_lst = [float(b) for b in (a[1:])]
    div_lst = [x/y for x,y in zip(student_lst, max_lst)]
    mult_lst = [a*b for a,b in zip(div_lst, weight_lst)]
    student_average = sum(mult_lst)*100

    #student_average = float(sum_a/average_a)
    return ('{}: {}'.format(student_name, student_average))

for a in names:
    console_ans= student_average(a)
    print (console_ans)

print('\nPart 4')
def assn_average(assn_name):
    if assn_name == 'Assn 1':
        assn = [float(a[1]) for  a in your_list]
        assn_sum = sum(assn)
        max_points = float(lst1[0])*6
        assng_average = float(assn_sum/max_points)*100
    elif assn_name == 'Assn 2':
        assn = [float(a[2]) for  a in your_list]
        assn_sum = sum(assn)
        max_points = float(lst1[1])*6
        assng_average = float(assn_sum/max_points)*100
    elif assn_name =='Assn 3':
        assn = [float(a[3]) for  a in your_list]
        assn_sum = sum(assn)
        max_points = float(lst1[2])*6
        assng_average = float(assn_sum/max_points)*100
    elif assn_name == 'Final Exam':
        assn = [float(a[4]) for  a in your_list]
        assn_sum = sum(assn)
        max_points = float(lst1[3])*6
        assng_average = float(assn_sum/max_points)*100
    return ('{}: {}'.format(assn_name, assng_average))
    #return assng_average


for i in new_list:
    g = assn_average(i)
    print(g)
