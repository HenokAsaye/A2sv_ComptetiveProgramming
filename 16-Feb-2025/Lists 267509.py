# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input().strip())  
    l = []  
    for _ in range(N):
        command = input().split()  
        operation = command[0].lower()  
        if operation == "insert":
            l.insert(int(command[1]), int(command[2]))  
        elif operation == "append":
            l.append(int(command[1]))  
        elif operation == "pop":
            if l:  
                l.pop()
        elif operation == "print":
            print(l)
        elif operation == "remove":
            if int(command[1]) in l:  
                l.remove(int(command[1]))
        elif operation == "sort":
            l.sort()
        elif operation == "reverse":
            l.reverse() 