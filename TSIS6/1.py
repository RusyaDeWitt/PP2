def max_of_three():
    max = 0
    for i in range(3):
        d = int(input())
        if(d > max):
            max = d

    print(max)

max_of_three()