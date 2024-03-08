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
    
    grouped_summary = list(dic.items())
  
    sorted_items = sorted(grouped_summary, key=lambda item: [-item[1], item[0]])
    
    the_final_result = []
    for i in range(len(sorted_items)):
        the_final_result.append(sorted_items[i][0] + ' ' + str(sorted_items[i][1])) 
        
    return the_final_result