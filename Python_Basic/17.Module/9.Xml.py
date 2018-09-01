# xml模块:数据交换.出现在json之前

import xml.etree.ElementTree as ET


tree = ET.parse('xml_lesson') # 解析xml文件
root = tree.getroot() # 拿到xml文件里的data根对象
print(root.tag) # 打印根的标签名

for i in root:
    # print(i.tag) # 打印root下的标签名
    # print(i.attrib) # 打印子对象的属性
    for j in i:
        # print(j.tag)
        # print(j.attrib)
        print(j.text) # 获取像<year>2008</year>中的2008
        
# 遍历xml文档
# for child in root:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag, i.text)

# 只遍历year节点
# for node in root.iter("year"): # node就是那3条year标签
#     print(node.tag, node.text)


# 修改
for node in root.iter("year"):
    new_year = int(node.text) + 1 # 改值
    node.text = str(new_year) # 赋值
    node.set("updated", "yes") # 改属性

tree.write("xml_lesson") # 改的仅是内存里的值，并非文本，需重新创建一个文件进行保存,或覆盖原来文件


# 删除node
for country in root.findall("country"): # findall和find都是找标签用的，区别是findall能找多个
    rank = int(country.find("rank").text)
    if rank > 50:
        root.remove(country)
tree.write("abc.xml")


# 用代码去创建xml数据
'''
import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist") # 相当于创建了<data> </data>

name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
sex.text = "33"

# 另一个子目录
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = "19"

et = ET.ElementTree(new_xml) # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)
'''
