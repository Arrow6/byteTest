def getByte(number, l):
	i = 0
	mn = 1
	nlist = []
	while i is < l:
		mn = mn * i
		nlist.append(mn)
		i += 1
	byte = []
	nr = number
	for i in nlist:
		
	
	


f = open(raw_input("->> "), "r")
c = f.read()
clist = []
for ch in c:
	clist.append(ch)

nlist = []
for ch in clist:
	nlist.append(ord(ch))


blist = []
i = 0
while i is < len(nlist):
	blist.append(getByte(n, 8))
	i += 1