import os

path = '/Users/liulingling/Documents/Github/docs' #待读取文件的文件夹绝对地址
files = os.listdir(path) #获得文件夹中所有文件的名称列表
skip_dirs = ['template', '.circleci', '.github', 'config-templates', 'etc', 'media', 'scripts', 'templates'
,'.git', '.gitignore']
skip_files = ['LICENSE']
for file in files:
    if not os.path.isdir(file): #判断是否是文件夹
        if file not in skip_files:
            print(file+'\n')
    else:
        if file not in skip_dirs:
            print(file)
            path1 = path+"/"+file
            files1 = os.listdir(path1)
            for file1 in files1:
                print(file1)