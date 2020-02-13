import time
import streamlit as st
import pandas
import numpy
from excel_factory import ExcelFactory
from logger import log
from frame.streamlit_sum import st_sum
from frame.streamlit_upload import st_upload


# def st_upload():
#         # 绘制地图
#     map_data = pandas.DataFrame(
#         numpy.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#         columns=['lat', 'lon'])

#     st.map(map_data)

#     # 复选框
#     if st.checkbox('Show dataframe'):
#         chart_data = pandas.DataFrame(
#             numpy.random.randn(20, 3),
#             columns=['a', 'b', 'c'])

#         st.line_chart(chart_data)

#     # 列表选择
#     option = st.selectbox(
#         'Which number do you like best?',
#         ['first column', "second column"])

#     'You selected: ', option


def manage():

    f = st.sidebar.text_input("解析的excel文件名或路径", "")
    opt = st.sidebar.selectbox('调用函数', ["求和", "查询"])
    files = st_upload(f)
    if f and not files:
        "文件不存在，请重新输入"

    elif f and files:
        st.markdown('<center>开始干活嘞</center>', unsafe_allow_html=True)
        obj = ExcelFactory(files)

        if opt == "求和":
            st_sum(obj)

        elif opt == "查询":
            pass


if __name__ == '__main__':
    manage()
