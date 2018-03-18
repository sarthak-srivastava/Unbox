
# coding: utf-8

# # Quickstart for Text Analytics API with Python 
# <a name="HOLTop"></a>
# 
# This walkthrough shows you how to [detect language](#Detect), [analyze sentiment](#SentimentAnalysis), and [extract key phrases](#KeyPhraseExtraction) using the [Text Analytics APIs](//go.microsoft.com/fwlink/?LinkID=759711) with Python.
# 
# You can run this example as a Jupyter notebook on [MyBinder](https://mybinder.org) by clicking on the launch Binder badge: 
# 
# [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Microsoft/cognitive-services-notebooks/master?filepath=TextAnalytics.ipynb)
# 
# Refer to the [API definitions](//go.microsoft.com/fwlink/?LinkID=759346) for technical documentation for the APIs.
# 
# ## Prerequisites
# 
# You must have a [Cognitive Services API account](https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account) with **Text Analytics API**. You can use the **free tier for 5,000 transactions/month** to complete this walkthrough.
# 
# You must also have the [endpoint and access key](../How-tos/text-analytics-how-to-access-key.md) that was generated for you during sign-up. 
# 
# To continue with this walkthrough, replace `subscription_key` with a valid subscription key that you obtained earlier.

# In[1]:


subscription_key = 'bed5d202ad2342fabdad64f1174c71a4'
assert subscription_key


# Next, verify that the region in `text_analytics_base_url` corresponds to the one you used when setting up the service. If you are using a free trial key, you do not need to change anything.

# In[2]:


text_analytics_base_url = "https://southeastasia.api.cognitive.microsoft.com/text/analytics/v2.0/"


# <a name="Detect"></a>
# 
# ## Detect languages
# 
# The Language Detection API detects the language of a text document, using the [Detect Language method](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/operations/56f30ceeeda5650db055a3c7). The service endpoint of the language detection API for your region is available via the following URL:

# In[3]:


language_api_url = text_analytics_base_url + "languages"
print(language_api_url)


# The payload to the API consists of a list of `documents`, each of which in turn contains an `id` and a `text` attribute. The `text` attribute stores the text to be analyzed. 
# 
# Replace the `documents` dictionary with any other text for language detection. 

# In[4]:


documents = { 'documents': [
    { 'id': '1', 'text': 'This is a document written in English.' },
    { 'id': '2', 'text': 'Este es un document escrito en Español.' },
    { 'id': '3', 'text': '这是一个用中文写的文件' }
]}


# The next few lines of code call out to the language detection API using the `requests` library in Python to determine the language in the documents.

# In[5]:


import requests
from pprint import pprint
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)


# The following lines of code render the JSON data as an HTML table.

# In[6]:


from IPython.display import HTML
table = []
for document in languages["documents"]:
    text  = next(filter(lambda d: d["id"] == document["id"], documents["documents"]))["text"]
    langs = ", ".join(["{0}({1})".format(lang["name"], lang["score"]) for lang in document["detectedLanguages"]])
    table.append("<tr><td>{0}</td><td>{1}</td>".format(text, langs))
HTML("<table><tr><th>Text</th><th>Detected languages(scores)</th></tr>{0}</table>".format("\n".join(table)))


# <a name="SentimentAnalysis"></a>
# 
# ## Analyze sentiment
# 
# The Sentiment Analysis API detexts the sentiment of a set of text records, using the [Sentiment method](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/operations/56f30ceeeda5650db055a3c9). The following example scores two documents, one in English and another in Spanish.
# 
# The service endpoint for sentiment analysis is available for your region via the following URL:

# In[7]:


sentiment_api_url = text_analytics_base_url + "sentiment"
print(sentiment_api_url)


# As with the language detection example, the service is provided with a dictionary with a `documents` key that consists of a list of documents. Each document is a tuple consisting of the `id`, the `text` to be analyzed and the `language` of the text. You can use the language detection API from the previous section to populate this field. 

# In[8]:


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


# The sentiment API can now be used to analyze the documents for their sentiments.

# In[39]:


import math


# In[44]:


headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
for i in range(len(documents['documents'])):
    sentiments['documents'][i]['score']=math.ceil(5*sentiments['documents'][i]['score'])
    print(sentiments['documents'][i]['score'])


# The sentiment score for a document is between $0$ and $1$, with a higher score indicating a more positive sentiment.

# <a name="KeyPhraseExtraction"></a>
# 
# ## Extract key phrases
# 
# The Key Phrase Extraction API extracts key-phrases from a text document, using the [Key Phrases method](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/operations/56f30ceeeda5650db055a3c6). This section of the walkthrough extracts key phrases for both English and Spanish documents.
# 
# The service endpoint for the key-phrase extraction service is accessed via the following URL:

# In[50]:


key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)


# The collection of documents is the same as what was used for sentiment analysis.

# In[51]:


pprint(documents)


# In[52]:


headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)


# The JSON object can once again be rendered as an HTML table using the following lines of code:

# In[53]:


from IPython.display import HTML
table = []
P =""
for document in key_phrases["documents"]:
    text    = next(filter(lambda d: d["id"] == document["id"], documents["documents"]))["text"]    
    phrases = ",".join(document["keyPhrases"])
    P = P+phrases
    table.append("<tr><td>{0}</td><td>{1}</td>".format(text, phrases))
HTML("<table><tr><th>Text</th><th>Key phrases</th></tr>{0}</table>".format("\n".join(table)))


# ## Next steps
# 
# > [!div class="nextstepaction"]
# > [Text Analytics With Power BI](../tutorials/tutorial-power-bi-key-phrases.md)
# 
# ## See also 
# 
#  [Text Analytics overview](../overview.md)  
#  [Frequently asked questions (FAQ)](../text-analytics-resource-faq.md)
