# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/DicomBrowserWin.ui'
#
# Created: Mon Nov 14 17:33:29 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_DicomBrowserWin(object):
    def setupUi(self, DicomBrowserWin):
        DicomBrowserWin.setObjectName(_fromUtf8("DicomBrowserWin"))
        DicomBrowserWin.resize(1188, 843)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/image.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DicomBrowserWin.setWindowIcon(icon)
        DicomBrowserWin.setAnimated(False)
        self.centralwidget = QtGui.QWidget(DicomBrowserWin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.listSplit = QtGui.QSplitter(self.centralwidget)
        self.listSplit.setOrientation(QtCore.Qt.Horizontal)
        self.listSplit.setChildrenCollapsible(False)
        self.listSplit.setObjectName(_fromUtf8("listSplit"))
        self.sourceGroup = QtGui.QGroupBox(self.listSplit)
        self.sourceGroup.setObjectName(_fromUtf8("sourceGroup"))
        self.gridLayout = QtGui.QGridLayout(self.sourceGroup)
        self.gridLayout.setContentsMargins(3, 6, 6, 6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listView = QtGui.QListView(self.sourceGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMinimumSize(QtCore.QSize(50, 0))
        self.listView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.importButton = QtGui.QPushButton(self.sourceGroup)
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.horizontalLayout_2.addWidget(self.importButton)
        self.statusText = QtGui.QLabel(self.sourceGroup)
        self.statusText.setText(_fromUtf8(""))
        self.statusText.setObjectName(_fromUtf8("statusText"))
        self.horizontalLayout_2.addWidget(self.statusText)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.statusProgressBar = QtGui.QProgressBar(self.sourceGroup)
        self.statusProgressBar.setMaximumSize(QtCore.QSize(200, 16777215))
        self.statusProgressBar.setMaximum(1)
        self.statusProgressBar.setProperty("value", 0)
        self.statusProgressBar.setObjectName(_fromUtf8("statusProgressBar"))
        self.gridLayout.addWidget(self.statusProgressBar, 1, 0, 1, 1)
        self.seriesGroup = QtGui.QGroupBox(self.listSplit)
        self.seriesGroup.setObjectName(_fromUtf8("seriesGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.seriesGroup)
        self.gridLayout_2.setContentsMargins(3, 6, 6, 6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.numLabel = QtGui.QLabel(self.seriesGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numLabel.sizePolicy().hasHeightForWidth())
        self.numLabel.setSizePolicy(sizePolicy)
        self.numLabel.setMinimumSize(QtCore.QSize(30, 0))
        self.numLabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.numLabel.setObjectName(_fromUtf8("numLabel"))
        self.horizontalLayout.addWidget(self.numLabel)
        self.imageSlider = QtGui.QSlider(self.seriesGroup)
        self.imageSlider.setPageStep(1)
        self.imageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.imageSlider.setInvertedAppearance(False)
        self.imageSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.imageSlider.setTickInterval(1)
        self.imageSlider.setObjectName(_fromUtf8("imageSlider"))
        self.horizontalLayout.addWidget(self.imageSlider)
        self.autoLevelsCheck = QtGui.QCheckBox(self.seriesGroup)
        self.autoLevelsCheck.setChecked(True)
        self.autoLevelsCheck.setObjectName(_fromUtf8("autoLevelsCheck"))
        self.horizontalLayout.addWidget(self.autoLevelsCheck)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.seriesSplit = QtGui.QSplitter(self.seriesGroup)
        self.seriesSplit.setOrientation(QtCore.Qt.Vertical)
        self.seriesSplit.setChildrenCollapsible(False)
        self.seriesSplit.setObjectName(_fromUtf8("seriesSplit"))
        self.tableView = QtGui.QTableView(self.seriesSplit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(50, 0))
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(10)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(30)
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setCascadingSectionResizes(False)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.seriesTab = QtGui.QTabWidget(self.seriesSplit)
        self.seriesTab.setTabPosition(QtGui.QTabWidget.North)
        self.seriesTab.setTabShape(QtGui.QTabWidget.Rounded)
        self.seriesTab.setDocumentMode(False)
        self.seriesTab.setObjectName(_fromUtf8("seriesTab"))
        self.metaTab = QtGui.QWidget()
        self.metaTab.setObjectName(_fromUtf8("metaTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.metaTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tagView = QtGui.QTreeView(self.metaTab)
        self.tagView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tagView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tagView.setProperty("showDropIndicator", False)
        self.tagView.setDragDropOverwriteMode(False)
        self.tagView.setAlternatingRowColors(True)
        self.tagView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tagView.setTextElideMode(QtCore.Qt.ElideRight)
        self.tagView.setSortingEnabled(True)
        self.tagView.setObjectName(_fromUtf8("tagView"))
        self.gridLayout_4.addWidget(self.tagView, 0, 0, 1, 1)
        self.seriesTab.addTab(self.metaTab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.seriesSplit, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.listSplit, 0, 0, 1, 1)
        DicomBrowserWin.setCentralWidget(self.centralwidget)
        self.action_Quit = QtGui.QAction(DicomBrowserWin)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_Open_Directory = QtGui.QAction(DicomBrowserWin)
        self.action_Open_Directory.setObjectName(_fromUtf8("action_Open_Directory"))

        self.retranslateUi(DicomBrowserWin)
        self.seriesTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DicomBrowserWin)

    def retranslateUi(self, DicomBrowserWin):
        DicomBrowserWin.setWindowTitle(_translate("DicomBrowserWin", "Dicom Browser (RESEARCH ONLY)", None))
        self.sourceGroup.setTitle(_translate("DicomBrowserWin", "Dicom Sources", None))
        self.importButton.setText(_translate("DicomBrowserWin", "Import...", None))
        self.statusProgressBar.setFormat(_translate("DicomBrowserWin", "%p% (%v / %m)", None))
        self.seriesGroup.setTitle(_translate("DicomBrowserWin", "Series", None))
        self.numLabel.setText(_translate("DicomBrowserWin", "0", None))
        self.autoLevelsCheck.setText(_translate("DicomBrowserWin", "Auto Levels", None))
        self.seriesTab.setTabText(self.seriesTab.indexOf(self.metaTab), _translate("DicomBrowserWin", "Metadata", None))
        self.action_Quit.setText(_translate("DicomBrowserWin", "&Quit", None))
        self.action_Open_Directory.setText(_translate("DicomBrowserWin", "&Open Directory", None))

import Resources_rc
