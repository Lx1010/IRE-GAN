# -*- coding: utf-8 -*-

import tensorflow as tf
import string,re

regex = re.compile('[%s]' % re.escape(string.punctuation))

######################################
# Load Data
######################################

userId = list()
idToArticle = dict()
articleToData = dict()
listToRem = ["URL","originalUrl","inlineUrl","imageUrlHash","linkType","title","desc","source","urlHash","shortUrl"]
listAfter_desc= ["source","pId","unsafe","src","reachAmount","hasFullText","duration","hasEntity","sensitive","timeStamp","blocked","broken","lang","isRetweet","truncated","postCount","reachAmount","fbLikesCount","retweetCount","followersCount","friendsCount"]
listAfter_categ = ["reachAmount","hasFullText","isVeooz360Available","isTrending","duration"]


def detect_language(line):

    try:
        line.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

with open('01-05-2017') as fin:
	for line in fin:
		if "{" not in line:
			line = line.split()
			userId.append(line[1])
			idToArticle[line[1]] = line[2]
		else:
			if detect_language(line):
				line = line.split()
				articleToData[line[0]] = line[1:]

# fid = open("test.txt","w")
# for i in idToArticle:
# 	fid.write(i+"   --->   "+str(idToArticle[i])+"\n")

k = 1
title = False
desc = False
categ = False
bow = set()
artToBOW = {}
for j in articleToData:
	bow.clear()
	title = False
	desc = False
	categ = False
	if "category" not in str(articleToData[j]).lower():
		for word in articleToData[j]:
			if word in listAfter_desc:
				break
			if "title" in word.lower():
				title = True
			if "desc" in word.lower():
				title = False
				desc = True
			if title and word!="title":
				bow.add(word.lower())
			if desc and word!="desc":
				bow.add(word.lower())
		if j not in artToBOW:
			artToBOW[j] = bow
	else:
		for word in articleToData[j]:
			if word in listAfter_categ:
				break
			if "category" in word.lower():
				categ = True
			if categ and word.lower() != "category":
				bow.add(word.lower())
		if j not in artToBOW:
			artToBOW[j] = bow


print len(artToBOW)