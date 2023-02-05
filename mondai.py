import streamlit as st
import ast
# constant
STR_ANSCL="解答欄(全角)"
STR_SEEANS = "答えを見る"
STR_OK = "－ＯＫ－"
STR_NG = "－ＮＧ－"
DSP_LCOL = 2   # 左表示カラム数
DSP_RCOL = 1   # 右表示カラム数
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
anst41 = [''] * len(fddct["asc41"])       # 16-1 問題数初期化　文字列リスト
anst42 = [''] * len(fddct["asc42"])       # 16-2 問題数初期化　文字列リスト
anst43 = [''] * len(fddct["asc43"])       # 16-3 問題数初期化　文字列リスト
anst44 = [''] * len(fddct["asc44"])       # 16-4 問題数初期化　文字列リスト
anst45 = [''] * len(fddct["asc45"])       # 16-5 問題数初期化　文字列リスト
anst51 = [''] * len(fddct["asc51"])       # 17-1 問題数初期化　文字列リスト
anst52 = [''] * len(fddct["asc52"])       # 17-2 問題数初期化　文字列リスト
anst53 = [''] * len(fddct["asc53"])       # 17-3 問題数初期化　文字列リスト
anst54 = [''] * len(fddct["asc54"])       # 17-4 問題数初期化　文字列リスト
anst55 = [''] * len(fddct["asc55"])       # 17-5 問題数初期化　文字列リスト
anst56 = [''] * len(fddct["asc56"])       # 17-5 問題数初期化　文字列リスト
anst61 = [''] * len(fddct["asc61"])       # 18-1 問題数初期化　文字列リスト
anst62 = [''] * len(fddct["asc62"])       # 18-2 問題数初期化　文字列リスト
anst63 = [''] * len(fddct["asc63"])       # 18-3 問題数初期化　文字列リスト
anst64 = [''] * len(fddct["asc64"])       # 18-4 問題数初期化　文字列リスト
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
# ------------------------------------------------------------------------------------
st.write(fddct["title"])
tab1, tab2, tab3, tab4, tab5, tab6 = \
    st.tabs([fddct["tabt"][0],fddct["tabt"][1],fddct["tabt"][2],fddct["tabt"][3],fddct["tabt"][4],fddct["tabt"][5]])
with tab1:  #13
    tab11,tab12,tab13,tab14,tab15,tab16 = \
    st.tabs([fddct["tab1"][0],fddct["tab1"][1],fddct["tab1"][2],fddct["tab1"][3],fddct["tab1"][4],fddct["tab1"][5]])
    with tab11: # 13-1
        t11col1, t11col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t11col1, t11col2, fddct["pbs11"], fddct["asc11"], fddct["ans11"] )
    with tab12: # 13-2
        t12col1, t12col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t12col1, t12col2, fddct["pbs12"], fddct["asc12"], fddct["ans12"] )
    with tab13: # 13-3
        t13col1, t13col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t13col1, t13col2, fddct["pbs13"], fddct["asc13"], fddct["ans13"] )
    with tab14: # 13-4
        t14col1, t14col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t14col1, t14col2, fddct["pbs14"], fddct["asc14"], fddct["ans14"] )
    with tab15: # 13-5
        t15col1, t15col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t15col1, t15col2, fddct["pbs15"], fddct["asc15"], fddct["ans15"] )
    with tab16: # 13-6
        t16col1, t16col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t16col1, t16col2, fddct["pbs16"], fddct["asc16"], fddct["ans16"] )
with tab2:  #14
    tab21,tab22,tab23,tab24,tab25,tab26,tab27,tab28,tab29 = \
    st.tabs([fddct["tab2"][0],fddct["tab2"][1],fddct["tab2"][2],fddct["tab2"][3],fddct["tab2"][4] \
             ,fddct["tab2"][5],fddct["tab2"][6],fddct["tab2"][7],fddct["tab2"][8]])
    with tab21: # 14-1
        t21col1, t21col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t21col1, t21col2, fddct["pbs21"], fddct["asc21"], fddct["ans21"] )
    with tab22: # 14-2
        t22col1, t22col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t22col1, t22col2, fddct["pbs22"], fddct["asc22"], fddct["ans22"] )
    with tab23: # 14-3
        t23col1, t23col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t23col1, t23col2, fddct["pbs23"], fddct["asc23"], fddct["ans23"] )
    with tab24: # 14-4
        t24col1, t24col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t24col1, t24col2, fddct["pbs24"], fddct["asc24"], fddct["ans24"] )
    with tab25: # 14-5
        t25col1, t25col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t25col1, t25col2, fddct["pbs25"], fddct["asc25"], fddct["ans25"] )
    with tab26: # 14-6
        t26col1, t26col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t26col1, t26col2, fddct["pbs26"], fddct["asc26"], fddct["ans26"] )
    with tab27: # 14-7
        t27col1, t27col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t27col1, t27col2, fddct["pbs27"], fddct["asc27"], fddct["ans27"] )
    with tab28: # 14-8
        t28col1, t28col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t28col1, t28col2, fddct["pbs28"], fddct["asc28"], fddct["ans28"] )
    with tab29: # 14-9
        t29col1, t29col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t29col1, t29col2, fddct["pbs29"], fddct["asc29"], fddct["ans29"] )
with tab3:  #15
    tab31,tab32,tab33,tab34,tab35 = \
    st.tabs([fddct["tab3"][0],fddct["tab3"][1],fddct["tab3"][2],fddct["tab3"][3],fddct["tab3"][4]])
    with tab31: # 15-1
        t31col1, t31col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t31col1, t31col2, fddct["pbs31"], fddct["asc31"], fddct["ans31"] )
    with tab32: # 15-2
        t32col1, t32col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t32col1, t32col2, fddct["pbs32"], fddct["asc32"], fddct["ans32"] )
    with tab33: # 15-3
        t33col1, t33col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t33col1, t33col2, fddct["pbs33"], fddct["asc33"], fddct["ans33"] )
    with tab34: # 15-4
        t34col1, t34col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t34col1, t34col2, fddct["pbs34"], fddct["asc34"], fddct["ans34"] )
    with tab35: # 15-5
        t35col1, t35col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t35col1, t35col2, fddct["pbs35"], fddct["asc35"], fddct["ans35"] )
with tab4:  #16
    tab41,tab42,tab43,tab44,tab45 = \
    st.tabs([fddct["tab4"][0],fddct["tab4"][1],fddct["tab4"][2],fddct["tab4"][3],fddct["tab4"][4]])
    with tab41: # 16-1
        t41col1, t41col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t41col1, t41col2, fddct["pbs41"], fddct["asc41"], fddct["ans41"] )
    with tab42: # 16-2
        t42col1, t42col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t42col1, t42col2, fddct["pbs42"], fddct["asc42"], fddct["ans42"] )
    with tab43: # 16-3
        t43col1, t43col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t43col1, t43col2, fddct["pbs43"], fddct["asc43"], fddct["ans43"] )
    with tab44: # 16-4
        t44col1, t44col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t44col1, t44col2, fddct["pbs44"], fddct["asc44"], fddct["ans44"] )
    with tab45: # 16-5
        t45col1, t45col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t45col1, t45col2, fddct["pbs45"], fddct["asc45"], fddct["ans45"] )
with tab5:  #17
    tab51,tab52,tab53,tab54,tab55 = \
    st.tabs([fddct["tab5"][0],fddct["tab5"][1],fddct["tab5"][2],fddct["tab5"][3],fddct["tab5"][4]])
    with tab51: # 17-1
        t51col1, t51col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t51col1, t51col2, fddct["pbs51"], fddct["asc51"], fddct["ans51"] )
    with tab52: # 17-2
        t52col1, t52col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t52col1, t52col2, fddct["pbs52"], fddct["asc52"], fddct["ans52"] )
    with tab53: # 17-3
        t53col1, t53col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t53col1, t53col2, fddct["pbs53"], fddct["asc53"], fddct["ans53"] )
    with tab54: # 17-4
        t54col1, t54col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t54col1, t54col2, fddct["pbs54"], fddct["asc54"], fddct["ans54"] )
    with tab55: # 17-5
        t55col1, t55col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t55col1, t55col2, fddct["pbs55"], fddct["asc55"], fddct["ans55"] )
with tab6:  #18
    tab61,tab62,tab63,tab64 = \
    st.tabs([fddct["tab6"][0],fddct["tab6"][1],fddct["tab6"][2],fddct["tab6"][3]])
    with tab61: # 18-1
        t61col1, t61col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t61col1, t61col2, fddct["pbs61"], fddct["asc61"], fddct["ans61"] )
    with tab62: # 18-2
        t62col1, t62col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t62col1, t62col2, fddct["pbs62"], fddct["asc62"], fddct["ans62"] )
    with tab63: # 18-3
        t63col1, t63col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t63col1, t63col2, fddct["pbs63"], fddct["asc63"], fddct["ans63"] )
    with tab64: # 18-4
        t64col1, t64col2 = st.columns([DSP_LCOL, DSP_RCOL])
        sub_test(t64col1, t64col2, fddct["pbs64"], fddct["asc64"], fddct["ans64"] )