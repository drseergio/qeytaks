# -*- coding: utf-8 -*-

'''controller.py: sets-up Qt GUI and handles UI events.'''

__author__ = 'drseergio@gmail.com (Sergey Pisarenko)'

import sys

from PyQt4 import QtCore, QtGui

from qeytaks import _DIFFERENT_VAL, _TAG_DIFF_CHAR
from qeytaks.model import PhotoModel
from qeytaks.ui_mainwindow import Ui_MainWindow


class QeyTaks(object):
  def __init__(self, args):
    self.app = QtGui.QApplication(args)
    self.gui = Ui_MainWindow()
    self.model = PhotoModel()

    window = QtGui.QMainWindow()
    self.gui.setupUi(window)
    self.gui.imageList.setModel(self.model)
    self.gui.imageList.keyPressEvent = self._ListKeyEvent
    window.show()

    self.app.connect(
        self.gui.imageList,
        QtCore.SIGNAL('dropped'),
        self._AddPhotos)
    self.app.connect(
        self.gui.imageList.selectionModel(),
        QtCore.SIGNAL('selectionChanged(QItemSelection, QItemSelection)'),
        self._PhotosSelected)
    self.app.connect(
        self.gui.clearBtn,
        QtCore.SIGNAL('clicked()'),
        self.model.ClearPhotos)
    self.app.connect(
        self.gui.addPhotosBtn,
        QtCore.SIGNAL('clicked()'),
        self._SelectFiles)
    self.app.connect(
        self.gui.saveBtn,
        QtCore.SIGNAL('clicked()'),
        self._SaveChanges)
    self.app.connect(
        self.gui.tagEdit,
        QtCore.SIGNAL('textChanged()'),
        self._ValueEdited)

    sys.exit(self.app.exec_())

  def _AddPhotos(self, files):
    progress = QtGui.QProgressDialog('Loading photos...', '', 0, 0)
    progress.setWindowModality(QtCore.Qt.WindowModal)
    progress.setWindowTitle('qeytaks')
    progress.show()
    progress.setAutoClose(True)
    progress.setCancelButton(None)
    progress.setMaximum(len(files))
    progress.setMinimum(0)

    i = 0
    for path in files:
      i += 1
      self.model.AddPhoto(path)
      progress.setValue(i)

    progress.close()

  def _ValueEdited(self):
    self.gui.saveBtn.setEnabled(True)

  def _SelectFiles(self):
    files = QtGui.QFileDialog.getOpenFileNames()
    self._AddPhotos(files)

  def _SaveChanges(self):
    progress = QtGui.QProgressDialog('Applying changes...', '', 0, 0)
    progress.setWindowModality(QtCore.Qt.WindowModal)
    progress.setWindowTitle('qeytaks')
    progress.show()
    progress.setAutoClose(True)
    progress.setCancelButton(None)
    progress.setMaximum(len(self.model.paths))
    progress.setMinimum(0)

    self.model.SaveChanges(
        str(self.gui.tagEdit.toPlainText()),
        str(self.gui.labelEdit.text()),
        [i.row() for i in self.gui.imageList.selectedIndexes()],
        progress)
    self.gui.imageList.clearSelection()
    progress.close()

  def _ListKeyEvent(self, event):
    if event.key() == QtCore.Qt.Key_Delete:
      self.model.RemovePhotos(self.gui.imageList.selectedIndexes())
      self.gui.imageList.clearSelection()
    elif (event.key() == QtCore.Qt.Key_A and
          event.modifiers() & QtCore.Qt.ControlModifier):
      self.gui.imageList.selectAll()
    elif (event.key() == QtCore.Qt.Key_D and
          event.modifiers() & QtCore.Qt.ControlModifier):
      self.gui.imageList.clearSelection()

  def _PhotosSelected(self, _new_select, _old_select):
    if len(self.gui.imageList.selectedIndexes()) == 0:
      self.gui.tagEdit.setEnabled(False)
      self.gui.tagEdit.setText('')
      self.gui.labelEdit.setEnabled(False)
      self.gui.labelEdit.setText('')
      self.gui.saveBtn.setEnabled(False)
      return

    self.gui.tagEdit.setEnabled(True)
    self.gui.labelEdit.setEnabled(True)

    paths = [self.model.paths[index.row()] for index in
        self.gui.imageList.selectedIndexes()]
    labels = [self.model.labels[path] for path in paths]

    if len(set(labels)) == 1:
      if labels[0]:
        self.gui.labelEdit.setText(labels[0])
    else:
      self.gui.labelEdit.setText(_DIFFERENT_VAL)

    self.gui.tagEdit.setText(self._CreateTagString(paths))

  def _CreateTagString(self, paths):
    tags_show = {}
    for tag in self.model.tags.keys():
      for path in paths:
        if path in self.model.tags[tag]:
          if not tag in tags_show.keys():
            tags_show[tag] = 0
          tags_show[tag] += 1
    tags_common = [tag for tag in tags_show.keys() if
        tags_show[tag] == len(paths)]
    tags_different = set(tags_show.keys()).difference(tags_common)
    return ', '.join(
        tags_common + [
            '%s%s' % (_TAG_DIFF_CHAR, tag) for tag in tags_different])
