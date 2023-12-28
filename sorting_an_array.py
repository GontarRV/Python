def sorting(l):
    xchange = True 

    while(xchange):
        xchange = False
    
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
            
                xchange = True