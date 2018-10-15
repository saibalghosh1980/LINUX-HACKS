import sys
print('-------------------File instrumentation started------------------------------')
filename = ''.join(['./',str(sys.argv[1])])
print(filename)
from xml.dom import minidom
root = minidom.parse(
    filename).documentElement
hawtioNode = ("<dependency>" +
              "<groupId>io.hawt</groupId>" +
              "<artifactId>hawtio-springboot</artifactId>" +
              "<version>2.1.0</version>" +
              "</dependency >")
child = minidom.parseString(hawtioNode).documentElement
for node in root.getElementsByTagName('dependencies'):
    # print(node.parentNode.nodeName)
    if node.parentNode.nodeName == "project":
        #print(node.parentNode.nodeName)
        node.appendChild(child)
# print(root.toprettyxml())
with open(filename, 'w') as f:
    f.write(root.toprettyxml())
print('-------------------File is instrumented------------------------------')