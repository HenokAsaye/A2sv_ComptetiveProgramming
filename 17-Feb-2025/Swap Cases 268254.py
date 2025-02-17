# Problem: Swap Cases - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    new = []
    for i in s:
        if(i.lower()==i):
            new.append(i.upper())
        else:
            new.append(i.lower())
    return "".join(new)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)