matn = "python is easy and python is fun"

new_dic = {}

for i in matn.split(" "):
    if not new_dic.get(i):
      new_dic[i] = 1
    else:
       new_dic[i] +=1

print(new_dic)