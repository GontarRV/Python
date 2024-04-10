def Keymaker(k: int) -> str:
    
    l = []
    for i in range(k):
        l.append('0')
        
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            if j % i == 0:
                l[j - 1] = open_close(l[j - 1])
    
    s = ''.join(l)
    
    return s 
        
def open_close(n: str) -> str:
    
    if n == '0':
        return '1'
    return '0'