import re
import sys
import os
article_id = {}
id_article = {}
user_id = {}
id_user = {}
u_article = {}
user_article_map = {}
data_folder = sys.argv[1]
def main ():
	users = []
	articles = []
	files = os.listdir(data_folder)

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


	articles = list(set(articles))
	users = list (set(users))
	# print len(users) , len(articles)
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

		new_dict[temp] = new_list

	user_article_map = new_dict
	

main()