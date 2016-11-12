import json

# Reading data list
FileArray = ["HatePolitics-1-1000.json","HatePolitics-1001-2000.json","HatePolitics-2001-3000.json","HatePolitics-3001-3542.json"]

DICT=list()

for file in FileArray:
    with open("Json/HatePolitics/"+file, 'r',encoding='UTF-8') as f:
        Data = json.load(f)
        for gos in Data["articles"]:
            if 'error' not in gos.keys():
                if gos["article_title"] is not None:
                    if "洪秀柱" in gos["article_title"] or "洪秀柱" in gos["content"]:
                        DICT.append(gos)
# Writing JSON data
with open("JsonOutput/filter-Hate.json", 'w',encoding='UTF-8') as f:
    json.dump(DICT, f,indent=4,ensure_ascii=False)