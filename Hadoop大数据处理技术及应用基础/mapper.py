'''
@author ShaoHuasong
@desc A mapper for hadoop-streaming
@date 2021/11/28
@pyversion 3
'''
import sys
for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')
    if len(data)==2:  # 如果用户有好友
        user = data[0]  # 主用户
        friends = data[1].split(',')  # 主用户的所有好友
        for firstPointer in range(len(friends)):
            print(user + "," + friends[firstPointer] + "\t" + "-1")  # 输出已经是好友的用户组合，并设置共同好友为-1
            for secondpointer in range(len(friends)):  # 输出所有可能的好友组合，共同好友为主用户
                if firstPointer!=secondpointer:  # 用户不可能和自己交朋友
                    print(friends[firstPointer] + "," + friends[secondpointer] + "\t" + user)