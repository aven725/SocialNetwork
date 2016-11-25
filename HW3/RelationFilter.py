import json


def filter_articles(file_path, file_array, output_name):

    # 建立新的空間，用來放最後過濾的資料
    dict_list = list()

    # 將 "article_title" 有 "洪秀柱" 相關的複製一份到 DICT
    for file in file_array:
        with open(file_path + file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            for gos in data["articles"]:
                # 當有被刪除的文章時，key為 error，所以沒error時才copy
                if 'error' not in gos.keys():
                    if gos["article_title"] is not None:
                        if "洪秀柱" in gos["article_title"] or "洪秀柱" in gos["content"]:
                            dict_list.append(gos)
    # Writing JSON data
    with open("JsonOutput/filter-"+output_name+".json", 'w', encoding='UTF-8') as f:
        json.dump(dict_list, f, indent=4, ensure_ascii=False)


def main():
    # Reading data list
    HatePoliticsPath = "Json/HatePolitics/"
    HatePoliticsArray = ["HatePolitics-1-1000.json", "HatePolitics-1001-2000.json", "HatePolitics-2001-3000.json",
                         "HatePolitics-3001-3542.json"]
    GossipingPath = "Json/Gossiping/"
    GossipingArray = ["Gossiping-10000-11000.json", "Gossiping-11001-12000.json", "Gossiping-12001-13000.json",
                      "Gossiping-13001-14000.json", "Gossiping-14001-15000.json", "Gossiping-15001-16000.json",
                      "Gossiping-16001-17000.json", "Gossiping-17000-17678.json"]

    filter_articles(HatePoliticsPath, HatePoliticsArray, "Hate")
    filter_articles(GossipingPath, GossipingArray, "Gos")

if __name__ == "__main__":
    main()
