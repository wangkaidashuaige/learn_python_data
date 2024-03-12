import csv
#   通过csv对文件进行读操作
# file = "test.csv"
# csfile = csv.reader(open(file,"r"))
# for cs in csfile:
#     print(cs)

#  对CSV文件进行写操作
fw = open ("../data/111.csv", "w", newline='') # 消除空行
c = csv. writer (fw)
dic = {"selenium":"web","appium":"mobile","interface" :"all"}
for key in dic:
    c. writerow ((key, dic [key]))