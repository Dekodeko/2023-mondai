import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

t1strt = ["第１３回カール大帝とヨーロッパの始まり",
    "１．:red[［　A　］]人の大移動",
    "（１）原始ゲルマン人の社会　※印欧族のケルト人が広く居住",
    "①現在地　バルト海沿岸→紀元前後頃には、ライン川～ドナウ川の北方牧畜・農耕生活",
    "②平和的移動　人口増加・耕地不足→傭兵・:red[［　B　］]としてローマ帝国内に移住",
    "（２）ゲルマン人の移動と西ローマ帝国の滅亡",
    "①移動開始　:red[［　C　］]人（匈奴？）の西進→東ゴート征服→３７５年、西ゴート族の南下がきっかけ",
    "②ローマ帝国の分裂　３９５年、東西分裂→移動は西ローマに集中（以後２００年継続）",
    "③:red[［　D　］]の大帝国　５世紀前半成立（神の災い）→西ローマがゲルマンと結んで撃破"]
t1strat = ["ゲルマン","？？？","フン","アッティラ"]             #　正解答
anst1t = ['','','','']

st.subheader('歴史')
tab1, tab2, tab3 = st.tabs(["第１３回","第１４回","第１５回"])
with tab1:
    tab11, tab12, tab13 = st.tabs(["13-1","13-2","13-3"])
    with tab11:
        st.subheader(':blue[カール大帝とヨーロッパの始まり]')
        t1col1, t1col2 = st.columns([2, 1])
        for ws in t1strt:
            t1col1.caption(ws)
        t1col2.subheader("解答欄")
        anst1t[0] = t1col2.text_input(':red[［A］]', '')
        if anst1t[0] == t1strat[0]:
            t1col2.caption(':green[－ＯＫ－]')
        else:
            t1col2.caption(':violet[－ＮＧ－]')
        anst1t[1] = t1col2.text_input(':red[［B］]', '')
        if anst1t[1] == t1strat[1]:
            t1col2.caption(':green[－ＯＫ－]')
        else:
            t1col2.caption(':violet[－ＮＧ－]')
        anst1t[2] = t1col2.text_input(':red[［C］]', '')
        if anst1t[2] == t1strat[2]:
            t1col2.caption(':green[－ＯＫ－]')
        else:
            t1col2.caption(':violet[－ＮＧ－]')
        anst1t[3] = t1col2.text_input(':red[［D］]', '')
        if anst1t[3] == t1strat[3]:
            t1col2.caption(':green[－ＯＫ－]')
        else:
            t1col2.caption(':violet[－ＮＧ－]')

        expander = st.expander("答えを見る")
        expander.write('［Ａ］ゲルマン ［Ｂ］？？？ ［Ｃ］フン ［Ｄ］アッティラ')
    #    expander.image("https://static.streamlit.io/examples/dice.jpg")
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
