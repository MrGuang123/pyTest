from urllib.request import urlopen
from lxml import etree

# xpath基本使用

text = '''
  <div>
    <ul>
      <li class="item-0"><a href="link1.html">first item</a></li>
      <li class="item-1"><a href="link2.html">second item</a></li>
      <li class="item-inactive"><a href="link3.html">third item</a></li>
      <li class="item-1"><a href="link4.html">fourth item</a></li>
      <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
  </div>
'''
text1 = '''
  <li class="li li-first"><a href="link1.html">first item</a></li>
'''
text2 = '''
  <li class="li li-first" name="item"><a href="link1.html">first item</a></li>
'''

# # 构造一个xpath解析对象
# html = etree.HTML(text)
# # tostring方法可以修正错误的HTML代码
# result = etree.tostring(html)
# # decode方法将其转换为str类型
# print(result.decode('utf-8'))

# 无法运行
# html = etree.parse('test.html')
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# //li[@class="item-0"]/a/text()获取a下面的文字，//li[@class="item-0"]//text()获取所有子节点
# html = etree.HTML(text)
# result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)

# 获取属性
# html = etree.HTML(text)
# result = html.xpath('//li/a/@href')
# print(result)

# 属性有多个值的时候匹配
# html = etree.HTML(text1)
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)

# 多个属性匹配一个节点
# html = etree.HTML(text2)
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)

# 选择匹配到的所有数据的某个数据
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position() < 3]/a/text()')
# print(result)
# result = html.xpath('//li[last() - 2]/a/text()')
# print(result)

# 节点轴的选择，子元素，兄弟元素，父元素，祖先元素等
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)
