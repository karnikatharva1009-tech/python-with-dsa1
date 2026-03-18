def securitykey(number):
    s=str(number)
    frequency={}
    for ch in s:
        frequency[ch]=frequency.get(ch,0)+1
    repeatednumber=0
    for i in frequency.values():
        if i>1:
            repeatednumber+=(i-1)
    return repeatednumber if repeatednumber>0 else -1           