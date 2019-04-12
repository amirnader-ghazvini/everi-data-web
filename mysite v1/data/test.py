import json
from pprint import pprint 
path="sample.json"
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
        temp=[i[0] for i in items[t+'.Related.Attribute']]
        rel_attr.append(temp)

    
    if "Flag" in items:
        flag=items['Flag']['URL']
    else:
        flag=False
    everipedia=items['Everipedia.Page']

##    try: 
    lst.append({'str_id':str_id,'synonyms':synonyms,'type':types,'related_attr':rel_attr,'flag':flag,"everipedia":everipedia})
##    except NameError:
##        lst.append({'str_id':str_id,'synonyms':synonyms,'type':types,'related_attr':rel_attr,"everipedia":everipedia})
        
