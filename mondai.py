import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

t1strt = ["第１３回カール大帝とヨーロッパの始まり",
    "１．［　　A　　］人の大移動",
    "（１）原始ゲルマン人の社会　※印欧族のケルト人が広く居住",
    "①現在地　バルト海沿岸→紀元前後頃には、ライン川～ドナウ川の北方牧畜・農耕生活",
    "②平和的移動　人口増加・耕地不足→傭兵・［　　B　　］としてローマ帝国内に移住",
    "（２）ゲルマン人の移動と西ローマ帝国の滅亡",
    "①移動開始　［　C　］人（匈奴？）の西進→東ゴート征服→３７５年、西ゴート族の南下がきっかけ",
    "②ローマ帝国の分裂　３９５年、東西分裂→移動は西ローマに集中（以後２００年継続）",
    "③［　D　］の大帝国　５世紀前半成立（神の災い）→西ローマがゲルマンと結んで撃破"]
t1strat = ["ゲルマン","？？？","フン","アッティラ"]             #　正解答
anst1t = ['','','','']

st.title('歴史')
tab1, tab2, tab3 = st.tabs(["第１３回","第１４回","第１５回"])

with tab1:
    st.subheader(':blue[カール大帝とヨーロッパの始まり]')
    t1col1, t1col2 = st.columns([2, 1])
    for ws in t1strt:
        t1col1.caption(ws)
    t1col2.subheader("解答欄")
    anst1t[0] = t1col2.text_input('[A]', '')
    if anst1t[0] == t1strat[0]:
        t1col2.caption(':green[－ＯＫ－]')
    else:
        t1col2.caption(':red[－ＮＧ－]')
    anst1t[1] = t1col2.text_input('[B]', '')
    if anst1t[1] == t1strat[1]:
        t1col2.caption(':green[－ＯＫ－]')
    else:
        t1col2.caption(':red[－ＮＧ－]')
    anst1t[2] = t1col2.text_input('[C]', '')
    if anst1t[2] == t1strat[2]:
        t1col2.caption(':green[－ＯＫ－]')
    else:
        t1col2.caption(':red[－ＮＧ－]')
    anst1t[3] = t1col2.text_input('[D]', '')
    if anst1t[3] == t1strat[3]:
        t1col2.caption(':green[－ＯＫ－]')
    else:
        t1col2.caption(':red[－ＮＧ－]')

#    ta = t1col2.caption('[ A ]')

    st.caption('This is a string that explains something above.')

    st.text('This is some text.')

    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')

    kotae = '昭和'
    ans01 = st.text_input('答え', '')
    if ans01 == kotae:
        st.write('当たり', ':blue[' + ans01 + ']')
    else:
        st.write('はずれ', ':red[' + ans01 + ']')
        
with tab2:
    st.header(":blue[インダス文明とアーリヤ人の社会]")
    st.subheader('This is a subheader')

with tab3:
    st.header(':blue[古代インドと東南アジア]')
    st.subheader('This is a subheader')