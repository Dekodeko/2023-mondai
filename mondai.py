import streamlit as st
import ast
# 定数
STR_ANSCL="解答欄(全角)"
STR_SEEANS = "答えを見る"
STR_OK = "－ＯＫ－"
STR_NG = "－ＮＧ－"
DSP_LCOL = 2   # 左表示カラム数
DSP_RCOL = 1   # 右表示カラム数
# main()
f = open('rekishi.txt', 'r', encoding='shift_jis')  # 問題データ一括読み込み
fstr = f.read()
print("file >",fstr)
f.close()
fddct = ast.literal_eval(fstr)    # 文字列から、辞書型へ
anst11 = [''] * len(fddct["asc11"])       # 13-1 問題数初期化　文字列リスト
anst12 = [''] * len(fddct["asc12"])       # 13-2 問題数初期化　文字列リスト
anst13 = [''] * len(fddct["asc13"])       # 13-3 問題数初期化　文字列リスト
anst14 = [''] * len(fddct["asc14"])       # 13-4 問題数初期化　文字列リスト
anst15 = [''] * len(fddct["asc15"])       # 13-5 問題数初期化　文字列リスト
anst16 = [''] * len(fddct["asc16"])       # 13-6 問題数初期化　文字列リスト

print("fddct= ",fddct)         # debug 
# print("fddct > ",type(fddct))
# val = fddct["title"]
# print('title = ',val)
# print('tabt >')
# for wstr in fddct["tabt"]:  print(wstr)
# print('tab1 >')
# for wstr in fddct["tab1"]:  print(wstr)
# print('pbs11 >')
# for wstr in fddct["pbs11"]: print(wstr)
# print('asc11 = ')
# for wstr in fddct["asc11"]:  print(wstr)
# print('ans11 = ')
# for wstr in fddct["ans11"]:   print(wstr)

st.subheader(fddct["title"])
tab1, tab2, tab3 = st.tabs([fddct["tabt"][0],fddct["tabt"][1],fddct["tabt"][2]])
with tab1:  #13
    tab11,tab12,tab13,tab14,tab15,tab16 = \
    st.tabs([fddct["tab1"][0],fddct["tab1"][1],fddct["tab1"][2],fddct["tab1"][3],fddct["tab1"][4],fddct["tab1"][5]])
    with tab11: # 13-1
        t11col1, t11col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs11"]:
            t11col1.caption(ws)
        t11col2.subheader(STR_ANSCL)
        for i,asc in enumerate(fddct["asc11"]):
            anst11[i] = t11col2.text_input(':red[［' + asc + '］]', '')
            if len(anst11[i]) == 0:
                ws = " "
            elif anst11[i] == fddct["ans11"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t11col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp11str = '　　'
        for asc,ans in zip(fddct["asc11"],fddct["ans11"]):
            exp11str = exp11str + '[' + asc + ']' + ans + '　'
        exp11str = exp11str+ '　　'
        expander.write(exp11str)
    with tab12: # 13-2
        t12col1, t12col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs12"]:
            t12col1.caption(ws)
        t12col2.subheader(STR_ANSCL)
        for i,asc in enumerate(fddct["asc12"]):
            anst12[i] = t12col2.text_input(':red[［' + asc + '］]', '')
            if len(anst12[i]) == 0:
                ws = " "
            elif anst12[i] == fddct["ans12"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t12col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp12str = '　　'
        for asc,ans in zip(fddct["asc12"],fddct["ans12"]):
            exp12str = exp12str + '[' + asc + ']' + ans + '　'
        exp12str = exp12str+ '　　'
        expander.write(exp12str)
    with tab13: # 13-3
        t13col1, t13col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs13"]:
            t13col1.caption(ws)
        t13col2.subheader(STR_ANSCL)
        for i,asc in enumerate(fddct["asc13"]):
            anst13[i] = t13col2.text_input(':red[［' + asc + '］]', '')
            if len(anst13[i]) == 0:
                ws = " "
            elif anst13[i] == fddct["ans13"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t13col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp13str = '　　'
        for asc,ans in zip(fddct["asc13"],fddct["ans13"]):
            exp13str = exp13str + '[' + asc + ']' + ans + '　'
        exp13str = exp13str+ '　　'
        expander.write(exp13str)
    with tab14: # 13-4
        t14col1, t14col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs14"]:
            t14col1.caption(ws)
        t14col2.subheader(STR_ANSCL)
        for i,asc in enumerate(fddct["asc14"]):
            anst14[i] = t14col2.text_input(':red[［' + asc + '］]', '')
            if len(anst14[i]) == 0:
                ws = " "
            elif anst14[i] == fddct["ans14"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t14col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp14str = '　　'
        for asc,ans in zip(fddct["asc14"],fddct["ans14"]):
            exp14str = exp14str + '[' + asc + ']' + ans + '　'
        exp14str = exp14str+ '　　'
        expander.write(exp14str)
    with tab15: # 13-5
        t15col1, t15col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs15"]:
            t15col1.caption(ws)
        t15col2.subheader(STR_ANSCL)
        for i,asc in enumerate(fddct["asc15"]):
            anst15[i] = t15col2.text_input(':red[［' + asc + '］]', '')
            if len(anst15[i]) == 0:
                ws = " "
            elif anst15[i] == fddct["ans15"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t15col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp15str = '　　'
        for asc,ans in zip(fddct["asc15"],fddct["ans15"]):
            exp15str = exp15str + '[' + asc + ']' + ans + '　'
        exp15str = exp15str+ '　　'
        expander.write(exp15str)
    with tab16: # 13-6
        t16col1, t16col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs16"]:
            t16col1.caption(ws)
        t16col2.subheader(STR_ANSCL)
        for i,asc in enumerate(fddct["asc16"]):
            anst16[i] = t16col2.text_input(':red[［' + asc + '］]', '')
            if len(anst16[i]) == 0:
                ws = " "
            elif anst16[i] == fddct["ans16"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t16col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp16str = '　　'
        for asc,ans in zip(fddct["asc16"],fddct["ans16"]):
            exp16str = exp16str + '[' + asc + ']' + ans + '　'
        exp16str = exp16str+ '　　'
        expander.write(exp16str)
with tab2:
    st.subheader(":blue[インダス文明とアーリヤ人の社会]")
with tab3:
    st.subheader(':blue[古代インドと東南アジア]')
