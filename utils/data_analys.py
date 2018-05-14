import os
import pandas
import glob
# os.chdir('data/2017-11-01')
# # print(os.getcwd())
#
# list1=glob.glob('*.csv')
# # 读取文件中的内容
# for data in list1:
#
#     df=pandas.read_csv(data)
#     print(df)
def scan_files(directory, prefix=None, postfix=None):
    files_list = []

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list
# list1=scan_files('data')
# for data in list1:
#     print(data)
#     df=pandas.read_csv(data)
#
#     print(df.head(5))
#     print(df.tail(5))
#     pandas.DataFrame()

# a='utils/data/2017-11-25/checking.csv'
# print(a.split('/'))