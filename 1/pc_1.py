# -*- coding: utf-8 -*-

from string import maketrans

"""
看图的意思是每个字母都代表着其后两位的字母，a代表着c,b代表着d

然后下面给出了一堆乱七八糟的字母，估计是根据上面的规则，把这个杂乱的片段翻译成某个连接
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

encryptionStr = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb
gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

expresslyList = []
for str in encryptionStr:
    i = ord(str)
    if i < 121 and i > 96:
        expresslyList.append(chr(i + 2))
    elif i == 121:
        expresslyList.append('a')
    elif i == 122:
        expresslyList.append('b')
    else:
        expresslyList.append(str)
# print ''.join(expresslyList)

"""
看完自己翻译的语句后才知道python有个string.translate函数
Python maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
注：两个字符串的长度必须相同，为一一对应的关系。

from string import maketrans   # 必须调用 maketrans 函数。

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab);

以上实例输出结果如下：
th3s 3s str3ng 2x1mpl2....w4w!!!
"""

a = 'yzabcdefghijklmnopqrstuvwx'
b = 'abcdefghijklmnopqrstuvwxyz'
trans = maketrans(a, b)
print encryptionStr.translate(trans)
print 'map'.translate(trans)


print map(ord,'abc')
l = map(chr, xrange(256))
print ''.join(l)