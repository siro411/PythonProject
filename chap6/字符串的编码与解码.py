s='伟大的中国梦'
scode=s.encode(errors='replace')
print(scode)
scode_gbk=s.encode('gbk',errors='replace')
print(scode_gbk)

#ignore忽略
#strict提示编码错误
#replace 替换成问号？
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode,'utf-8',errors='replace'))