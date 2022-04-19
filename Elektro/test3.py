a = '''
 ┏━━━━┳━━━━┓
 ┃    ┃   ┏┻┓
 ┃    ┃   ┃R┃ 
 ┃   ┏┻┓  ┃2┃
╭┻╮  ┃R┃  ┗┳┛
┃↑┃I ┃1┃  ┏┻┓
╰┳╯  ┗┳┛  ┃R┃  
 ┃    ┃   ┃3┃
 ┃    ┃   ┗┳┛
 ┗━━━━┻━━━━┛
'''
def toString(n):
    ret = str(n)
    if n < 1:
        i = -1
        mult = ["m", "μ", "n", "p", "f"]
        while n<1:
            n*=1000
            i+=1
        ret = str(round(n))+mult[i]
    elif n > 999:
        i = -1
        mult = ["k", "M", "G", "T", "P"]
        while n>999:
            n/=1000
            i+=1
        ret = str(n)+mult[i]
    return ret
def main():
    print(a)
    print(toString(123))
main()