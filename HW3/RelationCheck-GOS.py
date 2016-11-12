import json

# Reading data list
FileArray = ["Gossiping-10000-11000.json","Gossiping-11001-12000.json","Gossiping-12001-13000.json",
             "Gossiping-13001-14000.json","Gossiping-14001-15000.json","Gossiping-15001-16000.json",
             "Gossiping-16001-17000.json","Gossiping-17000-17678.json"]

DICT=list()

for file in FileArray:
    with open("Json/Gossiping/"+file, 'r',encoding='UTF-8') as f:
        Data = json.load(f)
        for gos in Data["articles"]:
            if 'error' not in gos.keys():
                if gos["article_title"] is not None:
                    if "洪秀柱" in gos["article_title"] or "洪秀柱" in gos["content"]:
                        DICT.append(gos)
# Writing JSON data
with open("JsonOutput/filter-GOS.json", 'w',encoding='UTF-8') as f:
    json.dump(DICT, f,indent=4,ensure_ascii=False)

