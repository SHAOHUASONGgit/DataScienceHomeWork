'''
@author ShaoHuasong
@desc A reducer for hadoop-streaming
@date 2021/11/28
@pyversion 3
'''
import sys
currentUser1 = None  # 当前主用户
currentUser2 = None  # 当前推荐用户
user1 = None  # 用于读取输入的主用户
user2 = None  # 用于读取输入的推荐用户
mutualCount = []  # 主用户与推荐用户的共同好友列表
outputStream = []  # 输出流表
for line in sys.stdin:
    line = line.strip()
    data = line.split()
    user12 = data[0].split(',')

    user1 = int(user12[0])
    user2 = int(user12[1])
    mutualUser = int(data[1])  # 共同好友
    if(currentUser1 == user1):  # 如果当前主用户与读入的相同
        if(currentUser2 == user2):  # 如果当前推荐用户与读入的相同
            mutualCount.append(mutualUser)  # 向列表中插入共同好友
        elif(-1 in mutualCount):  # 共同好友列表中-1(即当前主用户与当前推荐用户已经是好友)
            mutualCount.clear()  # 清空共同好友列表
            currentUser2 = user2  # 更新当前推荐用户
            mutualCount.append(mutualUser)
        else:
            outputStream.append([currentUser2, mutualCount.copy()])  # 向输出流表中添加当前推荐用户与共同好友(例子:[4,[1,2,3]])
            mutualCount.clear()
            currentUser2 = user2
            mutualCount.append(mutualUser)
    else:  # 如果当前主用户与读入的不相同
        if(currentUser1 == None):  # 如果当前主用户为None(即读取第一行时)
            currentUser1 = user1  # 更新当前主用户
            currentUser2 = user2
            mutualCount.append(mutualUser)
            outputStream.append(currentUser1)  # 向输出流表中插入当前主用户
        else:
            if(-1 in mutualCount):
                if(len(outputStream)==1):  # 如果输出流表长度为1(即表中只有当前主用户)
                    currentUser1 = user1
                    currentUser2 = user2
                    outputStream.clear()  # 清空输出流表
                    mutualCount.clear()
                    mutualCount.append(mutualUser)
                    outputStream.append(currentUser1)
                else:
                    output = "Recommend for user:" + str(outputStream[0]) + "\t"
                    recommendationInOrder = sorted(outputStream[1:], key=lambda mutualNum: len(mutualNum[1]),reverse=True)  # 根据共同好友数量，对输出流表中的推荐用户进行排序
                    for data in recommendationInOrder:
                        output = output + str(data[0]) + "(" + str(len(data[1])) + ":" + str(data[1]) + ") "
                    print(output)
                    currentUser1 = user1
                    currentUser2 = user2
                    outputStream.clear()
                    mutualCount.clear()
                    mutualCount.append(mutualUser)
                    outputStream.append(currentUser1)
            else:
                outputStream.append([currentUser2, mutualCount.copy()])
                output = "Recommend for user:" + str(outputStream[0]) + "\t"
                recommendationInOrder = sorted(outputStream[1:], key=lambda mutualNum: len(mutualNum[1]), reverse=True)
                for data in recommendationInOrder:
                    output = output + str(data[0]) + "(" + str(len(data[1])) + ":" + str(data[1]) + ") "
                print(output)
                currentUser1 = user1
                currentUser2 = user2
                mutualCount.clear()
                outputStream.clear()
                mutualCount.append(mutualUser)
                outputStream.append(currentUser1)
# 读到了最后一行
if(-1 in mutualCount):
    if(len(outputStream)==1):
        pass  # 啥也不干，因为数据已经读完了，不用再更新了
    else:
        output = "Recommend for user:" + str(outputStream[0]) + "\t"
        recommendationInOrder = sorted(outputStream[1:], key=lambda mutualNum: len(mutualNum[1]), reverse=True)
        for data in recommendationInOrder:
            output = output + str(data[0]) + "(" + str(len(data[1])) + ":" + str(data[1]) + ") "
        print(output)
else:
    outputStream.append([currentUser2, mutualCount.copy()])
    output = "Recommend for user:" + str(outputStream[0]) + "\t"
    recommendationInOrder = sorted(outputStream[1:], key=lambda mutualNum:len(mutualNum[1]),reverse=True)
    for data in recommendationInOrder:
        output = output + str(data[0]) + "(" + str(len(data[1])) + ":" + str(data[1]) + ") "
    print(output)