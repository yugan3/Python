#1. 无空隙回声输出
a = input("")
a = a.replace(" ","")
print(a)

#2. 文件关键行数
f = open(‘latex.log’, 'r', encoding='utf-8')
s = 0
f = set(f.readlines())
f = list(f)
for i in f:
    s = s + 1
print(s)

#3. 字典翻转输出
s = input()
try:
    dict_1 = eval(s)
    if isinstance(dict_1, dict):
        dict_2 = dict(zip(dict_1.values(), dict_1.keys()))
        print(dict_2)
    else:
        print('输入错误')
except:
    print('输入错误')

#4. 《沉默的羔羊》之最多单词
import jieba
f = open('沉默的羔羊.txt', 'r', encoding='utf-8').read()
words  = jieba.lcut(f)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
print(items[0][0]) #这里是list，然后每个元素又是list，所以是list的list