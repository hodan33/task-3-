def fn (list,x,y):
    for i in list[x:y] :
        for x in range (1,max(list)):
            if i/x==x :
                print(i)
fn([1,3,10000,6,9,16,22,25,29,64,69,70,81],1,6)


