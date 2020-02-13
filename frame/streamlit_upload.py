import os
# import streamlit as st


def st_upload(file):

    # ti = st.text_input(
    #     '请输入要解析的excel路径, 当为文件夹时会解析下面的所有xlsx文件', '请输入')

    return get_file(file)


def get_file(file_dir):
    f = []
    if not os.path.isdir(file_dir) and os.path.exists(file_dir):
        return [file_dir]

    for root, dirs, files in os.walk(file_dir):
        for file in files:
            _ = os.path.join(root, file)
            if file.split('.')[-1] not in ["xlsx"] or not os.path.exists(_):
                continue
            f.append(_)
    return f


if __name__ == '__main__':
    print(get_file("D:\\code\\streamlit-test\\test\\ewda"))
