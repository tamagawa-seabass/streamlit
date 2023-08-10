import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('interactive widgets')

"Start!!"

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
"Done"
#expander=st.beta_expander("inqury")
#expander.wite("typing")

#left_column,right_column=st.beta_columns(2)
#left_column.button("display word on right")


#text = st.text_input("あなたの趣味をおしえて")
#'あなたの趣味は',text,"です"
#
#
#condition=st.slider("how are you?",0,100,50)
#"condition:",condition


#option=st.selectbox(
#    "あなたの好きな数字を教えてください",
#    list(range(1,11))
#)

#"あなたの好きな数字は",option

#if st.checkbox("Show Image"):
#    img=Image.open("sample.jpg")
#
#    st.image(img,caption="test",use_column_width=True)









"""
# TAMAGAWA SEABASS SECRET BASE
## 節
### 項

```python


a=()
for i in range(30):
    a+=i
print(a)
```

"""