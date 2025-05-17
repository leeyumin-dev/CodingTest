'''
그룹단어 = 각 문자가 연속해서 나타는 경우
ccazzzzbb, kin => 그룹 단어임
aabbbccb => 그룹 단어 아님
현재 문자열이 다음에도 오는지 확인

'''
N = int(input())
result = 0
isgroup = []
for i in range(N):
    isgroup = []
    word = input()
    if len(word) == 1:
        isgroup.append(True)
    else:
        for cur_w in word:
            indexs = [idx for idx, w in enumerate(word) if w == cur_w]
            if all(indexs[idx + 1] - indexs[idx] == 1 for idx in range(len(indexs)-1)):
                isgroup.append(True)
            else:
                isgroup.append(False)

    if all(isgroup):
        result += 1

print(result)    

################# 다른 풀이
result = N
for i in range(N):
    word = input()
    for w_idx in range(len(word) - 1):
        if word[w_idx] == word[w_idx + 1]:
            continue
        elif word[w_idx] in word[w_idx+1:]: # 바로 옆글자에 없는데 뒤에 문자열에는 있음 -> 연속된거 아님
            result -= 1
            break

print(result)
