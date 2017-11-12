import re
import sys
import os
import random
article_id = {}
id_article = {}
user_id = {}
id_user = {}
u_article = {}
nu_article = {}
user_article_map = {}
data_folder = sys.argv[1]
article_data = {}

users = []
articles = []
# file = "01-05-2017"
files = os.listdir(data_folder)
flag = 0
for file in files:
	fp = open(data_folder + file)
	for line in fp: 
		if(line.split()[0]=="an"):
			temp = line.split("\t")
			user = temp[1]
			users.append(temp[1])
			new = temp[2].split("[")
			new = new[1].split("]")[0]
			user_articles = new.split(",")
			for j in range(len(user_articles)):
				user_articles[j] = user_articles[j].strip('"')
			if(user not in u_article):
				u_article[user] = user_articles
			else:
				u_article[user] += user_articles

			articles += user_articles
		else:
			if(re.search("\"lang\":\"en\"",line)):
				art_id = line.split("\t")[0]
				article_data[art_id] = line

for i in u_article:
	new_set = []
	for j in u_article[i]:
		if(j in article_data):
			new_set +=[j]
	u_article[i] = new_set

users = []
articles = []
new_dict = {}
for i in u_article:
	if(len(u_article[i])>=10):
		new_dict[i] = u_article[i]
		
u_article =new_dict


count = 0
new_dict = {}

#change the count in the below loop to change the number of users.

for i in u_article:
	if(count==100):
		break
	new_dict[i] = u_article[i]
	articles += u_article[i]
	count+=1

u_article = new_dict   




users = list(u_article.keys())
articles = list(set(articles))
# print len(articles),len(users)


count = 0	
for i in articles:
	article_id[i] = count
	id_article[count] = i
	count +=1
count = 0

for i in users:
	user_id[i] = count
	id_user[count] = i
	count+=1
new_dict = {}
for i in u_article:
	temp = user_id[i]
	# print temp	
	new_list=[]
	for j in range(len(u_article[i])):
		new_list += [article_id[u_article[i][j]]]

	new_dict[temp] = list(set(new_list))

u_article = new_dict

temp = set(id_article.keys())
# u_not_read = {}
# for i in range(len(u_article)):
# 	not_read = temp.difference(set(u_article[i]))
# 	length = int(0.3 * float(len(u_article[i])))
# 	not_read = random.sample(not_read,length)
# 	u_not_read[i] = list(not_read)


for i in range(len(u_article)):
	for j in u_article[i]:
		print str(i) + "\t" + str(j) + "\t" + str(5)
	# for j in u_not_read[i]:
	# 	print str(i) + "\t" + str(j) + "\t" + str(0)