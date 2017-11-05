import os

import pandas as pd
import numpy as np


os.mkdir('/Users/BuleSky/Desktop/work') # 结果文件夹路径
os.mkdir('/Users/BuleSky/Desktop/notwork')

file_dir = "/Users/BuleSky/Desktop/csv"    # 数据文件夹路径
for root, dirs, files in os.walk(file_dir):
    for i in range(2):  # 文件夹里几个文件范围就是几
        list1 = []
        name = files[i] # windows应该不需要+1

        rf = pd.read_csv('/Users/BuleSky/Desktop/csv/' + name)
        print(rf.index)
        for i in rf.index:

            start = rf.iat[i, 37]
            end = rf.iat[i, 38]
            print(i)
            if start > end:
                print(i)
                rf.iat[i, 29] = rf.iat[i, 32]
                rf.iat[i, 30] = rf.iat[i, 33]
                rf.iat[i, 31] = rf.iat[i, 34]
            else:
                if start < end:
                    continue

                else:
                     #print(type(rf.iloc[i]))
                    series = rf.iloc[i]
                    new_list = list(series.values)
                    list1.extend([new_list])
                    print(rf.index[i])
                    # rf.drop(i, inplace=True)
        rf2 = rf.drop(['32','33','34','39'], axis = 1)
        rf2.to_csv("/Users/BuleSky/Desktop/work/"+name, index=False)
        rf3 = pd.DataFrame(np.array(list1),columns=['time',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39])
        #rf4 = rf3.drop(['39'],axis = 1)
        rf3.to_csv("/Users/BuleSky/Desktop/notwork/"+name, index=False)





