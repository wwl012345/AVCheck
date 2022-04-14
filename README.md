# AVCheck
对windows系统进程中的杀软进行识别，快速发现杀软，为后续绕过进行准备。

### 工具简介:
首先使用tasklist查看windows服务器上运行的进程，然后将结果复制到“tasklist.txt”，然后遍历tasklist文件并将进程名获取到，然后将进程名与“杀软识别.txt”中的进程名进行对比，如果存在即证明服务器上存在该杀软。

### 使用方法
1.在服务器上执行tasklist命令查看运行的进程
2.将结果复制到tasklit.txt文件中
3.执行命令`python3 AVCheck.py`运行程序
