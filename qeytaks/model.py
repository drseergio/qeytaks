# -*- coding: utf-8 -*-

'''model.py: underlying model of photo data.'''

__author__ = 'drseergio@gmail.com (Sergey Pisarenko)'

import logging
import os
import sys

from PyQt4 import QtCore, QtGui

try:
  from gi.repository import GExiv2
except ImportError:
  print ('You must have GExiv2 installed, please visit:\n'
         'http://redmine.yorba.org/projects/gexiv2/wiki')
  sys.exit(1)

_LABEL_TAG = 'Xmp.xmp.Label'
_TAG_TAG = 'Iptc.Application2.Keywords'

from qeytaks import _DIFFERENT_VAL, _TAG_DIFF_CHAR


class PhotoModel(QtCore.QAbstractListModel):
  def __init__(self):
    super(PhotoModel, self).__init__()
    self.paths = []
    self.photos = {}
    self.tags = {}
    self.labels = {}

  def rowCount(self, parent=QtCore.QModelIndex()):
    return len(self.paths)

  def data(self, index, role):
    if not index.isValid or index.row() > len(self.paths):
      return QtCore.QVariant()

    path = self.paths[index.row()]
    if role == QtCore.Qt.DisplayRole:
      return QtCore.QVariant(self.photos[path].name())

    if role == QtCore.Qt.DecorationRole:
      return self.photos[path].icon

    return QtCore.QVariant()

  def AddPhoto(self, path):
    path = os.path.abspath(str(path))

    if path in self.paths or not os.path.isfile(path):
      return

    tags = []
    try:
      gexiv2_meta = GExiv2.Metadata(path)
      tags = gexiv2_meta.get_tag_multiple(_TAG_TAG)
      self.labels[path] = gexiv2_meta.get(_LABEL_TAG)
    except Exception, e:
      logging.error('Failed adding %s', path)
      logging.exception(e)
      return

    self.beginInsertRows(QtCore.QModelIndex(), 0, 0)
    self.paths.append(path)
    photo = Photo(path, tags)
    self.photos[path] = photo
    for tag in tags:
      if not tag in self.tags.keys():
        self.tags[tag] = []
      self.tags[tag].append(path)
    self.endInsertRows()

  def RemovePhotos(self, indexes):
    self.beginRemoveRows(QtCore.QModelIndex(), 0, 0)
    for index in indexes:
      path = self.paths[index.row()]
      del self.photos[path]
      del self.labels[path]
      for tag in self.tags.keys():
        if path in self.tags[tag]:
          self.tags[tag].remove(path)
      del self.paths[index.row()]
    self.endRemoveRows()

  def ClearPhotos(self):
    self.beginRemoveRows(QtCore.QModelIndex(), 0, 0)
    self.paths = []
    self.photos = {}
    self.tags = {}
    self.labels = {}
    self.endRemoveRows()

  def SaveChanges(self, tag_field, label_field, rows, progress):
    paths = [self.paths[row] for row in rows]
    gexivs = [GExiv2.Metadata(path) for path in paths]

    if not label_field == _DIFFERENT_VAL:
      for gexiv in gexivs:
        gexiv[_LABEL_TAG] = label_field
      for path in paths:
        self.labels[path] = label_field

    tags_all = tag_field.replace(' ', '').replace('\n', '').split(',')
    if len(tags_all) == 1 and not tags_all[0]:
      tags_opt = []
      tags_common = []
    else:
      tags_opt = [tag[1:] for tag in tags_all if tag[0] == _TAG_DIFF_CHAR]
      tags_common = [tag for tag in tags_all if tag[0] != _TAG_DIFF_CHAR]

    for i in range(len(paths)):
      progress.setValue(i)
      path = paths[i]
      gexiv = gexivs[i]
      tags_curr = self.photos[path].tags
      tags_new = tags_curr[:]

      for tag in tags_curr:
        if tag not in tags_opt and tag not in tags_common:
          tags_new.remove(tag)
          self.tags[tag].remove(path)

      for tag in tags_common:
        if tag not in tags_curr:
          tags_new.append(tag)
          if not tag in self.tags.keys():
            self.tags[tag] = []
          self.tags[tag].append(path)

      self.photos[path].tags = tags_new
      gexiv.set_tag_multiple(_TAG_TAG, tags_new)

    for gexiv in gexivs:
      gexiv.save_file()


class Photo(object):
  def __init__(self, path, tags):
    self.path = path
    self.icon = QtGui.QIcon(
        QtGui.QIcon(path).pixmap(72, 72))
    self.tags = tags

  def name(self):
    return os.path.basename(self.path)
