# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

# Create your views here.

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
                obj = {'title':'nil','href':''};
                obj['title'] = li.find('a').string
                obj['href'] = li.find('a')['href'][9:]
                print(obj)
                print('------');
                context['data'].append(obj)

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
