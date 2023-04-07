import sys
import ast
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
#hugging face - sentiment
#BERT - Topic Modelling

#for data conversion from json to readable in python
posts=sys.argv
dict_obj=ast.literal_eval(posts[1])
commentsList=[]
commentsList=np.array(commentsList)
ind=0
for values in dict_obj.values():
    for i in values['comments']:
        commentsList=np.append(commentsList,i)

###########################################################################################
sid=SentimentIntensityAnalyzer() #responsible for giving sentiment scores to each post
sentiment_scores=[] #for distiguishing the post's sentiment

for i in commentsList: #needs changes
    score=sid.polarity_scores(i)
    sentiment_scores.append(score)

dict_to_send={}
# dict_to_send["sentiment_scores"]=sentiment_scores #needs changes


label=[] #for storing label of each posts
postiveCount=0
negativeCount=0
neutralCount=0

for s in sentiment_scores:
    if s['pos']>=0.05:
        label.append('Postive')
        postiveCount+=1
    elif s['neg']<=-0.05:
        label.append('Negative')
        negativeCount+=1
    else:
        label.append('Neutral')
        neutralCount+=1

dict_to_send["sentiment_labels"]=label #needs changes

totalCount=postiveCount+negativeCount+neutralCount #total no. of posts
dict_to_send["totalComments"]=totalCount
dict_to_send["postiveComments"]=postiveCount
dict_to_send["negaticeComments"]=negativeCount
dict_to_send["neutralComments"]=neutralCount

labelSeries=pd.Series(label)
sentiment_counts=labelSeries.value_counts() #needs changes

print(dict_to_send)

plt.pie(sentiment_counts,labels=sentiment_counts.index,autopct='%1.1f%%')
plt.title("Sentiment Distribution")

plt.savefig("D://Sem VI//Projects//SDP//Blog_Management_App-main-Aadit//BLOG_MANAGEMENT_TEST_AADIT//client//public//assets//pieChart.png")
plt.show()