import re
import sys
article_id = {}
id_article = {}
user_id = {}
id_user = {}
u_article = {}
data_folder = sys.argv[1]
def main ():
	fp = open(data_folder + "01-05-2017")
	users = []
	articles = []
	count = 0
	for line in fp:
		count +=1
		if(line.split()[0]=="an"):
			temp = line.split("\t")
			user = temp[1]
			users.append(temp[1])
			new = temp[2].split("[")
			new = new[1].split("]")[0]
			user_articles = new.split(",")
			u_article[user] = user_articles
			# print user_articles
			articles += user_articles
	articles = list(set(articles))
	users = list (set(users))
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
		# del u_article[i]
		new_dict[temp] = new_list
	# print new_dict

	# print len(users)

main()