#coding:utf-8
class CLanguage :
    # 下面定义了2个类变量
    name = 'xiaoming'
    def __init__(self):
        #下面定义 2 个实例变量
        print(self.name)
    # 下面定义了一个say实例方法
    def say(self,name):
        print(self,name)
if __name__ == '__main__':
    a = CLanguage()
    a.say('ljc')
