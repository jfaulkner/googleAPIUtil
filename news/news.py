#!/usr/bin/python
import feedparser
import xml.etree.cElementTree as ET
from xml.dom import minidom

URL = 'http://feeds.bbci.co.uk/news/rss.xml'
BBCHOME = feedparser.parse(URL)

def prettify(elem):
  rough_string = ET.tostring(elem, 'utf-8')
  reparsed = minidom.parseString(rough_string)
  return reparsed.toprettyxml(indent="  ")

root = ET.Element('root')
print '{} entries found'.format(len(BBCHOME.entries))

for story in BBCHOME.entries:
  item = ET.SubElement(root,'item')
  title = ET.SubElement(item,'title')
  title.text = story.title.encode('latin-1', 'ignore')
  description = ET.SubElement(item,'description')
  description.text = story.description.encode('latin-1', 'ignore')
  link = ET.SubElement(item,'link')
  link.text = story.link.encode('latin-1', 'ignore')
  #print prettify(root)
  print '{} : {} ({})'.format(title.text, description.text, link.text)
  print ''
