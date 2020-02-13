[TOC]

# Excel补充计划
---------------------
目标：将excel的函数集成进来，做第一的excel套壳软件
目标人群：经常使用excel，做重复有逻辑操作，并且**粗心**的人
示例:

![示例](.\template_20200216192338.png)

#### 1. Requirements
- python3.x
- streamlit

#### 2. 安装及使用
##### 2.1. 安装streamlit
```
pip install streamlit
```

##### 2.2. 运行以下命令，在浏览器上打开地址:  `http:localhost:8080`
```
streamlit run run.py --server.port 8080
```

#### 3. 更新
- 20190216 - 增加求和函数

#### 4. 吐槽点
- pyinstaller 无法将streamlit打进exe中
- streamlit 运行即加载，设置类变量等用来判断组件是否执行无意义，只能通过组建的返回值来判断
