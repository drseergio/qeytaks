#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''qeytaks is a tool to set keywords and labels in photos.'''

__author__ = 'drseergio@gmail.com (Sergey Pisarenko)'

import sys

from qeytaks.controller import QeyTaks


def main():
  QeyTaks(sys.argv)

if __name__ == '__main__':
  main()
