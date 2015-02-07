#########################################################
## customize Title bar
## dotpy.ir
## iraj.jelo@gmail.com
#########################################################
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt


class TitleBar(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        css = """

QWidget
{
Background: rgb(255,0,0);
color:white;
font_family: Segoe UI;
font:12px bold;
font-weight:bold;
border-radius: 1px;
height: 11px;

}
QDialog{
font-size:12px;
color: black;

}
QToolButton{
Background: rgb(0,240,0);
font-size:13px;
}
QToolButton:hover{
Background: rgb(230,0,0);
font-size:13px;
}
"""

        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css) 

        self.minimize=QtGui.QToolButton(self);
        self.minimize.setIcon(QtGui.QIcon('img/min.png'));

        self.maximize=QtGui.QToolButton(self);
        self.maximize.setIcon(QtGui.QIcon('img/max.png'));

        close=QtGui.QToolButton(self);
        close.setIcon(QtGui.QIcon('img/close.png'));

        self.minimize.setMinimumHeight(10);
        close.setMinimumHeight(10);
        self.maximize.setMinimumHeight(10);

        label=QtGui.QLabel(self);
        label.setText("Window Title");
        self.setWindowTitle("Window Title");
        hbox=QtGui.QHBoxLayout(self);

        hbox.addWidget(label);
        hbox.addWidget(self.minimize);
        hbox.addWidget(self.maximize);
        hbox.addWidget(close);
        hbox.insertStretch(1,500);
        hbox.setSpacing(0);
        self.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed);
        self.maxNormal=False;

        close.clicked.connect(self.close);
        self.minimize.clicked.connect(self.showSmall);
        self.maximize.clicked.connect(self.showMaxRestore);


    def showSmall(self):
        box.showMinimized();

    def showMaxRestore(self):
        if(self.maxNormal):
            box.showNormal();
            self.maxNormal= False;
            self.maximize.setIcon(QtGui.QIcon('img/max.png'));
            print('1')

        else:
            box.showMaximized();
            self.maxNormal=  True;
            print ('2')
            self.maximize.setIcon(QtGui.QIcon('img/max2.png'));

    def close(self):
        box.close()

    def mousePressEvent(self,event):

        if event.button() == Qt.LeftButton:
            box.moving = True; box.offset = event.pos()

    def mouseMoveEvent(self,event):
        if box.moving: box.move(event.globalPos()-box.offset)


class Frame(QtGui.QFrame):
    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self, parent)
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        css = """

QFrame

{
Background:  #FFFFHF;


color:white;
font:13px ;
font-weight:bold;

}


"""


        self.setStyleSheet(css) 
        self.setWindowFlags(Qt.FramelessWindowHint);
        self.setMouseTracking(True);
        self.m_titleBar= TitleBar(self);
        self.m_content= QtGui.QWidget(self);

        vbox=QtGui.QVBoxLayout(self);
        vbox.addWidget(self.m_titleBar);
        vbox.setMargin(0);
        vbox.setSpacing(0);
        layout=QtGui.QVBoxLayout(self);
        layout.addWidget(self.m_content);
        layout.setMargin(5);
        layout.setSpacing(0);
        vbox.addLayout(layout);
        # Allows you to access the content area of the frame
        # where widgets and layouts can be added
    def contentWidget(self):
        return self.m_content
    def titleBar(self):
        return self.m_titleBar

    def mousePressEvent(self,event):
        self.m_old_pos = event.pos();
        self.m_mouse_down = event.button()== Qt.LeftButton;
    def mouseMoveEvent(self,event):

        x=event.x();
        y=event.y();

    def mouseReleaseEvent(self,event):
        m_mouse_down=False;




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv);
    box = Frame()
    box.move(60,60);
    l=QtGui.QVBoxLayout(box.contentWidget());
    l.setMargin(0);
    edit=QtGui.QLabel("""Hello World

                          """);
    l.addWidget(edit)
    box.show()
