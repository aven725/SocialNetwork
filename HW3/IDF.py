import json
import math


def run(cut_file_path, cut_file, org_file_path, org_file_array, output_name):
    keywords = dict()
    total_articles = 0
    with open(cut_file_path + cut_file, 'r', encoding='UTF-8') as j:
        words = json.load(j)
    for word in words:
        keywords[word[0]] = 0

    for file in org_file_array:
        with open(org_file_path + file, 'r', encoding='UTF-8') as f:
            articles = json.load(f)
        for article in articles["articles"]:
            # 當有被刪除的文章時，key為 error，所以沒error時才運算
            if 'error' not in article.keys():
                total_articles += 1
                for keyword in keywords:
                    keywords[keyword] = keywords[keyword] + int(appearInDoc(article, keyword))

    # 計算 IDF
    for keyword in keywords:
        if keywords[keyword] != 0:
            # 取log 10為基底
            keywords[keyword] = math.log(total_articles/keywords[keyword], 10)

    with open("IDF/idf-" + output_name + ".txt", 'w', encoding='UTF-8') as f:
        for word in words:
            f.write(str(word[0])+" "+str(keywords[word[0]])+"\n")


# 檢查關鍵字是否出現過在文章內
def appearInDoc(article, keyword):
    title = str(article["article_title"])
    content = str(article["content"])
    message = str(article["messages"])

    # 找標題
    if keyword in title:
        return 1

    # 找內容
    if keyword in content:
        return 1

    # 找推文
    if keyword in message:
        return 1
    return 0


def main():
    cutPath = "Cut/"
    HatePoliticsPath = "Json/HatePolitics/"
    HatePoliticsArray = ["HatePolitics-1-1000.json", "HatePolitics-1001-2000.json", "HatePolitics-2001-3000.json",
                         "HatePolitics-3001-3542.json"]
    # HatePoliticsArray = ["HatePolitics-1-1000.json"]
    GossipingPath = "Json/Gossiping/"
    GossipingArray = ["Gossiping-10000-11000.json", "Gossiping-11001-12000.json", "Gossiping-12001-13000.json",
                      "Gossiping-13001-14000.json", "Gossiping-14001-15000.json", "Gossiping-15001-16000.json",
                      "Gossiping-16001-17000.json", "Gossiping-17000-17678.json"]
    # GossipingArray = ["Gossiping-10000-11000.json"]

    run(cutPath, "cut-Hate.json", HatePoliticsPath, HatePoliticsArray, "Hate")
    run(cutPath, "cut-Gos.json", GossipingPath, GossipingArray, "Gos")


if __name__ == "__main__":
    main()
