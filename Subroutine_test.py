import streamlit as st
import ast
# constant
STR_ANSCL="解答欄(全角)"
STR_SEEANS = "答えを見る"
STR_OK = "－ＯＫ－"
STR_NG = "－ＮＧ－"
DSP_LCOL = 2   # 左表示カラム数
DSP_RCOL = 1   # 右表示カラム数
# main
f = open('rekishi.txt', 'r', encoding='shift_jis')  # 問題データ一括読み込み
fstr = f.read()
# print("file >",fstr)
f.close()
fddct = ast.literal_eval(fstr)    # 文字列から、辞書型へ
anst11 = [''] * len(fddct["asc11"])       # 13-1 問題数初期化　文字列リスト

# print("fddct= ",fddct)         # debug 
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
#          pointer,pointer,list,list, 

# subroutine
def sub_test(tcol1, tcol2, pbst, asct, anst): # 各タブ画面の表示入力サブ
    ansit = [''] * len(anst)       # 問題数初期化　文字列リスト
    for ws in pbst:
        tcol1.caption(ws)
    tcol2.caption(STR_ANSCL)
    for i,asc in enumerate(asct):
        ansit[i] = tcol2.text_input(':red[［' + asc + '］]', '')
        if len(ansit[i]) == 0:
            ws = " "
        elif ansit[i] == anst[i]:
            ws = ':green[' + STR_OK + ']'
        else:
            ws = ':violet[' + STR_NG + ']'
        tcol2.caption(ws)
    expander = st.expander(STR_SEEANS)
    expstr = '　　'
    for asc,ans in zip(asct,anst):
        expstr = expstr + '[' + asc + ']' + ans + '　'
    expstr = expstr+ '　　'
    expander.write(expstr)
# main
st.subheader(fddct["title"])
tab1, tab2, tab3 = st.tabs([fddct["tabt"][0],fddct["tabt"][1],fddct["tabt"][2]])
with tab1:  #13
    tab11,tab12,tab13,tab14,tab15,tab16 = \
    st.tabs([fddct["tab1"][0],fddct["tab1"][1],fddct["tab1"][2],fddct["tab1"][3],fddct["tab1"][4],fddct["tab1"][5]])
    with tab11: # 13-1
        t11col1, t11col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs11"]:
            t11col1.caption(ws)
        t11col2.caption(STR_ANSCL)
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
        sub_test(t12col1, t12col2, fddct["pbs12"], fddct["asc12"], fddct["ans12"] )
    with tab13: # 13-3
        t13col1, t13col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t13col1, t13col2, fddct["pbs13"], fddct["asc13"], fddct["ans13"] )