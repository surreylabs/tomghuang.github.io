---
layout: post2
title:  "Using PySide to Create Qt-based Applications in Python"
date:   2011-03-09 10:12:04
tags: python qt libraries
---

[PySide][pyside] provides LGPL-licensed Python bindings for the Qt C++ framework. It allows both open source and commercial software development, and supports most of the platforms as Qt itself.

The benefit of using PySide instead of Qt is that you don’t need to setup complicated C++ development environment. With Python and PySide, you can write simple or complex cross-platform applications right away. If you have installed Python 2.7 and PySide 1.0.0 on your machine, you can try the following script in your console:

```python
#!/usr/bin/python
 
# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
 
# Create a Qt application 
app = QApplication(sys.argv)
# Create a Label and show it
label = QLabel("Hello World")
label.show()

# Enter Qt application main loop
app.exec_()
sys.exit()
```

Executing the script will launch a small window with a label in it, and you can start adding other Qt components to make it more useful. For more information on using PySide, you can see the official [PySide Documentation][pyside-doc] and some great Qt books, such as [C++ GUI Programming with Qt 4][cpp-gui-programming-with-qt4].

[pyside]: http://www.pyside.org/
[pyside-doc]: http://developer.qt.nokia.com/wiki/PySideDocumentation/
[cpp-gui-programming-with-qt4]: http://www.amazon.com/Programming-Prentice-Source-Software-Development/dp/0132354160/ref=sr_1_1?s=books&ie=UTF8&qid=1299737275&sr=1-1

