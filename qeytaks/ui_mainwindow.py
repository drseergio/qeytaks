# -*- coding: utf-8 -*-

'''ui_mainwindow.py: mostly-generated PyQt UI code.'''

__author__ = 'drseergio@gmail.com (Sergey Pisarenko)'

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(558, 434)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.imageList = DragDropListView(self.layoutWidget)
        self.imageList.setDragEnabled(True)
        self.imageList.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.imageList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.imageList.setObjectName(_fromUtf8("imageList"))
        self.imageList.setFrameShape(QtGui.QFrame.StyledPanel)
        self.imageList.setAlternatingRowColors(True)
        self.imageList.setIconSize(QtCore.QSize(72, 72))
        self.gridLayout_3.addWidget(self.imageList, 1, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.clearBtn = QtGui.QPushButton(self.layoutWidget)
        self.clearBtn.setObjectName(_fromUtf8("clearBtn"))
        self.gridLayout_5.addWidget(self.clearBtn, 0, 1, 1, 1)
        self.saveBtn = QtGui.QPushButton(self.layoutWidget)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.saveBtn.setEnabled(False)
        self.gridLayout_5.addWidget(self.saveBtn, 0, 2, 1, 1)
        self.addPhotosBtn = QtGui.QPushButton(self.layoutWidget)
        self.addPhotosBtn.setObjectName(_fromUtf8("addPhotosBtn"))
        self.gridLayout_5.addWidget(self.addPhotosBtn, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tagEdit = QtGui.QTextEdit(self.groupBox)
        self.tagEdit.setObjectName(_fromUtf8("tagEdit"))
        self.tagEdit.setEnabled(False)
        self.gridLayout.addWidget(self.tagEdit, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.labelEdit = QtGui.QLineEdit(self.groupBox)
        self.labelEdit.setObjectName(_fromUtf8("labelEdit"))
        self.labelEdit.setEnabled(False)
        self.gridLayout.addWidget(self.labelEdit, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAdd_photos = QtGui.QAction(MainWindow)
        self.actionAdd_photos.setObjectName(_fromUtf8("actionAdd_photos"))
        self.actionClear_list = QtGui.QAction(MainWindow)
        self.actionClear_list.setObjectName(_fromUtf8("actionClear_list"))
        self.actionSave_tags = QtGui.QAction(MainWindow)
        self.actionSave_tags.setObjectName(_fromUtf8("actionSave_tags"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "qeytaks", None))
        self.label_5.setText(_translate("MainWindow", "Photo files", None))
        self.clearBtn.setText(_translate("MainWindow", "Clear list", None))
        self.saveBtn.setText(_translate("MainWindow", "Save", None))
        self.addPhotosBtn.setText(_translate("MainWindow", "Add photos", None))
        self.groupBox.setTitle(_translate("MainWindow", "Edit metadata", None))
        self.label.setText(_translate("MainWindow", "Keywords", None))
        self.label_2.setText(_translate("MainWindow", "Label", None))
        self.actionAdd_photos.setText(_translate("MainWindow", "Add photos", None))
        self.actionClear_list.setText(_translate("MainWindow", "Clear list", None))
        self.actionSave_tags.setText(_translate("MainWindow", "Save", None))


class DragDropListView(QtGui.QListView):
    def __init__(self, type, parent=None):
        super(DragDropListView, self).__init__(parent)
        self.setAcceptDrops(True)
 
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
 
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
 
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            l = []
            for url in event.mimeData().urls():
                l.append(str(url.toLocalFile()))
            self.emit(QtCore.SIGNAL("dropped"), l)
        else:
            event.ignore()
