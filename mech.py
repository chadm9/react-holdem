import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html
from lxml import etree

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

url = 'https://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-52052007'
r = Render(url)  
result = r.frame.toHtml()
print result
#This step is important.Converting QString to Ascii for lxml to process
archive_links = html.fromstring(str(result.toAscii()))
print archive_links.content
root = etree.HTML(str(result.toAscii()))
print root.content

price = root.xpath('//div[@class="price"]')
# price = archive_links.xpath('//div[@class="price"]')
print price
