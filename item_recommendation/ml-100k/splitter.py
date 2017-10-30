from sklearn.model_selection import train_test_split
# from tqdm import tqdm #install pip install tqdm
f=open('test_file_small.txt','r')

X=[]
Y=[]
dictC={}#dict of classes
for line in f:
	X.append(line)
	uid,aid,score=line.strip().split();
	Y.append(uid)
	if uid not in dictC:
		dictC[uid]=1
	else:
		dictC[uid]+=1


#remove classes with one member
X,Y= zip(*[(x,y) for x,y in zip(X,Y) if not dictC[y]<=1])

print len(X),len(Y)
		


X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.2, random_state=42,stratify=Y)
#write train file
f=open('train.txt','w')
for line in X_train:
	f.write(line)

#write test file
f=open('test.txt','w')
for line in X_test:
	f.write(line)

