# ==================================================================#
# 知识图谱webapp：                                                  #
# ==================================================================#
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd  


# ------- 函数01：定义三元组 ------------------------------------#
def Setup_Knowledge_Triples(triples):
# 读取Excel文件  
# 假设Excel文件名为'data_source.xlsx'，并且三元组元素分别位于'A', 'B', 'C'列  
  df = pd.read_excel('data_source.xlsx', usecols=['A', 'B', 'C'])  
  
# 提取三元组  
# 假设我们想要将每行的值作为一个三元组提取出来  
  triples = [[row['A'], row['B'], row['C']] for index, row in df.iterrows()]
  return triples

# --- 函数02：把不重复的三元组节点设置到nodes对象中 ----------------#
def Setup_Triple_Nodes_to_Object_Nodes(triples_n, triple_nodes, nodes):
    for i in range(triples_n):
        m = 0
        # print('nodes对象数目====', len(nodes))
        for j in range(len(nodes)):
            if triple_nodes[i] == nodes[j].id:
                m = 1
                break
        if m == 1:
            continue
        else:
            nodes.append(Node(id=triple_nodes[i],
                              label=triple_nodes[i],  # source_nodes[i],
                              size=15,
                              shape="circularImage",
                              image="craw.jpg"))  # includes **kwargs  //报错找不到文件
            # print("nodes=object", nodes[-1].id)
    return nodes


# ----- 函数03：把源节点和目标节点间的关系设置到edges对象中！---------
def Setup_Triple_Relations_to_Object_Edges(triples_n, source_nodes, current_edges, target_nodes, edges):
    for i in range(triples_n):
        edges.append(Edge(source=source_nodes[i],
                          label=current_edges[i],
                          target=target_nodes[i],  # **kwargs
                          ))
    return edges

# ----- 函数04：展示源代码---------
def Show_Source_Codes():
    my_code = '''
# ==================================================================#
# 知识图谱webapp：                                                  #
# ==================================================================#
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd  


# ------- 函数01：定义三元组 ------------------------------------#
def Setup_Knowledge_Triples(triples):
# 读取Excel文件  
# 假设Excel文件名为'data.xlsx'，并且三元组元素分别位于'A', 'B', 'C'列  
  df = pd.read_excel('data.xlsx', usecols=['A', 'B', 'C'])  
  
# 提取三元组  
# 假设我们想要将每行的值作为一个三元组提取出来  
  triples = [[row['A'], row['B'], row['C']] for index, row in df.iterrows()]
  return triples

# --- 函数02：把不重复的三元组节点设置到nodes对象中 ----------------#
def Setup_Triple_Nodes_to_Object_Nodes(triples_n, triple_nodes, nodes):
    for i in range(triples_n):
        m = 0
        # print('nodes对象数目====', len(nodes))
        for j in range(len(nodes)):
            if triple_nodes[i] == nodes[j].id:
                m = 1
                break
        if m == 1:
            continue
        else:
            nodes.append(Node(id=triple_nodes[i],
                              label=triple_nodes[i],  # source_nodes[i],
                              size=15,
                              shape="circularImage",
                              image="craw.jpg"))  # includes **kwargs  //报错找不到文件
            # print("nodes=object", nodes[-1].id)
    return nodes


# ----- 函数03：把源节点和目标节点间的关系设置到edges对象中！---------
def Setup_Triple_Relations_to_Object_Edges(triples_n, source_nodes, current_edges, target_nodes, edges):
    for i in range(triples_n):
        edges.append(Edge(source=source_nodes[i],
                          label=current_edges[i],
                          target=target_nodes[i],  # **kwargs
                          ))
    return edges
# 主程序：
# ==============================================================#
# 定义浏览器页面作为：运行控制区域、信息可视化展示区
#st.set_page_config(layout="wide")   #将页面显示为整个屏幕
st.sidebar.title('知识图谱生成系统')
st.sidebar.header('菜单与运行控制区域：', divider='rainbow')
st.subheader('运行及其信息显示区域', divider='rainbow')
my_choice = str()
my_choice = st.sidebar.radio('点击按钮，选择一个运行项：',
                             [ '知识图谱构造','知识图谱检索','源代码', '退出系统'])
#
# 第1步：在菜单项外加载三元组集合，避免重复加载
triples_n = 380
triples = [[] for i in range(triples_n)]
triples = Setup_Knowledge_Triples(triples)
# 菜单项：知识图谱构造
if my_choice == '知识图谱构造':
    #
    # 第1步：加载三元组，在上面的程序中已完成
    # print('triples=', triples)
    #
    # 第2步：分解成源节点source_nodes、目标节点target_nodes和边edges
    source_nodes = []
    current_edges = []
    target_nodes = []
    for i in range(triples_n):
        source_nodes.append(str(triples[i][0]))
        current_edges.append(str(triples[i][1]))
        target_nodes.append(str(triples[i][2]))
    # print('源=', source_nodes)
    # print('关系=', current_edges)
    # print('目标=', target_nodes)
    #
    # 第3步：定义KG的Nodes和edges
    nodes = []
    edges = []
    # 把不重复的源节点设置到nodes对象中:
    nodes = Setup_Triple_Nodes_to_Object_Nodes(triples_n, source_nodes, nodes)
    # 把不重复的目标节点设置到nodes对象中:
    nodes = Setup_Triple_Nodes_to_Object_Nodes(triples_n, target_nodes, nodes)
    # 把节点间关系设置到edges对象中:
    edges = Setup_Triple_Relations_to_Object_Edges(triples_n, source_nodes, current_edges, target_nodes, edges)
    #
    # 第4步：设置KG显示区域
    config = Config(width=2000,
                    height=2000,
                    directed=True,
                    physics=True,
                    hierarchical=False,
                    # **kwargs
                    )
    #
    # 第5步：显示KG
    return_value = agraph(nodes=nodes,
                          edges=edges,
                          config=config)

#知识图谱检索
if my_choice=='知识图谱检索':
    pass
# 菜单项：源代码
if my_choice == '源代码':
    Show_Source_Codes()
# 菜单项：退出系统
if my_choice == '退出系统':
    st.write('先休息一下，再运行本系统！')
    st.stop()

# =========================================== 程序结束！=========================#
'''
    # 显示源代码
    st.code(my_code, language='python', line_numbers=True)
    return

# ----- 函数05：知识图谱检索---------


# 主程序：
# ==============================================================#
# 定义浏览器页面作为：运行控制区域、信息可视化展示区
#st.set_page_config(layout="wide")   #将页面显示为整个屏幕
st.sidebar.title('知识图谱生成系统')
st.sidebar.header('菜单与运行控制区域：', divider='rainbow')
st.subheader('运行及其信息显示区域', divider='rainbow')
my_choice = str()
my_choice = st.sidebar.radio('点击按钮，选择一个运行项：',
                             [ '知识图谱构造','知识图谱检索','源代码', '退出系统'])
#
# 第1步：在菜单项外加载三元组集合，避免重复加载
triples_n = 3500
triples = [[] for i in range(triples_n)]
triples = Setup_Knowledge_Triples(triples)
# 菜单项：知识图谱构造
if my_choice == '知识图谱构造':
    #
    # 第1步：加载三元组，在上面的程序中已完成
    # print('triples=', triples)
    #
    # 第2步：分解成源节点source_nodes、目标节点target_nodes和边edges
    source_nodes = []
    current_edges = []
    target_nodes = []
    for i in range(triples_n):
        source_nodes.append(str(triples[i][0]))
        current_edges.append(str(triples[i][1]))
        target_nodes.append(str(triples[i][2]))
    # print('源=', source_nodes)
    # print('关系=', current_edges)
    # print('目标=', target_nodes)
    #
    # 第3步：定义KG的Nodes和edges
    nodes = []
    edges = []
    # 把不重复的源节点设置到nodes对象中:
    nodes = Setup_Triple_Nodes_to_Object_Nodes(triples_n, source_nodes, nodes)
    # 把不重复的目标节点设置到nodes对象中:
    nodes = Setup_Triple_Nodes_to_Object_Nodes(triples_n, target_nodes, nodes)
    # 把节点间关系设置到edges对象中:
    edges = Setup_Triple_Relations_to_Object_Edges(triples_n, source_nodes, current_edges, target_nodes, edges)
    #
    # 第4步：设置KG显示区域
    config = Config(width=700,
                    height=1050,
                    directed=True,
                    physics=True,
                    hierarchical=False,
                    # **kwargs
                    )
    #
    # 第5步：显示KG
    return_value = agraph(nodes=nodes,
                          edges=edges,
                          config=config)

#知识图谱检索
if my_choice=='知识图谱检索':
    pass
# 菜单项：源代码
if my_choice == '源代码':
    Show_Source_Codes()
# 菜单项：退出系统
if my_choice == '退出系统':
    st.write('先休息一下，再运行本系统！')
    st.stop()

# =========================================== 程序结束！=========================#
