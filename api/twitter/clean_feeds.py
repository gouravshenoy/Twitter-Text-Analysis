__author__ = 'Gaurav-PC'

import csv
from time import sleep
from locations import Locations
from sentiment.classifier import Classifier
from sentiment.indico_sentiment_analyser import IndicoSentimentAnalyser

in_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\cuisine_dataset.csv"
out_file = "cuisine_dataset_with_header.csv"
temp_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\cuisine_dataset_clean.csv"

# cuisine files
indian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\indian.csv"
italian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\italian.csv"
mideast_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\mideast.csv"
chinese_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\chinese.csv"

indian_cuisine = ['biryani', 'indian', 'india', 'masala', 'tikka',
                  'naan', 'kulcha', 'upma', 'idli', 'dosa', 'sambar',
                  'rasam', 'kheer', 'tandoori', 'makhni', 'daal', 'dal',
                  'pulao', 'paneer', 'gobi', 'aaloo', 'bhindi', 'rava',
                  'malai', 'kofta', 'sheera', 'puri', 'pani', 'masala dosa',
                  'namkeen', 'samosa', 'vada', 'chutney', 'bhurji', 'bhel', 'chaat',
                  'ragda', 'shev', 'choley', 'kulfi', 'lassi', 'gulab', 'jamun', 'kala',
                  'raj', 'bhog', 'bhajia', 'bhujia', 'rasgulla', 'rasmalai', 'sandesh',
                  'momo', 'tadka', 'kashmir', 'barfi', 'goan', 'south indian', 'north indian',
                  'rajasthani', 'jalebi', 'laddoo', 'papad', 'kolhapuri', 'raita', 'mangalorean',
                  'xacuti', 'rachedo', 'saag', 'sarso', 'gulkand', 'paan']

italian_cuisine = ['italy', 'italian', 'spain', 'spanish', 'pizza', 'cheeze', 'pasta', 'spaghetti', 'breadstick',
                   'alfredo', 'antipasti', 'bruschetta', 'capicollo', 'insalata capreses', 'mozzarelline',
                   'fitte', 'mozzarella', 'olives', 'prosciutto', 'salami', 'nervetti', 'bari', 'biga', 'buccellato',
                   'casatiello', 'ciabatta', 'ciaccino', 'ciriola', 'colimba', 'pasquale', 'crocche', 'farinata',
                   'acquacotta', 'bagna', 'cauda', 'garmugia', 'minestrone', 'fagioli', 'grine', 'straciatella',
                   'marinara', 'siciliana', 'pugilese', 'capricciosa', 'quatrro', 'formaggi', 'ziti', 'ravioli',
                   'carbonara', 'risotto', 'vitello', 'rosetta', 'pita', 'lasagne']

mid_east_cuisine = ['hummus', 'manakeesh', 'halloumi', 'meddamas', 'falafel', 'tabouleh', 'moutabal', 'ghanoush',
                    'fattoush', 'shanklish',
                    'shawarma', 'shish', 'tawook', 'dolma', 'kofta', 'quwarmah', 'dajaj', 'mansaf', 'baklava', 'knafeh',
                    'masgouf', 'qaimar',
                    'lablabi', 'kishta', 'shineena', 'laban', 'musakhan', 'mujaddara', 'aseed', 'fahsa', 'thareed',
                    'samak', 'mofa', 'mandi',
                    'fattah', 'shakshouka', 'kabsa', 'jachnun']

chinese_cuisine = ['china', 'chinese', 'beijing', 'asian', 'shangai','pork', 'gong', 'bao', 'chicken', 'tofu', 'wonton',
                   'dumpling', 'chowmein', 'chow', 'mein', 'rangoon', 'teriyaki', 'sushi',
                   'spring', 'roll', 'peking' 'roasted' 'duck', 'hunan',
                   'bamboo', 'noodle', 'sichuan', 'chengdu', 'chilli',
                   'beef', 'lamian', 'zhajiangmian', 'char', 'siu', 'egg', 'peking', 'soy', 'buddha',
                   'stir', 'fry', 'stirfry', 'Baozi', 'dim', 'sum', 'guotie', 'jiaozi', 'mantou', 'wonton',
                   'xiaolongbao', 'zongzi', 'sachima', 'shaobing', 'youtiao', 'congee', 'pot', 'tong', 'sui',
                   'pumpkin', 'rabbit', 'cantonese', 'roast', 'pig', 'seafood',
                   'shark', 'yeung', 'yusheng', 'popiah', 'fujian', 'oyster', 'omlette', 'wine', 'hainanese', 'wengchang',
                   'jiangsu', 'shangdong', 'fuqi', 'feipian', 'dandan', 'dandan', 'chongqing', 'mapo', 'shuizhu', 'zhangcha']


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
diff_count = 0
classifier = Classifier()
analyser = IndicoSentimentAnalyser()
locations = Locations()

with open(temp_file, 'rb') as fp:
    reader = csv.reader(fp)

    with open(chinese_file, 'wb') as op:
        writer = csv.writer(op)
        writer.writerow(['Date', 'Location', 'Country', 'Text', 'Sentiment'])

        for row in reader:
            tweet_text = row[12]
            location = row[3]
            date = row[7]
            country = locations.get_country(location=location)

            try:
                if any(word in tweet_text.lower().split() for word in chinese_cuisine):
                    """
                    small code to cover up for last failure
                    """
                    count += 1
                    # diff_count += 1
                    # if diff_count < 8234:
                    #     continue

                    # sentiment = classifier.get_sentiment(tweet_text)
                    sentiment = analyser.analyse_sentiment(text=tweet_text)
                    writer.writerow([date, location, country, tweet_text, sentiment])
                    print("Done.. " + str(count))
            except Exception as ex:
                print("Error after: [" + str(count) + "] items. Msg: " + str(ex.message))
                sleep(5)
                continue
print(count)
