from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse
import json

path="data/sample.json"
with open(path) as file:
    data=json.load(file)

entities_type=[]
for entities in data['list']:
    s=entities['type']
    if isinstance(s, str):
        if s not in entities_type:
            entities_type.append(s)
    else:
        for items in s:
            if items[0] not in entities_type:
                entities_type.append(items[0])
    
lst=[]
for j,items in enumerate(data['list']):
    str_id=items['str.id']
    synonyms=[i[0] for i in items['synonyms']]
    s=items['type']
    if isinstance(s, str):
        types=[s]
    else:
        types=[i[0] for i in items['type']]
    rel_attr=[]
    for t in types:
        try:
            temp=[i[0] for i in items[t+'.Related.Attribute']]
            rel_attr.append(temp)
        except:
            pass
    if "Flag" in items:
        flag=items['Flag']['URL']
    else:
        flag=0
    everipedia=items['Everipedia.Page']

    lst.append({'str_id':str_id,'synonyms':synonyms,'type':types,'related_attr':rel_attr,'flag':flag,"everipedia":everipedia})
        

    
    

def homepage(request):
    return render(request = request,
                  template_name='main/header.html')

def find_view(request):
    return render(request = request,
                  template_name='main/find_view.html')

def entities(request):
    context={
                'data':data['list'],
                'parsed':lst,
                'type':entities_type,
        }
    return render(request=request,template_name='main/entities.html',context=context)


def patterns(request):
    return render(request = request,
                  template_name='main/patterns.html')


def functions(request):
    return render(request = request,
                  template_name='main/functions.html')


def everidata(request):
    return render(request = request,
                  template_name='main/everidata.html')
    
