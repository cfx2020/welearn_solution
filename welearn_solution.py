from bs4 import BeautifulSoup
units = [i for i in range(1, 9)]
tasks = [i for i in range(1, 21)]
list = []
print('此脚本完全免费，仅供学习使用，使用前请查看我的readme.md文档')
while True:
    lesson = int(input('请输入你想查询的的课程代码，课程代码在以下目录：Android/data/com.sflep.course/files/data/')
    unit=int(input('请输入你想查询的单元序号(1~8)'))
    task=int(input('请输入你需要查询的任务序号（1~20）'))
    if unit in units:
        if task in tasks:
            break
        else:
            print('你输入了错误的任务序号，请重新输入')
    else:
        print('你输入了错误的单元序号，请重新输入')

with open(f'/storage/emulated/0/Android/data/com.sflep.course/files/data/{lesson}/unit_0{unit}/main{task}.html') as main:
    bs1=BeautifulSoup(main, 'html.parser')
    list=bs1.find_all('input', type="text")
    print(f'第{unit}单元，第{task}个任务的答案是：')
    for i in list:
        i=str(i)
        bs2=BeautifulSoup(i, 'html.parser')
        solution1=bs2.input['data-solution']
        print(solution1)
