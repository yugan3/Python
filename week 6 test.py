# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:18:10 2019

@author: Gan
"""

N = input("")
a = (" ".join(N))
a = set(a)
a.discard(' ')
a = list(a)
b = []
for i in a:
    b.append(int(i))
a=b
sum = 0
for i in a:
    sum = sum+i
print(sum)




s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖 
       杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙 
       金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍 
       鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰 
       阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰 
       乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王 
       忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正 
       李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复 
       逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣 
       洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复 
       黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄 
       张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫 
       洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈 
       完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱 
       郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲 
       谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉 
       双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏 
       逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''
s = s.split()
counts = {}
for aa in s:
        counts[a]=counts.get(a,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(1):
    a,count = items[i]
print(a,count)


#{'双儿': 9,
# '洪七公': 6,
# '赵敏': 11,
# '逍遥子': 7,
# '鳌拜': 9,
# '殷天正': 5,
# '金轮法王': 10,
# '乔峰': 9,
# '杨过': 8,
# '郭靖': 3,
# '杨逍': 10,
# '段誉': 7,
# '慕容复': 6,
# '阿紫': 8,
# '郭芙': 9,
# '令狐冲': 5,
# '小龙女': 1,
# '梅超风': 6,
# '李莫愁': 5,
# '张无忌': 6,
# '岳不群': 1,
#'黄药师': 4,
# '黄蓉': 7,
# '忽必烈': 8,
# '张三丰': 9,
# '袁冠南': 5,
# '郭襄': 8,
# '陈家洛': 3,
# '完颜洪烈': 6,
# '虚竹': 1,
# '王语嫣': 2,
# '韦小宝': 3,
# '阿朱': 2,
# '岳灵珊': 1,
# '谢逊': 4,
# '灭绝师太': 1}