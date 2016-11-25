import json
import jieba.analyse
import operator


jieba.initialize()
jieba.set_dictionary('data/dict.txt.big')
jieba.load_userdict("data/mydict.txt.big")


# 方便未來擴充所以寫成 array
def cut_articles(file_array, output_name, idf_file="NONE"):

    # 如果有設定IDF辭典，則設定此檔案
    if idf_file != "NONE":
        jieba.analyse.set_idf_path(idf_file)

    # 存放每一篇的topK的hash table
    maptable = {}

    for file in file_array:
        with open("JsonOutput/" + file, 'r', encoding='UTF-8') as f:
            array_data = json.load(f)
            for data in array_data:
                str_temp = data["article_title"] + "\n" + data["content"] + "\n"
                for msg in data["messages"]:
                    str_temp = str_temp + msg["push_content"] + "\n"

                # 存放每篇文章的topK , K目前取20
                topK = jieba.analyse.extract_tags(str_temp, topK=20, withWeight=True, allowPOS=['n', 'ns', 'nr', 'na'])

                for topmap in topK:
                    if topmap[0] in maptable:
                        maptable[topmap[0]] += topmap[1]
                    else:
                        maptable[topmap[0]] = topmap[1]

    ans = list(reversed(sorted(maptable.items(), key=operator.itemgetter(1))))

    if idf_file == "NONE":
        with open("Cut/cut-"+output_name+".txt", 'w', encoding='UTF-8') as f:
            # indent=4 代表縮排，排版用
            json.dump(ans, f, indent=4, ensure_ascii=False)
    else:
        with open("Cut/cut-" + output_name + ".txt", 'w', encoding='UTF-8') as f:
            for word in ans:
                f.write(str(int(word[1])) + "　" + str(word[0]) + "\n")


def main():
    # Reading data list
    HatePoliticsArray = ["filter-Hate.json"]
    GossipingArray = ["filter-GOS.json"]

    cut_articles(HatePoliticsArray, "Hate")
    cut_articles(GossipingArray, "Gos")

    # TF-IDF Calculator
    cut_articles(HatePoliticsArray, "IDF-Hate", "IDF/idf-Hate.txt")
    cut_articles(GossipingArray, "IDF-Gos", "IDF/idf-Gos.txt")

if __name__ == "__main__":
    main()
