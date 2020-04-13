#coding:utf-8
class CLanguage :
    # 下面定义了2个类变量
    def __init__(self,name):
        #下面定义 2 个实例变量
        self.name = name
        print(name)
    # 下面定义了一个say实例方法
    def say(self,name):
        print(self,name)
if __name__ == '__main__':
    a = CLanguage('ljc')
    a.say('小明')
