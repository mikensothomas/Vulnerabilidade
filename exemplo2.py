import xml.etree.ElementTree as ET

xml_data = """
<root>
  <name>John</name>
  <ssn>&xxe;</ssn>
</root>
"""

parser = ET.XMLParser()
parser.entity["xxe"] = "file:///etc/passwd"
parser.entity["&xxe;"] = "file:///etc/passwd"

try:
    root = ET.fromstring(xml_data, parser=parser)
    print("Name:", root.find("name").text)
    print("SSN:", root.find("ssn").text)
except ET.ParseError as e:
    print("Erro de parsing XML:", e)
