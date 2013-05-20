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
