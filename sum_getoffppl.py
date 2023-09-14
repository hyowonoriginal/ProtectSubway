import numpy as np
import pandas as pd
import csv

station = pd.read_csv('지하철_역별OD_20230331.csv', encoding = 'cp949')
line2_df = pd.read_csv('2호선_역위치.csv', encoding = 'cp949')
line5_df = pd.read_csv('5호선_역위치.csv', encoding = 'cp949')
line7_df = pd.read_csv('7호선_역위치.csv', encoding = 'cp949')
line8_df = pd.read_csv('8호선_역위치.csv', encoding = 'cp949')

sort_station = station.sort_values(by='하차인원', ascending=False)

sta_line2 = ['강변(동서울터미널)', '구의(광진구청)', '건대입구']
sta_line5 = ['군자(능동)', '광나루(장신대)', '아차산(어린이대공원후문)']
sta_line7 = ['건대입구', '중곡', '어린이대공원(세종대)', '뚝섬유원지', '군자(능동)']

sta_list = [sta_line2, sta_line5, sta_line7]

line2_list = list(line2_df.iloc[:, 2])
line5_list = list(line5_df.iloc[:, 2])
line7_list = list(line7_df.iloc[:, 2])

print(top_orient_sta('광나루(장신대)', 5))

class Passenger:
    def top_orient_sta(dest, line):
        return list(sort_station.iloc[:10, 2])
    
    def top_orient(dest, line):
        result = []
        sort_station = station.loc[(station['하차_역'] == dest) & (station['하차_호선'] == f'{line}호선')].sort_values(by = '총_승객수', ascending = False)
        top_list = top_orient_sta(dest, line)
        for i in range(10):
            return_list = [top_list[i], sort_station.iloc[i, 1], dest, sort_station.iloc[i, 3], sort_station.iloc[i, 5]]
            result.append(return_list)
        return result
    
    def sum(name, line):
        top_list = top_orient_sta(name, line)
        below_sum = 0
        above_sum = 0
        
        if line == 2:
            for i in range(len(top_list)):    
                if line2_list.index(name) < line2_list.index(top_list[i]):
                    below_sum += sort_station.iloc[i, 5]
                else:
                    above_sum += sort_station.iloc[i, 5]
        elif line == 5:
            for i in range(len(top_list)):
                try:
                    if line5_list.index(name) < line5_list.index(top_list[i]):
                        below_sum += sort_station.iloc[i, 5]
                    else:
                        above_sum += sort_station.iloc[i, 5]
                except ValueError:
                    above_sum += sort_station.iloc[i, 5]
        else:
            try:
                for i in range(len(top_list)):
                    if line7_list.index(name) < line7_list.index(top_list[i]):
                        below_sum += sort_station.iloc[i, 5]
                    else:
                        above_sum += sort_station.iloc[i, 5]
            except ValueError:
                below_sum += sort_station.iloc[i, 5]
        
        result_list = [name, line, above_sum, below_sum]
        return result_list

f = open('상하행_하차인원.csv', 'w', newline = '')       
wr = csv.writer(f)

wr.writerow(['역명', '호선', 'above_sum', 'below_sum'])
for i in range(len(sta_list)):
    if i == 0:
        for j in range(len(sta_list[i])):
            wr.writerow(passenger.sum(sta_line2[j], 2))
    elif i == 1:
        for j in range(len(sta_list[i])):
            wr.writerow(passenger.sum(sta_line5[j], 5))
    else:
        for j in range(len(sta_list[i])):
            wr.writerow(passenger.sum(sta_line7[j], 7))
    
f.close()

f = open('승차역_상위10개_.csv', 'w', newline = '')
wr = csv.writer(f)
wr.writerow(['승차역', '승차_호선', '하차역', '하차_호선', '하차승객_수'])

for i in range(len(sta_list)):
    if i == 0:
        for j in range(len(sta_list[i])):
            passenger.top_orient(sta_line2[j], 2)
    elif i == 1:
        for j in range(len(sta_list[i])):
            passenger.top_orient(sta_line5[j], 5)
    else:
        for j in range(len(sta_list[i])):
            passenger.top_orient(sta_line7[j], 7)
            
f.close()


f = open('승차역_상위10개_.csv', 'w', newline = '')
wr = csv.writer(f)
wr.writerow(['승차역', '승차_호선', '하차역', '하차_호선', '하차승객_수'])


for i in range(len(sta_list)):
    if i == 0:
        for j in range(len(sta_list[i])):
            dest = sta_line2[j]
            line = 2
            with open('승차역_상위10개.csv', 'a', newline='') as f:
                wr = csv.writer(f)
                for data in passenger.top_orient(dest, line):
                    wr.writerow(data)
    elif i == 1:
        for j in range(len(sta_list[i])):
            dest = sta_line5[j]
            line = 5
            with open('승차역_상위10개.csv', 'a', newline='') as f:
                wr = csv.writer(f)
                for data in passenger.top_orient(dest, line):
                    wr.writerow(data)
    else:
        for j in range(len(sta_list[i])):
            dest = sta_line7[j]
            line = 7
            with open('승차역_상위10개.csv', 'a', newline='') as f:
                wr = csv.writer(f)
                for data in passenger.top_orient(dest, line):
                    wr.writerow(data)
f.close()

