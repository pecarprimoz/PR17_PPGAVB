with open("clusters.txt", encoding="utf-8") as f:
    clusters = f.readlines()

clusters = list(map(lambda x: x.strip(), clusters[1:]))
# print(clusters)
clusters_list = list(map(lambda x: x[2:-2].split("', '"),clusters))
print(clusters_list)
print(list(map(len,clusters_list)))