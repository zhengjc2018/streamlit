"""
    requirements:  pip install streamlit

"""
import time
import streamlit as st
import pandas
import numpy


def manage():
    # 增加一个滑动条
    x = st.slider('select a value')
    st.write(x, 'squared is', x * x)

    # 添加标题, write支持markdown格式
    st.title('My first app')
    st.write('#### test')
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pandas.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))

    # 绘制地图
    map_data = pandas.DataFrame(
        numpy.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)

    # 复选框
    if st.checkbox('Show dataframe'):
        chart_data = pandas.DataFrame(
            numpy.random.randn(20, 3),
            columns=['a', 'b', 'c'])

        st.line_chart(chart_data)

    # 列表选择
    option = st.selectbox(
        'Which number do you like best?',
        ['first column', "second column"])

    'You selected: ', option

    # 侧边栏
    option1 = st.sidebar.selectbox(
        'Which number do you like best?',
        ['first column1', "second column1"])
    if option1 == "first column1":
        'You selected: ', option1

    # 进度条
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)


if __name__ == "__main__":
    manage()
