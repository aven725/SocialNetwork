import json
import jieba
import jieba.analyse
import operator

jieba.initialize()
jieba.set_dictionary('data/dict.txt.big')
jieba.load_userdict('data/mydict')

# Reading data list
File_Array = ["filter-GOS.json"]

maptable = {}

top20 = list()

for file in File_Array:
    with open("JsonOutput/"+file, 'r',encoding='UTF-8') as f:
        Array_Data = json.load(f)
        for data in Array_Data:
            str_temp =  data["article_title"] + "\n" + data["content"] + "\n"
            for msg in data["messages"]:
                str_temp = str_temp + msg["push_content"] + "\n"

            top20 = jieba.analyse.extract_tags(str_temp, topK=20, withWeight=True,allowPOS=['n','ns','nr','na'])

            for topmap in top20:
                if topmap[0] in maptable:
                    maptable[topmap[0]] += topmap[1]
                else:
                    maptable[topmap[0]] = topmap[1]

ans = list(reversed(sorted(maptable.items(), key=operator.itemgetter(1))))

with open("Cut/cut-GOS.txt",'w',encoding='UTF-8') as f:
    f.write(str(ans))