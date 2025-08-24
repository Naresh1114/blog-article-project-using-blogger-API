from django.shortcuts import render
import requests

API_KEY = "AIzaSyCTdtkDaiBXCCW8y742iCvkhZ8_v_EZFyI"
BLOG_ID = "2399953"

url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts"
params = {
    "maxResults": 1, # Number of posts to fetch
    "fields": "items(id,title,url,published,labels,author(displayName),content)",
    "key": API_KEY
}
data = requests.get(url, params=params).json()

def content(request):
    return render(request,'home.html',data)

def final(request,id):
    for item in data['items']:
        if item['id']==id:
            return render(request,'result.html',{'data':item})