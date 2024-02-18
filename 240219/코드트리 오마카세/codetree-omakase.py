from copy import deepcopy

l, q = map(int, input().split())
table = [[]for i in range(l)]
people = 0
sushi = 0
eaten = {}
people_location = {}
curr_time = 1

def rotate(table):
    dummy = deepcopy(table)
    for i in range(len(table)-1):
        table[i + 1] = dummy[i]
    
    table[0] = dummy[-1]


def eat(table, method, people_location, eaten):
        global people
        global sushi

        for name in eaten.keys():
            for i in range(eaten[name]):
                if(name in table[people_location[name]] and eaten[name] > 0):
                    table[people_location[name]].remove(name)
                    sushi -= 1
                    eaten[name] -= 1

                if (eaten[name] == 0):
                    people -= 1
                    eaten[name] = -1

        

for i in range(q):

    a = list(input().split())

    if(a[0] == '100'): # 초밥만들기
        if(people > 0):
            rotate(table)
            eat(table, method, people_location, eaten)
        else:
            rotate(table)
        method, t, x, name = a
        t = int(t)
        x = int(x)
        curr_time = t
        sushi += 1
        table[x].append(name)
        for name in eaten.keys():
            if(name in table[x] and eaten[name] > 0):
                table[x].remove(name)
                sushi -= 1
                eaten[name] -= 1

            if (eaten[name] == 0):
                people -= 1
                eaten[name] = -1

    elif(a[0] == '200'): # 손님오기
        rotate(table)
        method, t, x, name, n = a
        people += 1
   
        t = int(t)
        curr_time = t
        x = int(x)
        n = int(n)
        people_location[name] = x
        eaten[name] = n
        eat(table, method, people_location, eaten)
        
    
    else:  # 사진촬영
        method, t = a
        t = int(t)
        for i in range(t - curr_time):
            rotate(table)
            eat(table, method, people_location, eaten)
            
        curr_time = t

        print(f"{people} {sushi}")