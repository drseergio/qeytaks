qeytaks
=======

qeytaks is a keyword editor for photos. qeytaks lets you edit IPTC keywords and
set XMP label.

I wrote qeytaks for my own usage as it nicely fits with my photo workflow
and integrates well with usage of photofs.

qeytaks is licensed under GPLv3

Installation
=======

qeytaks uses setuptools. To install qeytaks run the following command
```
$ sudo python setup.py install
```

Example usage:
=======

```
$ python qeytaks.py [list-of-paths-to-photos]
```

KDE integration
=======

To enable context right-click menu that invokes qeytaks do the following:

  1. check what is your service path in KDE:

```
$ kde4-config --path services
/home/drseergio/.kde4/share/kde4/services/:/usr/share/kde4/services/
```

  2. create ServiceMenus folder if it does not exist:

```
$ mkdir -p ~/.kde4/share/kde4/services/ServiceMenus
```

  3. put a file called "qeytaks.desktop" in that folder:

```
$ vi ~/.kde4/share/kde4/services/ServiceMenus/qeytaks.desktop

[Desktop Entry]
Actions=qeytaks
MimeType=image/*
ServiceTypes=KonqPopupMenu/Plugin
Type=Service
X-KDE-Priority=TopLevel

[Desktop Action qeytaks]
Exec=/usr/bin/qeytaks %U
Name=Edit photo tags
```


Dependencies
=======

  * GExiv2 library version 0.6.0 or newer with enabled introspection
  (Gentoo ebuild =media-libs/gexiv2-0.6.0 with USE flag "introspection")

  * exiv2 library with XMP support
  (Gentoo ebuild media-gfx/exiv2 with USE flag "xmp")

  * pygobject (Gentoo ebuild dev-python/pygobject)

  * PyQt4 (Gentoo ebuild dev-python/PyQt4)

If not available in your distribution, GExiv2 can be downloaded from:
http://redmine.yorba.org/projects/gexiv2/wiki
