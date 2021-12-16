# !usr/bin/python
# encoding: utf-8
# Author: Tracy Tao(Dasein)
# Date: 2021/11/31

import pandas as pd
import numpy as np
from numpy import *
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

if __name__ == "__main__":
    f1 = open(".//data//features.txt", 'r') # 读取txt文件，获取数据
    str = f1.read()
    f1.close()
    df1 = pd.read_csv(".//data//features.txt", sep='\t') # 创建数据框
    df1 = df1.drop('000', axis=1) # 去除不相关的列
    df1 = df1.rename(columns={'A': 'Restaurant'}) # 重新命名特征名
    df1.to_csv("restauant.csv") # 保存好转换好的数据
    Name = ['id', 'UserName', 'idx'] # 设置列名
    atlanta = pd.read_csv(".//data//atlanta.txt", sep='\t', engine='python')    # 读取Atlanta数据
    atlanta.columns = Name  #重命名
    a = atlanta['idx'].str.split(' ')
    A = pd.DataFrame(a)
    # 同样的处理其他文件数据
    # 后期会改进，用循环的方式直接读取。当时为了查看数据防止报错就一个个coding的。【待更新@Dasein】
    boston = pd.read_csv(".//data//boston.txt", sep='\t', engine='python')
    boston.columns = Name
    b = boston['idx'].str.split(' ')
    B = pd.DataFrame(b)
    # print(B.head())
    chicago = pd.read_csv(".//data//chicago.txt", sep='\t', engine='python')
    chicago.columns = Name
    c = chicago['idx'].str.split(' ')
    C = pd.DataFrame(c)
    # print(C.head())
    la = pd.read_csv(".//data//los_angeles.txt", sep='\t', engine='python')
    la.columns = Name
    d = la['idx'].str.split(' ')
    D = pd.DataFrame(d)
    # print(D.head())
    new_orleans = pd.read_csv(".//data//new_orleans.txt", sep='\t', engine='python')
    new_orleans.columns = Name
    e = new_orleans['idx'].str.split(' ')
    E = pd.DataFrame(e)
    # print(E.head())
    new_york = pd.read_csv(".//data//new_york.txt", sep='\t', engine='python')
    new_york.columns = Name
    f = new_york['idx'].str.split(' ')
    F = pd.DataFrame(f)
    # print(F.head())
    san_francisco = pd.read_csv(".//data//san_francisco.txt", sep='\t', engine='python')
    san_francisco.columns = Name
    g = san_francisco['idx'].str.split(' ')
    G = pd.DataFrame(g)
    # print(G.head())
    washington_dc = pd.read_csv(".//data//washington_dc.txt", sep='\t', engine='python')
    washington_dc.columns = Name
    h = washington_dc['idx'].str.split(' ')
    H = pd.DataFrame(h)
    # print(H.head())
    All = pd.concat([A, B, C, D, E, F, G, H], ignore_index=True)
    print(All.shape) # 合并所有数据集，明查看数据量（4152rows）
    data = All['idx'].to_list()
    te = TransactionEncoder()
    X = te.fit_transform(data)
    # print(X)
    df_all = pd.DataFrame(X)
    # print(df_all.head())
    result = apriori(df_all, min_support=0.2, use_colnames=True) # 因为支持度实在太小了，所以只设置了0.2
    result.to_csv('all_apriori.csv')
    assc = association_rules(result, min_threshold=0.2)
    assc.to_csv('all_assc.csv')
    dataA = A['idx'].to_list()
    teA = TransactionEncoder()
    aa = teA.fit_transform(dataA)
    df_a = pd.DataFrame(aa)
    resultA1 = apriori(df_a, min_support=0.5, use_colnames=True)
    asscA = association_rules(resultA1, min_threshold=0.5)
    resultA1.to_csv('boston_res.csv')
    print(asscA)
    