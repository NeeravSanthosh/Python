# word matching
def word_matching(list1):
    count = 0
    new_list = []
    for word in list1:
        if len(word) > 2 and word [0] == word [-1]:
            count+=1
            new_list.append(word)

    print(new_list)
    print("the count of words where first and last character match are",count)
list1 = ['kick','truck','avocado','earphone','studies']
word_matching(list1)