import re
import random

new = []
hand = open('mbox.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('[-a-zA-Z._<]+[^0-9][^\s]@{1}[-a-zA-Z0-9._]+[.]+[a-zA-Z]+', line)
	if len(x) > 0:
		new.append(x)
#print(new)
new_new =[]
for a in new:
	for b in a:
		new_new.append(b)
#print (new_new)

new_lst = []
for g in new_new:
	if g not in new_lst:
		new_lst.append(g)
		sorted(new_lst)
print (new_lst)

d = {}
for x in new_lst:
	ran_num = random.randint(10001, 99999)
	if ran_num not in d:
		d[x] = ran_num


lx = open('mbox.txt')
lines = lx.readlines()

anon = open('mbox-anon.txt', 'w')

for line in lines:
	for key in d:
		if key in line:
			r = "%%" + str(d[key]) + "%%"
			line = line.replace(key, r)
	anon.write(line)
anon_key = open('mbox-anon-key.txt', 'w')

for x in d.keys():

	anon_k = str(d[x]) + '=' + x + '\n'
	anon_key.write(anon_k)
