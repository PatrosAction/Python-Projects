# A fucnction that takes a list and target parameter
# [1,2,3,4,5,6,7,8,9,10]  3:  (0+9)/2   (0+5)/2 :2.5==3   
# multiple variables : middle , start ,end ,steps

def binarry_search(list,element):
    middle =0
    start = 0
    end = len(list)
    steps = 0
    
    while(start<=end):
        print("steps",steps, ":" ,str(list[start:end+1]))
        steps +=1
        middle = (start + end) //2
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle -1
        else:
            start = middle +1
            
    return -1
my_list = [1,2,3,4,5,6,7,8,9]
target = 1
binarry_search(my_list,target)