# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube

import requests
from bs4 import BeautifulSoup

import uuid
# Create your views here.

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

def search(request):
    return render(request,'search.html')

def index(request):

    search_text = request.GET.get('search')
    if search_text is not None:
        print(search_text)
        context = {
            'search':search_text,
            'data':[]
        }
        print(context)
        url = "https://www.youtube.com/results?search_query="+search_text+""
        print('Searching '+url)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.find('div',{'id':'results'}).find('ol',{'class','item-section'}).findAll('li'):
            li = link.find('h3',{'class','yt-lockup-title '});
            if li is not None:
                obj = {'title':'nil','href':'','thumb':'nil'};
                obj['title'] = li.find('a').string
                obj['href'] = li.find('a')['href'][9:]
                print(obj['href'])
                print(str(obj['href']).find('?'))
                if obj['href'].find('&') > -1:
                    print('inside')
                    ind = obj['href'].find('&')
                    print(ind)
                    obj['href'] = obj['href'][0:ind]
                obj['thumb'] = 'http://i4.ytimg.com/vi/' + obj['href'] + '/hqdefault.jpg'
                print('----------');
                context['data'].append(obj)
                # print(context)

    else:
        context={'data':'nil'}
    return render(request, 'search.html',context)

def watch(request,video_id):
    # search_text = request.GET.get('search')
    # context = {
    #     'search':search_text,
    #     'data':[]
    # }
    # url = "https://www.youtube.com/results?search_query="+search_text
    # source_code = requests.get(url)
    # plain_text = source_code.text
    # soup = BeautifulSoup(plain_text, "html.parser")
    #
    # for link in soup.find('div',{'id':'results'}).find('ol',{'class','item-section'}).findAll('li'):
    #     print(link)
    # print(search_text)
    context = {
        'watch':video_id
    }
    return render(request,'watch.html',context)

def download(request,video_id):
    str = "https://www.youtube.com/watch?v="+video_id
    print(str)
    yt = YouTube(str)

    print(video_id)
    print(yt.get_videos())
    # print(yt.filename)
    fname = yt.filename + my_random_string(6)
    yt.set_filename(fname)
    # print(yt.filter('mp4')[-1])
    video = yt.get('mp4','720p')
    video.download('/tmp/')
    downloadpath = '/tmp/'+fname
    context = {
        'path':downloadpath
    }
    return render(request,'download.html',context)
