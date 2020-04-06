import pandas as pd
import time

df = pd.read_csv("data.csv", names=['Timestamp', 'Flextion', 'Rotation',
                                    'Abduction', 'CalAcc', 'CalGyro', 'LoadCell'], header=None)

# xList = []
# yList = []
#
# for i in range(len(df.index)):
#     xList.append(df['Timestamp'])
#     yList.append(df['Abduction'])

f = open("data_new.csv", "w")
f.write('')
f.close()

for i in range(len(df.index)):
    f = open("data_new.csv", "a")
    f.write(str(round((df['Timestamp'][i]-df['Timestamp'][0])/1000, 1)) + "," + str(df['Abduction'][i]) + '\n')
    time.sleep(0.04)
    f.close()

# f = open("data.txt", "r")
# data = f.readlines()
# f.close()
#
#     l = []
#     for i in range(len(data)):
#         l.append(int(data[i].rstrip("\n")))
#     return l
#
# time.sleep(1)

# print(xList)
#
#
