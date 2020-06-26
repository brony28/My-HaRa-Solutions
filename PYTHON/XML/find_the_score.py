#FIND THE SCORE



import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # c=len(node.attrib)
    # # your code goes here
    # for i in node:
    #     c=c+len(i.attrib)
    # return c
    return(len(node.attrib) + sum(get_attr_number(child) for child in node))


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


#    Ref: https://diveintopython3.net/xml.html