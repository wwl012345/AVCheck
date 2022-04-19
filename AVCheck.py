#!/usr/bin/env python3

banner = '''

     ___   ____    ____  ______  __    __   _______   ______  __  ___ 
    /   \  \   \  /   / /      ||  |  |  | |   ____| /      ||  |/  / 
   /  ^  \  \   \/   / |  ,----'|  |__|  | |  |__   |  ,----'|  '  /  
  /  /_\  \  \      /  |  |     |   __   | |   __|  |  |     |    <   
 /  _____  \  \    /   |  `----.|  |  |  | |  |____ |  `----.|  .  \  
/__/     \__\  \__/     \______||__|  |__| |_______| \______||__|\__\ 

                                                       --by 想走安全的小白
                                                                      
'''

print(banner)

with open('tasklist.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip('\n')
        #取出tasklist中的进程名称
        target = line.split(' ')[0]
        with open('杀软识别.txt', 'r') as f:
            for i in f.readlines():
                #将取出的进程名与杀软识别列表中的名称进行对比
                if target == i.strip('\n').split('\"')[1]:
                    result = i.strip('\n').split('\"')[3]
                    if result is None:
                        print("没有识别到杀软或者不存在杀软")
                    else:
                        print("服务器上存在的杀毒软件有:" + result)
                else:
                    pass
