import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit　超入門')
st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')

st.write('Interactive Widgets')

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    tab11, tab12, tab13 = st.tabs(["11", "12", "13"])
    with tab11:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

        st.header('This is a header')
        st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')

        st.subheader('This is a subheader')
        st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')

        st.caption('This is a string that explains something above.')
        st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

        st.text('This is some text.')

        st.latex(r'''
            a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
            \sum_{k=0}^{n-1} ar^k =
            a \left(\frac{1-r^{n}}{1-r}\right)
            ''')

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
    with tab12:
        st.header("tab12")
    with tab13:
        st.header("tab13")
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    expander1 = st.expander('問い合わせ1')
    expander1.write('問い合わせ1の回答')
    expander2 = st.expander('問い合わせ2')
    expander2.write('問い合わせ2の回答')
    expander3 = st.expander('問い合わせ3')
    expander3.write('問い合わせ3の回答')

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    left_column, right_column = st.columns(2)
    button = left_column.button('右カラムに、文字を表示')
    if button:
        right_column.write('ここは右カラム')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味は、',text,'です。'
# 'コンディション',condition

# st.sidebar.write('Interactive Widgets')

# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、',option,'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('ROSE.jpg')
#     st.image(img, caption='Rose', use_column_width=True)

