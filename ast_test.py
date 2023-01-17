import ast

tbl = '{"title":"歴史",\
        "tabt":["第１３回","第１４回","第１５回"],\
        "tab1":["13-1","13-2","13-3"],\
        "pbs11":["第１３回カール大帝とヨーロッパの始まり",\
		"１．:red[［　A　］]人の大移動",\
		"（１）原始ゲルマン人の社会　※印欧族のケルト人が広く居住",\
		"①現在地　バルト海沿岸→紀元前後頃には、ライン川～ドナウ川の北方牧畜・農耕生活",\
		"②平和的移動　人口増加・耕地不足→傭兵・:red[［　B　］]としてローマ帝国内に移住",\
		"（２）ゲルマン人の移動と西ローマ帝国の滅亡"\
	    "①移動開始　:red[［　C　］]人（匈奴？）の西進→東ゴート征服→３７５年、西ゴート族の南下がきっかけ",\
	    "②ローマ帝国の分裂　３９５年、東西分裂→移動は西ローマに集中（以後２００年継続）",\
	    "③:red[［　D　］]の大帝国　５世紀前半成立（神の災い）→西ローマがゲルマンと結んで撃破"]\
		],\
        "asc11":["A","B","C","D"],\
        "ans11":["ゲルマン","？？？","フン","アッティラ"]\
    }'

f = open('rekishi3.txt', 'r', encoding='shift_jis')
fstr = f.read()
print("file >",fstr)
f.close()

#fddct = ast.literal_eval(tbl)    # 文字列から、辞書型へ
fddct = ast.literal_eval(fstr)    # 文字列から、辞書型へ
print("fddct= ",fddct)
print("fddct > ",type(fddct))
val = fddct["title"]
print('title = ',val)
print('tabt >')
for wstr in fddct["tabt"]:  print(wstr)
print('tab1 >')
for wstr in fddct["tab1"]:  print(wstr)
print('pbs11 >')
for wstr in fddct["pbs11"]: print(wstr)
print('asc11 = ')
for wstr in fddct["asc11"]:  print(wstr)
print('ans11 = ')
for wstr in fddct["ans11"]:   print(wstr)
