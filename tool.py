
import csv
import os
os.mkdir('/Users/BuleSky/Desktop/test')
k=0
file_dir = "/Users/BuleSky/Downloads/110110"
for root, dirs, files in os.walk(file_dir):
    for i in range(2):
        k += 1
        name = files[i+1]
        f = open('/Users/BuleSky/Downloads/110110/'+name, 'rb')
        print(name)
        os.chdir('/Users/BuleSky/Desktop/test')
        num1 = 703+k
        num2 = 710+k
        wf1 = open('data'+str(num1)+'.csv','w')
        wf2 = open('data'+str(num2)+'.csv','w')

        writer1 = csv.writer(wf1)
        writer2 = csv.writer(wf2)

        writer1.writerow(['time',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
        writer2.writerow(['time',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
        line = f.readline()
        line = f.readline()
        line = str(f.readline())
        list1 = []
        p = 2
        q = None
        count1 = 0
        a = 0
        count = 0
        while len(line) > 4:
            for i in line:
                if i != 'r':
                    if i == '\\':
                        q = count1+a
                        list1.append(line[p: q])
                        p = q +2
                        a += 1
                    else:
                        count1 += 1
                else:
                    q = count1 + a -1
                    list1.append(line[p: q])
            count1 = 0
            new_list= list1[0:-2]
               # 调用文件的 readline()方法

            if count <= 800000:
                writer1.writerow(new_list)
                count += 1

            else:
                writer2.writerow(new_list)

            line = str(f.readline())
            list1 = []
            a = 0
            p = 2
            q = None
        print('3')
        f.close()
        wf1.close()
        wf2.close()
