import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# タイトル
st.title('Streamlit 超入門')
'Start!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!'
# 表
st.write('DataFrame')
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})
st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=100, height=200)
st.table(df.style.highlight_max(axis=0))

# マークダウン
"""
# 章
## 節
### 項

''' python
import streamlit as st
import numpy as np
import pandas as pd
'''
"""
# グラフ
st.write('DataFrame')
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df)
st.bar_chart(df)

# map
st.write('DataFrame')
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
    columns=['lat', 'lon']
)
df
st.map(df)

# 言葉 sidebar付けるとサイドに行く。
st.sidebar.write('sidebar')
# 画像
st.write('Display Image')
img = Image.open('neoki6.jpg')
st.image(img, caption='neko', use_column_width=True)
# チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('neoki6.jpg')
    st.image(img, caption='neko', use_column_width=True)

# セレクトボックス
option = st.selectbox(
    'あなたの好きな数字を教えてください。',
    list(range(1, 11))
)
'あなたの好きな数字は', option, 'です。'
# テキスト sidebar付けるとサイドに行く。
text = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味:', text
# スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション:', condition

# カラム
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
# エキスパンダー
expander1 = st.expander('問合せ1')
expander1.write('問合せ１の回答')
expander2 = st.expander('問合せ2')
expander2.write('問合せ2の回答')
