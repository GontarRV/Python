from typing import List

def ShopOLAP(N: int, items: List[str]) -> List[str]:

    List_of_products = []
    for i in range(N):
        List_of_products.extend([items[i].split()])
    
    dic = {}    
    for i in range(N):
        if List_of_products[i][0] not in dic.keys():
            dic[List_of_products[i][0]] = int(List_of_products[i][1])
            continue
        dic[List_of_products[i][0]] += int(List_of_products[i][1])
     
    grouped_summary = []
    for k, v in dic.items():
        grouped_summary.append(str(v) + ' ' + k)
        
    grouped_summary = sorted(grouped_summary, reverse = True)
    
    for i in range(len(grouped_summary)):
        grouped_summary[i] = grouped_summary[i].split()
        grouped_summary[i][0], grouped_summary[i][1] = grouped_summary[i][1], grouped_summary[i][0]
        grouped_summary[i] = ' '.join(grouped_summary[i])
        
    return grouped_summary