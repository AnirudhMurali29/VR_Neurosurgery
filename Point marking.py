a = arrayFromVolume(getNode('LabelMapVolume'))

p = np.shape(a)[0]
q = np.shape(a)[1]
r = np.shape(a)[2]

d1 = p//18
d2 = r//18
x1 = 6*d1
x2 = 12*d1
y1 = 6*d2
y2 = 12*d2
cloth = np.zeros((p,r))
index = np.zeros((p,r))
ind_count = 0

for i in range(x1,x2+1,d1):
	cloth[i-1][y1-1]=1
	cloth[i-1][y2-1]=1

for j in range(y1,y2+1,d2):
	cloth[x1-1][j-1]=1
	cloth[x2-1][j-1]=1
	if j<=(y1+3*d2):
		cloth[x1+3*d1-1][j-1]=1


point_count = np.count_nonzero(cloth)

for j in range(y1+3*d2,y1-1,-1):
	if cloth[x1+3*d1-1][j-1]==1:
		index[x1+3*d1-1][j-1]=ind_count
		ind_count+=1

for i in range(x1+4*d1,x2+1,d1):
	index[i-1][y1-1]=ind_count
	ind_count+=1

for j in range(y1+d2,y2+1,d2):
	index[x2-1][j-1] = ind_count
	ind_count+=1

for i in range(x2-d1,x1-1,-1*d1):
	index[i-1][y2-1]=ind_count
	ind_count+=1

for j in range(y2-d2,y1-1,-1*d2):
	index[x1-1][j-1] = ind_count
	ind_count+=1

for i in range(x1+d1,x1+2*d1+1,d1):
	index[i-1][y1-1]=ind_count
	ind_count+=1

list = np.zeros((point_count,3))
for j in range(q):
	slice = a[:,j] #2D slice at that Y coordinate
	b = np.minimum(slice,cloth) #Minimum achieves the same function as Logical And
	cloth = np.subtract(cloth,b) #Removing the points that have already been marked
	for i in range(p):
		for k in range(r):
			if b[i][k]==1:
				x = int(index[i][k])
				list[x] = [k,j,i] #Append points to a list



