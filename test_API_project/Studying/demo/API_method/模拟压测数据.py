import csv

def generate_usernames(num_users):      # 这是一个函数定义，名为generate_usernames。函数有一个参数num_users，表示要生成的用户名的数量。
    usernames = []
    for i in range(1, num_users + 1):   # 在函数内部，使用for循环从1到num_users（包括1和num_users）生成一个计数器i。
        username = f"张三{i}"            # 然后，通过字符串格式化（f"user_{i}"），创建一个以"user_"为前缀，后接递增计数器的用户名。
        usernames.append(username)      # usernames 是一个变量名，而 [] 表示一个空的列表
    return usernames                    # 这些用户名被添加到名为usernames的列表中，最后，该列表被作为函数的返回值。
def save_to_csv(data, filename):        # 这是另一个函数定义，名为save_to_csv。# 它接受两个参数：data是包含用户名的列表，filename是要保存的CSV文件名。
    with open(filename, 'w', newline='') as csvfile:# 函数使用with语句打开名为filename的文件，使用写入模式（'w'），并且newline=''参数确保在写入CSV时不插入额外的空行。
        writer = csv.writer(csvfile)                # 然后，创建一个CSV写入器（csv.writer(csvfile)）。
        writer.writerow(['Username'])               # 接下来，通过writer.writerow(['Username'])写入CSV文件的标题行，标题为"Username"。
        for username in data:                       # 最后，使用for循环遍历data中的每个用户名，逐行将其写入CSV文件。
            writer.writerow([username])
if __name__ == "__main__":                      # 这是一个条件语句，检查脚本是否作为主程序运行。
    num_users = 1000                            # 设置num_users变量为1000，表示要生成的用户名数量
    usernames = generate_usernames(num_users)   # 调用generate_usernames函数，将生成的用户名列表保存到名为usernames
    save_to_csv(usernames, '../创建csv文件数据/usernames1.csv')    # 用save_to_csv函数实现。
