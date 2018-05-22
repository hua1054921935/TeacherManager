import os


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

#
# list1 = scan_files('data')
# list1.sort()
#
# for data in list1:
#
#     name = data.split('/')[2]
#
#     if name == 'email.csv':
#         print(name)
#
#         df = pandas.read_csv(data,encoding = 'ISO-8859-1')
#         df.drop([0], inplace=True)
#         df.columns =['time','proto','sip','sport','dip','dport','from','to','subject']
#         counts=df['sip'].value_counts()
#         # print(len(counts))
#
# list3 = ["2017-11-%s" % i for i in range(1, 31)]
# print(list3)
