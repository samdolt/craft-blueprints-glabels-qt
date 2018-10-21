# -*- coding: utf-8 -*-

import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = 'https://github.com/jimevins/glabels-qt.git'
        self.defaultTarget = 'master'
        self.description = "gLabels Label Designer"
        self.displayName = "gLabels-qt"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["libs/qt5/qttools"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtsvg"] = None
        self.runtimeDependencies["libs/qrencode"] = None

class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        self.blacklist_file.append(os.path.join(os.path.dirname(__file__), 'blacklist.txt'))
    
    def createPackage(self):
        self.defines["website"] = "https://glabels.org/"
        self.defines["executable"] = "bin\\glabels-qt.exe"

        self.ignoredPackages.append("binary/mysql")

        return TypePackager.createPackage(self)