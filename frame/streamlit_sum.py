import streamlit as st
import pandas


def st_sum(obj):
    item = ["total", "avg", "min", "max"]
    options = st.multiselect(
        '请选择你要求和操作的表',
        obj.files)

    for file in options:
        data = obj.sum(file)
        for key, value in data.items():
            st.write(f"{file}: {key}")
            k = [""] + list(value.keys())
            v = [item] + [list(i.values()) for i in value.values()]

            st.write(pandas.DataFrame(dict(zip(k, v))))

    if options:
        st.markdown('<center>求和结束嘞</center>', unsafe_allow_html=True)
