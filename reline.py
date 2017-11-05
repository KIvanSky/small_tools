
import pandas as pd
import numpy as np
import os
os.mkdir('/Users/BuleSky/Desktop/csv')

file_dir = "/Users/BuleSky/Desktop/txt"    # 数据文件夹路径
for root, dirs, files in os.walk(file_dir):
    for i in range(2):  # 文件夹里几个文件范围就是几

        name = files[i] # windows应该不需要+1


        rf = pd.read_table('/Users/BuleSky/Desktop/txt/'+name,header=2)
# 每列数据的数据类型。例如 {‘a’: np.float64, ‘b’: np.int32})
        print(rf.columns)
        print(rf.values)
        df = pd.DataFrame(rf.values,columns=['time',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39])
#print(df)
        df.to_csv('/Users/BuleSky/Desktop/csv/'+ name[0:-4]+'.csv', index=False)






