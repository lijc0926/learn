alist = [1,2,'3','hello',[3,3,3,]]
blist = [4,3]
def demo1():
    #列表切片
    print(alist[4])
    print(alist[-1])
    print(alist[::-1])
    print(alist[1:5])
    print(alist[::2])
def demo2():
    #增加元素
    alist.append('你好')
    print(alist)
    #删除元素
    alist.pop(-1)
    print(alist)
def demo3():
    #合并
    alist.extend(blist)
    print(alist)
    alist.pop(-1)
    alist.pop(-1)
    alist.append(blist)
    print(alist)
def demo4():
    #排序
    clist = [9,3,2,19,10]
    clist.sort()
    print(clist)
    #倒序
    clist.sort(reverse=True)
    print(clist)
def demo5():
    #去重
    dlist = [1,1,2,2,3,3,4,4,5,5]
    print(type(list(set(dlist))))
    print(list(set(dlist)))
def number():
    one = 1;two = 2;three=3
    print('{}'.format(5))
if __name__ == '__main__':
    number()