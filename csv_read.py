import csv
 
#with open('testdata.csv', encoding='utf-8', newline='') as f:
with open('testdata.csv',  newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)  # nextメソッドを使用して、ヘッダーの情報を読み込む
    id_header = header[0]
    name_header = header[1]
    age_header = header[2]
    prefecture_header = header[3]
    print("id_h",id_header)
    print("name_h",name_header)
    print("age_h",age_header)
    print("preference_h",prefecture_header)
    
    persons_dic = {}
    for row in reader:
        id = int(row[0])
        name = row[1]
        age = row[2]
        prefecture = row[3]
        p_dic = {}
        p_dic[id_header] = id
        p_dic[name_header] = name
        p_dic[age_header] = age
        p_dic[prefecture_header] = prefecture
        persons_dic[id] = p_dic
        print("row=",row)

print("person_dic=",persons_dic)
 
# 対象者の情報
# ID      :1
# 姓      :牛島
# 年齢    :36
# 都道府県:大分県
