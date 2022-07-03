import json
import time
import os
import csv

user_feed_items = []
header = ['videoId','publish','caption','username','thumbnail','url','comments','plays','shares','likes']

folderpath = 'C://narasi-project//parser-tiktok//input//narasi'
list_response  = os.listdir(folderpath)
print(list_response)

for x in list_response:
    filename = os.path.join(folderpath,x)
    print(filename)

    timestr = time.strftime("%Y%m%d-%H%M%S")

    directory = os.path.join('./data',timestr)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, 'r',encoding="utf-8") as j:
        output_response = json.loads(j.read())

    feed_item = output_response["itemList"]

    nama_file = feed_item[0]["author"]["uniqueId"] + ".csv"

    for i in range(len(feed_item)):
        user_feed_items.append(feed_item[i])
        

    with open(os.path.join(directory,nama_file), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for item in user_feed_items:
            writer.writerow([
                    item["id"],
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item["createTime"])),
                    item["desc"],
                    item["author"]["uniqueId"],
                    item["video"]["cover"],
                    'https://www.tiktok.com/@' + item["author"]["nickname"] + '/video/' + item["id"],
                    item["stats"]["commentCount"],
                    item["stats"]["playCount"],
                    item["stats"]["shareCount"],
                    item["stats"]["diggCount"]
                ])
                


