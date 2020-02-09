
text = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."
text = text.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphalist = [*alphabet]
occurences = [0]*len(alphabet)

samletdic = dict(zip(alphabet, occurences))

for key, value in samletdic.items():
    samletdic[key] = text.count(key)

max_key = max(samletdic, key=lambda k: samletdic[k])
max_occ = samletdic.get(max_key)

# Sorter nu pr størelse
sorted_list = sorted(samletdic.items(), key=lambda x: x[1], reverse=True)
updatedDic = dict(sorted_list)

for key, value in updatedDic.items():
    print(key, " : ",  value)


print("Største brug af ", max_key, "på ", max_occ)
