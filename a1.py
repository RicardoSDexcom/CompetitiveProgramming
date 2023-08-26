l=int(input())
input_lists = [
    [1, 3, 4],
    [-1],
    [100, 150, 180, 200]
]
for i in range(3):
    list(map(int,input().split()))
    
for sublist in input_lists:
    print(*sublist)
    
l=int(input())
total=[]
for i in range(l):
    modified = True
    lst=list(map(int,input().split()))
    lst1=lst
    n = lst[len(lst)-1]
    default_value = 0  
    my_list = [default_value] * n
    my_list[0]=lst[0]
    my_list[len(my_list)-1]=lst[len(lst)-2]
    for i in range(1, len(my_list)):
        if my_list[i] == 0:
            my_list[i] = my_list[i-1] + 1
        elif my_list[i] <= my_list[i-1]:
            modified = False
            break
        
 
    if modified:
        total.append(my_list)
    else:
        total.append([-1])
  
 if  total == input_lists:
     
for sublist in total:
    print(*sublist)
