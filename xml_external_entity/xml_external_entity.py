
def xml_parse_noncompliant():
    from lxml import etree
    parser = etree.XMLParser()
    tree1 = etree.parse('resources/xxe.xml', parser)