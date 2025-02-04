# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    res=[]
    cmds=[]
    for i in range(N):
        cmds.append(input())
    
    for cmd in cmds:
        
        if (cmd.split()[0])=="insert":
            
            res.insert(int(cmd.split()[1]),int(cmd.split()[2]))
        elif (cmd.split()[0])=="print":
            print(res)
        elif (cmd.split()[0])=="remove":
            res.remove(int(cmd.split()[1]))
        elif (cmd.split()[0])=="append":
            res.append(int(cmd.split()[1]))
        elif (cmd.split()[0])=="sort":
            res.sort()
        elif (cmd.split()[0])=="pop":
            res.pop()
        elif cmd.split()[0]=="reverse":
            res.reverse()
            
        
        
        