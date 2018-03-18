
# coding: utf-8

# In[1]:


import requests
from pprint import pprint


# In[2]:


text_analytics_base_url = "https://southeastasia.api.cognitive.microsoft.com/text/analytics/v2.0/"


# In[3]:


subscription_key = 'bed5d202ad2342fabdad64f1174c71a4'
assert subscription_key


# In[4]:


key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)


# In[5]:


#Data
documents = {'documents':[
{'id': 'iphoneX', 'text': 'The Apple iPhone X is one of the most groundbreaking launches from Apple as far as both technology and design are concerned. Each and every department is richly fed with the most that you could get. And since the new iPhone 10 loses the home button and the fingerprint scanner on it, the FaceID is what replaces it, big time.'},
{'id': 'LGG6', 'text': 'The LG G6 is another powerful flagship smartphone from the house of LG, which has been extremely generous in providing the Indian smartphone market with a large number of great quality flagship smartphones one after the other. This smartphone feeds from a powerful processor and a great camera quality. So if you want to own a flagship smartphone, there wouldn�t have been any better option than this LG.'},
{'id': 'Iphone8', 'text': 'Apple has always followed a norm of manufacturing smartphones a notch better than the previous one. The iPhone 8 too is far better than its predecessor in ways more than one. The configuration and the battery are the best so far among all iPhones. So if you are in love with this high-end brand, and are prepared to shell out huge bucks, you can buy this one. '},
{'id': 'Iphone7', 'text': 'The Apple iPhone 7 is definitely a beauty worth beholding. But this time the beauty comes with a larger brain. Powered by the most powerful processor so far and the latest iOS, the smartphone indeed solves your tasks in a jiffy. The amazing camera, larger battery backup, wide arrayed connectivity options and a bag full of patented features, makes this flagship a good buy.'},
{'id': 'IphoneSE', 'text': 'The iPhone SE is targeted to the users who would still like to go with a smaller version of the Apple\'s newiPhone 6-series smartphones. If you have liked the previous iPhone 5-series smartphones and want to enjoy the same goodness again with upgraded features, this one worth your attention.'},
{'id': 'Iphone6s', 'text': 'The premium phone comes at a premium price tag. With a decent performing configuration, dazzling looks, wide arrayed connectivity and a bag full of patented features, the flagship device is a good buy. If you have liked the previous iPhone 5-series smartphones, iPhone SE worth your attention'},
{'id': 'Pixel2', 'text': 'After the success of the Nexus series, Google is back with a bang with Pixel XL, which is a powerful device with a good pair of cameras. The excellent display properties would make the users fall in love with it. However, the device lacks little features at such high price. But if you have a craze of using the latest version of Android OS, do give it a check.'},
{'id': 'Pixel', 'text': 'After the success of the Nexus series, Google is back with a bang with Pixel series, consisting of Pixel and Pixel XL, which is a powerful device with a good pair of cameras. However, the device lacks little features at such high price. But, the performance and a  good pair of cameras make it an obvious option if you have a craze of using the latest version of Android OS, do give it a check'},
{'id': 'GalaxyS8', 'text': 'The Samsung Galaxy S8 is the new flagship phone from the korean tech giant. It offers many of the best features and specification currently in demand by the consumers. Thus, if you are looking to buy a splendid smartphone with budget not being a barrier, you can wait for the release of this one.'},
{'id': 'GalaxyNote8', 'text': 'Albeit expensive, the Samsung Galaxy Note 8 can easily be termed as the best smartphone in the market. Equipped with great photography capabilities, sound performance, curved display, S-Pen and wireless charging support, the smartphone is worthy of its high price tag.'},
{'id': 'GalaxyA8+', 'text': 'The Samsung Galaxy A8 Plus 2018 can aptly be called a perfect blend of a tablet and a smartphone, termed as a phablet. This device is a powerhouse in terms of performance and storage. The cameras are praiseworthy and the selfie camera is the major highlight. Moreover, the battery backup of the device tends to improve with quick charging feature. Overall, it is a power-packed device to deliver some great smartphone experience to its users.'},
{'id': 'GalaxyC9Pro', 'text': 'Samsung Galaxy C9 Pro comes packed with all powerful features, including the processor, battery, great display, etc. However, the cameras tends to steal the show, compared to its peers. So if want to own a premium smartphone, this is probably the one you need to choose.'},
{'id': 'GalaxyC7', 'text': 'The Samsung Galaxy C7 Pro has everything to be a midrange flagship by a trustworthy brand. Its full scaled hardware and elegant metal outfit enlist this smartphone among the top smartphone contenders. It is perfect for an avid photographer as well as a selfie fanatic. Connectivity wise it does not seem to lack behind either. The only issue is the lower pixel density, but considering its budget it can be overlooked.'},
{'id': 'GalaxyJ7', 'text': 'If you have been waiting for a phablet from the Korean electronics giant, the Samsung Galaxy J7 2015 is here. It falls in the mid range portfolio and will expand Samsung\'s youngest J series. It boasts of a powerful processor along with exciting cameras but misses out a good display. And just like most other phablets, it is too heavy. The new Samsung Galaxy J7 2016 a powerful and elegant smartphone with its excellent design and good features.'},
{'id': 'GalaxyJ5', 'text': 'The Samsung Galaxy J5 2015 is an extension of the company\'s youngest J series of smartphones. This mid range device doesn\'t have anything surprising but also doesn\'t miss out anything that you should expect for its price. The excellent pair of cameras will surely win the hearts of photo crazy youngsters. On the downside, Samsung hasn\'t taken any efforts to make it look appealing. Click the new edition Samsung Galaxy J5 2016 comes with more power and better features.'},
{'id': 'GalaxyOn7Prime', 'text': 'The Samsung Galaxy On7 Prime 64GB is a premium smartphone which comes with a lot of strong features. It performs well while handling multitasking and offers a massive storage to enhance your entertainment scope. You can capture high-resolution images and record Full-HD videos with the excellent pair of cameras. Overall, if you are looking for a powerful mid-range device then you can go for the Samsung Galaxy On7 Prime 64GB.'},
{'id': 'GalaxyJ2Pro', 'text': 'The Samsung Galaxy J2 Pro is the latest mid range device from the South Korean tech giant. The device is a combination of good looks and powerful performance. The handset also comes with many innovative features like Turbo Speed Technology,  Smart Glow ring as well as Samsung\'s popular ultra data saving and S bike mode.'},
{'id': 'GalaxyS7Edge', 'text': 'The Samsung Galaxy S7 Edge is a monster in terms of specs and features and with 3D glass and metal body it combines beauty too. Additional features such as dust and waterproof make it a perfect choice. Along with Samsung Galaxy S7, it boasts of being the first phones to come with dual pixel camera as well.'},
{'id': 'OnePlus5', 'text': 'OnePlus, the Chinese smartphone maker has taken the league of smartphones to an altogether different level. The OnePlus 5 holds one of the most powerful processors and camera in the segment. Apart from this, the smart connectivity features, big battery backup and high internal storage leaves nothing to complain about, even with the high price tag.'},
{'id': 'OnePlus5T', 'text': 'The OnePlus 5T is an amazing smartphone and ticks all the correct boxes. All of the features, including the high-performance processor, an amazing pair of cameras, massive internal storage and a sharp display, work in tandem to make this smartphone work in a beast mode each time you use it. Almost every section of the smartphone is lag-free and delivers superior quality of everything. Moreover, a device with such calibre is seldom seen at that price tag.'},
{'id': 'GalaxyS9', 'text': 'The Samsung Galaxy S9 is a power packed smartphone with nice features such as a waterproof body and quick charging support. It comes in a stylish body and is a sound performer. The display quality, cameras and battery backup are great. The Samsung Galaxy S9 is worth buying. It has all the elements which the user desires from a top brand.'},
{'id': 'HTCU11', 'text': 'The HTC 11 is another powerful smartphone front the house of HTC, which has been extremely generous in providing the Indian smartphone market with a large number of great quality smartphones. This smartphone feeds from a powerful processor and a great camera quality. So if you want to own such a smartphone, there wouldn�t have been any better option than this.'},
{'id': 'HTCDesire10', 'text': 'The HTC Desire 10 Pro is a robust configured handset and marvellous cameras. The ample expandable memory is ideal for the ones looking out to save large number of high sized files. The users can enjoy 4G connectivity for long hours since the battery backup is excellent. However, a front flash would have been a good thing.'},
{'id': 'HTCU', 'text': 'The HTC U Play is another powerful smartphone fromt the house of HTC, which has been extremely generous in providing the Indian smartphone market with a large number of great quality smartphones. This smartphone feeds from an extremely powerful processor and a great camera quality, apart from offering a humongous storage option. So if you want to own such a smartphone, there wouldn�t be any better option than this.'},
{'id': 'HTC10Lifestyle', 'text': 'The semi-transparent front view metallic frame of the HTC 10 LifeStyle makes it one of the gorgeous looking smartphones in India. It is equipped with all the latest features and good specification one expects from a phone in this price segment. If you are looking for an all rounder phone that can also handle the bumps and slips of everyday life, the HTC 10 LifeStyle is a good option.'},
{'id': 'HTCDesire630', 'text': 'The HTC Desire 630 is basically for the ones who are looking forward to buy a GSM + CDMA phone along with nice cameras. Latest operating system comes as an additional package. However, a better battery along with an octa-core processor would have make it a perfect device..'},
{'id': 'RedmiNote5', 'text': 'The Xiaomi Redmi Note 5 is a promising smartphone with impressive features in all the departments. Despite having an affordable price tag, the phone carries a lot of features which are exclusive only to high-end smartphones according to the current market trend.'},
{'id': 'RedmitNote4', 'text': 'The Xiaomi Redmi Note 4 64GB brings more uniform metal texture, different from the previous \'three-stage\' metal Redmi series body. The independent space system is like having an additional cell phone. The users can play high end games and enjoy multitasking apps without any lag. In short, the Redmi Note 4 is one of the perfect allrounder handset for you.'},
{'id': 'Nokia8', 'text': 'The Nokia 8 is another addition to the Nokia series with class performance. It is very evident that the Nokia company is looking forward to introduce back to back mobiles this year. On a concluding note, the Nokia 8 is clearly a winner in all aspects and is a very profitable choice. An impressive display, a good battery backup with quick-charging, great configuration and excellent cameras completely makes this phone worthy.'},
]}


# In[6]:


headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)


# In[7]:


P =""
for document in key_phrases["documents"]:
    text    = next(filter(lambda d: d["id"] == document["id"], documents["documents"]))["text"]    
    phrases = ",".join(document["keyPhrases"])
    P = P+phrases


# In[8]:


P


# In[9]:


import pandas as pd
pd.options.mode.chained_assignment = None 
import numpy as np
import re
import nltk

from gensim.models import word2vec

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

data = pd.read_csv('train.csv').sample(50000, random_state=23)


# In[10]:


STOP_WORDS = nltk.corpus.stopwords.words()
def clean_sentence(val):
    "remove chars that are not letters or numbers, downcase, then remove stop words"
    regex = re.compile('([^\s\w]|_)+')
    sentence = regex.sub('', val).lower()
    sentence = sentence.split(" ")
    
    for word in list(sentence):
        if word in STOP_WORDS:
            sentence.remove(word)  
            
    sentence = " ".join(sentence)
    return sentence

def clean_dataframe(data):
    "drop nans, then apply 'clean_sentence' function to question1 and 2"
    data = data.dropna(how="any")
    
    for col in ['question1', 'question2']:
        data[col] = data[col].apply(clean_sentence)
    
    return data

data = clean_dataframe(data)
data.head(5)


# In[11]:


t = int(len(P)/100)


# In[12]:


d =int(t)*[[]]


# In[13]:


import nltk

w=0
q=0
for i in nltk.word_tokenize(P):
    
    if i not in STOP_WORDS and i!=',':
            d[w].append(i)
            q+=1
    if q>=100:
        q= 0
        w+=1
    
d


# In[14]:


def build_corpus(data):
    "Creates a list of lists containing words from each sentence"
    corpus = []
    for col in ['question1', 'question2']:
        for sentence in data[col].iteritems():
            word_list = sentence[1].split(" ")
            corpus.append(word_list)
            
    return corpus

corpus = build_corpus(data)        
corpus[0:2]


# In[15]:


model = word2vec.Word2Vec(d, size=100)


# In[16]:


def tsne_plot(model):
    "Creates and TSNE model and plots it"
    labels = []
    tokens = []

    for word in model.wv.vocab:
        tokens.append(model[word])
        labels.append(word)
    
    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])
        
    plt.figure(figsize=(16, 16)) 
    for i in range(len(x)):
        plt.scatter(x[i],y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()


# In[17]:


tsne_plot(model)


# In[19]:


X = model[model.wv.vocab]


# In[21]:


from nltk.cluster import KMeansClusterer
import nltk
NUM_CLUSTERS=7
kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25)
assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
print (assigned_clusters)


# In[23]:


words = list(model.wv.vocab)
for i, word in enumerate(words):  
    print (word + ":" + str(assigned_clusters[i]))


# In[24]:


from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

l = linkage(model.wv.syn0, method='complete', metric='seuclidean')

# calculate full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.ylabel('word')
plt.xlabel('distance')

dendrogram(
    l,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=16.,  # font size for the x axis labels
    orientation='left',
    leaf_label_func=lambda v: str(model.wv.index2word[v])
)
plt.show()

