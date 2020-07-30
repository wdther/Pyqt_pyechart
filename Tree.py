import pandas as pd
class MyTree:
    
#如何实现类似于指针的效果：通过引用。将属性定义为对象，而不是确定的值


    def __init__(self,name,value=[]):
        self.name=name
        self.value=value
        self.children=[]
        if self.value:
            self.dict = {'name': self.name, 'value': self.value, 'children': self.children}
        else:
            self.dict = {'name': self.name, 'children': self.children}


        #dict没有包装，只是一个字典




    def add_link(self,self2):


        if len(self2.children) and self2.value:
            dictemp={'name':self2.name,'value':self2.value,'children':self2.children}
            if dictemp not in self.children:
                self.children.append(dictemp)
            
        elif self2.value:
            dictemp = {'name':self2.name,'value': self2.value}
            if dictemp not in self.children:
                self.children.append(dictemp)

        elif self2.children:
            dictemp = {'name': self2.name,'children':self2.children}
            if dictemp not in self.children:
                self.children.append(dictemp)

        else:
            dictemp = {'name': self2.name}
            if dictemp not in self.children:
                self.children.append(dictemp)

        #通过append 方法 可以添加多个子对象
        
        

    def children_to_dict(self):
        return self.children

    def dict_clean(self):
        if len(self.children) and self.value: #都不为空
             self.dict = {'name': self.name, 'value': self.value, 'children': self.children}
        elif self.value: #值不为空
            self.dict = {'name': self.name, 'value': self.value}
        elif self.children:
             self.dict = {'name': self.name, 'children': self.children}
        else:
            self.dict = {'name': self.name}

    def to_dict(self):
        self.dict_clean()
        return self.dict




#通过索引添加数据
#data3=[{'name': '爷爷5', 'children': [{'name': '姑妈', 'children': [{'name': '堂弟', 'value': 2}]}]}]

#一个问题是，它只能从根部开始连接

if __name__ == "__main__":
    # A=MyTree('A',10)
    # B=MyTree("B",20)
    # B2=MyTree('B2',20)
    # B3=MyTree('B3',20)
    # C=MyTree('C',30)
    # D=MyTree('D',40)
    # df = pd.read_excel(r"E:\5-程序设计\A-编程语言\01Python\自定义\Pyecharts\组合\template\树.xlsx", sheet_name='Sheet1')
    # df.fillna(0,inplace=True)
    A=MyTree('A',1)
    B=MyTree('B',1)
    B2=MyTree('B2',1)
    C=MyTree('C',1)

#期望，add_link 得到的是对象的引用，当对象发生变化时能够相应的变化
#还有一个问题：必须创建对象
    # A.add_link(B)
    # A.add_link(B2)
    # B.add_link(C)


    dic = A.to_dict()

    print(dic)

'''
规则：
1.只能从起始往终止方向连接，从根部往枝部 add_link()
2.被连接的节点子对象之前要连接好，如未连接，默认无子节点
'''


# B.add_link(C)  #C具有子节点吗？ 除非把C.add_link(D) 写在前面，否则并不具有子节点除非我们保留变量名而非变量值

# C.add_link(D)


