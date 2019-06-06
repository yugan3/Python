f = open("latex.log")
s = 0
c = 0
for line in f.readlines():
    line = line.strip("\n") 
    #readliney有一个空格操作\n,所以要把这个换行带来的字符消除掉
    #类似于c语言中的\0座位字符串的标记
    if line == "":
        continue
    s += len(line)
    c += 1
print(round(s / c))

f = open(data.csv)
ls = f.readlines()
for row in ls:
    ls1 = ls[::-1]
lt=[]
for a in ls1:
    a = a.strip("\n") #去掉\n这个空格部分
    a = a.replace(" ", "")#将old（前面）替换为new（后面）
    lt = a.split(",")#分割成字符串的形式储存到一个列表中
    lt = lt[::-1]#倒序
    print(";".join(lt))#依次读取且添加；，最后保存到另一个文件中，解决了字符串的问题
f.close()

