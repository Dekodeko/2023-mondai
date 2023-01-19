import streamlit as st
import ast

anst1t = ['','','','']
STR_ANSCL="解答欄"
STR_OK = "－ＯＫ－"
STR_NG = "－ＮＧ－"
f = open('rekishi.txt', 'r', encoding='shift_jis')
fstr = f.read()
print("file >",fstr)
f.close()
fddct = ast.literal_eval(fstr)    # 文字列から、辞書型へ
print("fddct= ",fddct)
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
with tab1:
    tab11, tab12, tab13 = st.tabs([fddct["tab1"][0],fddct["tab1"][1],fddct["tab1"][2]])
    with tab11:
        t1col1, t1col2 = st.columns([2, 1])
        for ws in fddct["pbs11"]:
            t1col1.caption(ws)
        t1col2.subheader(STR_ANSCL)
        anst1t[0] = t1col2.text_input(':red[［'+fddct["asc11"][0]+'］]', '')
        if anst1t[0] == fddct["ans11"][0]:
            t1col2.caption(':green[' + STR_OK + ']')
        else:
            t1col2.caption(':violet[' + STR_NG + ']')
        anst1t[1] = t1col2.text_input(':red[［'+fddct["asc11"][1]+'］]', '')
        if anst1t[1] == fddct["ans11"][1]:
            t1col2.caption(':green[' + STR_OK + ']')
        else:
            t1col2.caption(':violet[' + STR_NG + ']')
        anst1t[2] = t1col2.text_input(':red[［'+fddct["asc11"][2]+'］]', '')
        if anst1t[2] == fddct["ans11"][2]:
            t1col2.caption(':green[' + STR_OK + ']')
        else:
            t1col2.caption(':violet[' + STR_NG + ']')
        anst1t[3] = t1col2.text_input(':red[［'+fddct["asc11"][3]+'］]', '')
        if anst1t[3] == fddct["ans11"][3]:
            t1col2.caption(':green[' + STR_OK + ']')
        else:
            t1col2.caption(':violet[' + STR_NG + ']')
        expander = st.expander("答えを見る")
        exp11str = '　　'
        for i in range(4):
            exp11str = exp11str + '[' + fddct["asc11"][i] + ']' + fddct["ans11"][i] + '　'
        exp11str = exp11str+ '　　'
        expander.write(exp11str)
    with tab12:
        st.subheader(':blue[カール大帝とヨーロッパの始まり]')
        st.subheader(":blue[1-2]")
    with tab13:
        st.subheader(':blue[カール大帝とヨーロッパの始まり]')
        st.subheader(":blue[1-3]")
with tab2:
    st.subheader(":blue[インダス文明とアーリヤ人の社会]")
with tab3:
    st.subheader(':blue[古代インドと東南アジア]')
