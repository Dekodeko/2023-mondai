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
anst12 = [''] * len(fddct["asc12"])       # 13-2 問題数初期化　文字列リスト
anst13 = [''] * len(fddct["asc13"])       # 13-3 問題数初期化　文字列リスト
anst14 = [''] * len(fddct["asc14"])       # 13-4 問題数初期化　文字列リスト
anst15 = [''] * len(fddct["asc15"])       # 13-5 問題数初期化　文字列リスト
anst16 = [''] * len(fddct["asc16"])       # 13-6 問題数初期化　文字列リスト
anst21 = [''] * len(fddct["asc21"])       # 14-1 問題数初期化　文字列リスト
anst22 = [''] * len(fddct["asc22"])       # 14-2 問題数初期化　文字列リスト
anst23 = [''] * len(fddct["asc23"])       # 14-3 問題数初期化　文字列リスト
anst24 = [''] * len(fddct["asc24"])       # 14-4 問題数初期化　文字列リスト
anst25 = [''] * len(fddct["asc25"])       # 14-5 問題数初期化　文字列リスト
anst26 = [''] * len(fddct["asc26"])       # 14-6 問題数初期化　文字列リスト
anst31 = [''] * len(fddct["asc31"])       # 15-1 問題数初期化　文字列リスト
anst32 = [''] * len(fddct["asc32"])       # 15-2 問題数初期化　文字列リスト
anst33 = [''] * len(fddct["asc33"])       # 15-3 問題数初期化　文字列リスト
anst34 = [''] * len(fddct["asc34"])       # 15-4 問題数初期化　文字列リスト
anst35 = [''] * len(fddct["asc35"])       # 15-5 問題数初期化　文字列リスト

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
        for ws in fddct["pbs12"]:
            t12col1.caption(ws)
        t12col2.caption(STR_ANSCL)
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
        t13col2.caption(STR_ANSCL)
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
        t14col2.caption(STR_ANSCL)
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
        t15col2.caption(STR_ANSCL)
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
        t16col2.caption(STR_ANSCL)
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
    tab21,tab22,tab23,tab24,tab25,tab26 = \
    st.tabs([fddct["tab2"][0],fddct["tab2"][1],fddct["tab2"][2],fddct["tab2"][3],fddct["tab2"][4],fddct["tab2"][5]])
    with tab21: # 14-1
        t21col1, t21col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs21"]:
            t21col1.caption(ws)
        t21col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc21"]):
            anst21[i] = t21col2.text_input(':red[［' + asc + '］]', '')
            if len(anst21[i]) == 0:
                ws = " "
            elif anst21[i] == fddct["ans21"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t21col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp21str = '　　'
        for asc,ans in zip(fddct["asc21"],fddct["ans21"]):
            exp21str = exp21str + '[' + asc + ']' + ans + '　'
        exp21str = exp21str+ '　　'
        expander.write(exp21str)
    with tab22: # 14-2
        t22col1, t22col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs22"]:
            t22col1.caption(ws)
        t22col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc22"]):
            anst22[i] = t22col2.text_input(':red[［' + asc + '］]', '')
            if len(anst22[i]) == 0:
                ws = " "
            elif anst22[i] == fddct["ans22"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t22col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp22str = '　　'
        for asc,ans in zip(fddct["asc22"],fddct["ans22"]):
            exp22str = exp22str + '[' + asc + ']' + ans + '　'
        exp22str = exp22str+ '　　'
        expander.write(exp22str)
    with tab23: # 14-3
        t23col1, t23col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs23"]:
            t23col1.caption(ws)
        t23col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc23"]):
            anst23[i] = t23col2.text_input(':red[［' + asc + '］]', '')
            if len(anst23[i]) == 0:
                ws = " "
            elif anst23[i] == fddct["ans23"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t23col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp23str = '　　'
        for asc,ans in zip(fddct["asc23"],fddct["ans23"]):
            exp23str = exp23str + '[' + asc + ']' + ans + '　'
        exp23str = exp23str+ '　　'
        expander.write(exp23str)
    with tab24: # 14-4
        t24col1, t24col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs24"]:
            t24col1.caption(ws)
        t24col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc24"]):
            anst24[i] = t24col2.text_input(':red[［' + asc + '］]', '')
            if len(anst24[i]) == 0:
                ws = " "
            elif anst24[i] == fddct["ans24"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t24col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp24str = '　　'
        for asc,ans in zip(fddct["asc24"],fddct["ans24"]):
            exp24str = exp24str + '[' + asc + ']' + ans + '　'
        exp24str = exp24str+ '　　'
        expander.write(exp24str)
    with tab25: # 14-5
        t25col1, t25col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs25"]:
            t25col1.caption(ws)
        t25col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc25"]):
            anst25[i] = t25col2.text_input(':red[［' + asc + '］]', '')
            if len(anst25[i]) == 0:
                ws = " "
            elif anst25[i] == fddct["ans25"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t25col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp25str = '　　'
        for asc,ans in zip(fddct["asc25"],fddct["ans25"]):
            exp25str = exp25str + '[' + asc + ']' + ans + '　'
        exp25str = exp25str+ '　　'
        expander.write(exp25str)        
    with tab26: # 14-6
        t26col1, t26col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs26"]:
            t26col1.caption(ws)
        t26col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc26"]):
            anst26[i] = t26col2.text_input(':red[［' + asc + '］]', '')
            if len(anst26[i]) == 0:
                ws = " "
            elif anst26[i] == fddct["ans26"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t26col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp26str = '　　'
        for asc,ans in zip(fddct["asc26"],fddct["ans26"]):
            exp26str = exp26str + '[' + asc + ']' + ans + '　'
        exp26str = exp26str+ '　　'
        expander.write(exp26str)
with tab3:
    tab31,tab32,tab33,tab34,tab35 = \
    st.tabs([fddct["tab3"][0],fddct["tab3"][1],fddct["tab3"][2],fddct["tab3"][3],fddct["tab3"][4]])
    with tab31: # 15-1
        t31col1, t31col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs31"]:
            t31col1.caption(ws)
        t31col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc31"]):
            anst31[i] = t31col2.text_input(':red[［' + asc + '］]', '')
            if len(anst31[i]) == 0:
                ws = " "
            elif anst31[i] == fddct["ans31"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t31col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp31str = '　　'
        for asc,ans in zip(fddct["asc31"],fddct["ans31"]):
            exp31str = exp31str + '[' + asc + ']' + ans + '　'
        exp31str = exp31str+ '　　'
        expander.write(exp31str)
    with tab32: # 15-2
        t32col1, t32col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs32"]:
            t32col1.caption(ws)
        t32col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc32"]):
            anst32[i] = t32col2.text_input(':red[［' + asc + '］]', '')
            if len(anst32[i]) == 0:
                ws = " "
            elif anst32[i] == fddct["ans32"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t32col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp32str = '　　'
        for asc,ans in zip(fddct["asc32"],fddct["ans32"]):
            exp32str = exp32str + '[' + asc + ']' + ans + '　'
        exp32str = exp32str+ '　　'
        expander.write(exp32str)
    with tab33: # 15-3
        t33col1, t33col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs33"]:
            t33col1.caption(ws)
        t33col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc33"]):
            anst33[i] = t33col2.text_input(':red[［' + asc + '］]', '')
            if len(anst33[i]) == 0:
                ws = " "
            elif anst33[i] == fddct["ans33"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t33col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp33str = '　　'
        for asc,ans in zip(fddct["asc33"],fddct["ans33"]):
            exp33str = exp33str + '[' + asc + ']' + ans + '　'
        exp33str = exp33str+ '　　'
        expander.write(exp33str)
    with tab34: # 15-4
        t34col1, t34col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs34"]:
            t34col1.caption(ws)
        t34col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc34"]):
            anst34[i] = t34col2.text_input(':red[［' + asc + '］]', '')
            if len(anst34[i]) == 0:
                ws = " "
            elif anst34[i] == fddct["ans34"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t34col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp34str = '　　'
        for asc,ans in zip(fddct["asc34"],fddct["ans34"]):
            exp34str = exp34str + '[' + asc + ']' + ans + '　'
        exp34str = exp34str+ '　　'
        expander.write(exp34str)
with tab35: # 15-5
        t35col1, t35col2 = st.columns([DSP_LCOL, DSP_RCOL])
        for ws in fddct["pbs35"]:
            t35col1.caption(ws)
        t35col2.caption(STR_ANSCL)
        for i,asc in enumerate(fddct["asc35"]):
            anst35[i] = t35col2.text_input(':red[［' + asc + '］]', '')
            if len(anst35[i]) == 0:
                ws = " "
            elif anst35[i] == fddct["ans35"][i]:
                ws = ':green[' + STR_OK + ']'
            else:
                ws = ':violet[' + STR_NG + ']'
            t35col2.caption(ws)
        expander = st.expander(STR_SEEANS)
        exp35str = '　　'
        for asc,ans in zip(fddct["asc35"],fddct["ans35"]):
            exp35str = exp35str + '[' + asc + ']' + ans + '　'
        exp35str = exp35str+ '　　'
        expander.write(exp35str)