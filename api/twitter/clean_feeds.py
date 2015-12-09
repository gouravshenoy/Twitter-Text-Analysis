__author__ = 'Gaurav-PC'

import csv
from time import sleep
from sentiment.classifier import Classifier

in_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\cuisine_dataset.csv"
out_file = "cuisine_dataset_with_header.csv"
temp_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\cuisine_dataset_clean.csv"

# cuisine files
indian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\indian.csv"

indian_cuisine = ['biryani', 'indian', 'india', 'masala', 'tikka',
                  'naan', 'kulcha', 'upma', 'idli', 'dosa', 'sambar',
                  'rasam', 'kheer', 'tandoori', 'makhni', 'daal', 'dal',
                  'pulao', 'paneer', 'gobi', 'aaloo', 'bhindi', 'rava',
                  'malai' , 'kofta', 'sheera', 'puri', 'pani', 'masala dosa',
                  'namkeen', 'samosa', 'vada', 'chutney', 'bhurji', 'bhel', 'chaat',
                  'ragda', 'shev', 'choley', 'kulfi', 'lassi', 'gulab', 'jamun', 'kala',
                  'raj', 'bhog', 'bhajia', 'bhujia', 'rasgulla', 'rasmalai', 'sandesh',
                  'momo', 'tadka', 'kashmir', 'barfi', 'goan', 'south indian', 'north indian',
                  'rajasthani', 'jalebi', 'laddoo', 'papad', 'kolhapuri', 'raita', 'mangalorean',
                  'xacuti', 'rachedo', 'saag', 'sarso', 'gulkand', 'paan']


# count = 0
# with open(in_file, 'rb') as fp:
#     with open(temp_file, 'wb') as op:
#         for line in fp:
#             if '\0' in line:
#                 print("null")
#             else:
#                 op.write(line)
#
# print(count)

# count = 0
# with open(temp_file, 'rb') as fp:
#     reader = csv.reader(fp)
#     for row in reader:
#         print(row)
#         count += 1
#         if count == 5:
#             break


# with open(temp_file, 'rb') as in_fp:
#     reader = csv.reader(in_fp)
#
#     with open(out_file, 'wb') as out_fp:
#         writer = csv.writer(out_fp)
#         writer.writerow(['Handle', 'Username', 'UserID', 'Location', 'X_Cord', 'Y_Cord', 'TimeZone', 'DateTime', 'Namespace', 'TimeZone_2', 'Unknown', 'Unknown_2', 'Text'])
#
#         count = 0
#         for row in reader:
#             try:
#                 #print(row)
#                 writer.writerow(row)
#                 # count += 1
#                 # if count == 100:
#                 #     break
#                 #print(count)
#
#             except Exception as ex:
#                 print(ex, ex.message)
#                 count += 1
#                 continue
#
#     print("Complete!")

count = 0
classifier = Classifier()

with open(temp_file, 'rb') as fp:
    reader = csv.reader(fp)

    with open(indian_file, 'wb') as op:
        writer = csv.writer(op)
        writer.writerow(['Location', 'Text', 'Sentiment'])

        for row in reader:
            tweet_text = row[12]
            location = row[3]
            try:
                if any(word in tweet_text.lower().split() for word in indian_cuisine):
                    count += 1
                    sentiment = classifier.get_sentiment(tweet_text)
                    print("Done.. " + str(count))
                    sleep(0.5)
                    writer.writerow([location, tweet_text, sentiment])
            except Exception as ex:
                print("Error after: [" + str(count) + "] items. Msg: " + ex.message)
                sleep(5)
                continue
print(count)