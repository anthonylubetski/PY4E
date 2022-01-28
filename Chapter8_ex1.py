def chop(lst):
    del lst[0] #removes first element
    del lst[-1] #removes last element
def middle(lst):
    new = lst[1:] #stores all but first element
    del new[-1] #deletes last element
    return new
my_list = [1,2,3,4,5,6,7,8,9]
my_list2 = [1,2,3,4,5,6,7,8,9]
chop_list = chop(my_list)
print(my_list) #should be [2,3,4,5,6,7,8]
print(chop_list) # should be None
middle_list = middle(my_list2)
print(my_list2) #Should be unchanged
print(middle_list) # Should be [2,3,4,5,6,7,8]
