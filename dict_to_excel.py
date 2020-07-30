import pandas as pd
dict=d={'天空': 24, '影子': 18, '孩子': 17, '人们': 15, '眼睛': 15, '石头': 15, '太阳': 13, '世界': 12, '黎明': 11, '窗户': 11}
name=list(dict.keys())
value=list(dict.values())
data={'name':name,'value':value}
df = pd.DataFrame(data,columns=['name','value'])
df.to_excel('./树-矩形树-类饼图.xlsx')