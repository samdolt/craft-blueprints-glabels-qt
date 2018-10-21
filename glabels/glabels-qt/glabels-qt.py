# -*- coding: utf-8 -*-

import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = 'https://github.com/jimevins/glabels-qt.git'
        self.defaultTarget = 'master'
        self.description = "glabels-qt"

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtsvg"] = None
        self.runtimeDependencies["libs/qt5/qttools"] = None
        self.runtimeDependencies["libs/qrencode"] = None


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args = "-DQt5_DIR=%s -DBUILD_STANDALONE=OFF" % CraftStandardDirs.craftRoot()