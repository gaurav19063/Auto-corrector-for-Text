from nltk.tokenize import word_tokenize




def load_data():
    path="/home/gaurav/Desktop/IIITD/IR/Assignments/assignment2/english2.txt"
    f = open(path,encoding='windows-1252')
    words = word_tokenize(f.read())
    return words



def Qwords():
    q=input().lower()
    return set(word_tokenize(q))


def find_editDistance(y, x):  # i->x,j->y

    arr = [[-1 for i in range(len(y) + 1)] for j in range(len(x) + 1)]
    # print(len(arr))
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            if i == 0:
                arr[i][j] = j
            elif j == 0:
                arr[i][j] = i
            elif x[i - 1] == y[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                if arr[i][j - 1] <= arr[i - 1][j] and arr[i][j - 1] <= arr[i - 1][j - 1]:
                    arr[i][j] = 1 + arr[i][j - 1]
                if arr[i - 1][j - 1] <= arr[i - 1][j] and arr[i - 1][j - 1] <= arr[i][j - 1]:
                    arr[i][j] = 3 + arr[i - 1][j - 1]
                if arr[i - 1][j] <= arr[i - 1][j - 1] and arr[i - 1][j] <= arr[i][j - 1]:
                    arr[i][j] = 2 + arr[i - 1][j]

    return arr[len(x)][len(y)]



def find_k_wordsfor_x(vocab,x,k):
    dict1={}
    for y in vocab:
        d=find_editDistance(x,y)
        dict1[y]=d
    # print(dict1)
    # dict1=sorted(dict1.items(), key=lambda kv: (kv[1], kv[0]))
    dict1 = sorted(dict1, key=dict1.get, reverse=False)
    if len(dict1)<=k:
        return dict1
    else:
        return dict1[0:k]
        # return  dict([itertools.islice(dict1.items(), k)])




def findWords(vocab,query_words,k):
    # print(k)
    dict2={}
    for x in query_words:
        if x not in vocab:
            # print (x)
            dict2[x]=find_k_wordsfor_x(vocab,x,k)
    # print(dict2)
    return dict2










# --------------------------------------
vocab=load_data()
print("---vocab loaded----Enter a query------Enter k value---------")
query_words=Qwords()
# print( query_words)
# print ()
k=int(input())
# print (k)
ranked_words=findWords(vocab,query_words,k)
for x in ranked_words:
    print("Simmilar words for word " +x +" Are: " ,end=" ")

    for  v in ranked_words[x]:
        # print(v)
        print(v+",", end=" ")
    print()        # for a,b in v:
        #     print(a)