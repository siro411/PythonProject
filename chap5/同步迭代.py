# fruits={'apple','orange','pear','grape'} #集合是无序的
fruits=['apple','orange','pear','grape']
counts=[10,3,4,5]
for f,c in zip(fruits,counts):
    match f,c:
        case'apple',10:
            print('10个苹果')
        case'orange',3:
            print('3个orange')
        case'pear',4:
            print('4个pear')
        case'grape',5:
            print('5个grape')

