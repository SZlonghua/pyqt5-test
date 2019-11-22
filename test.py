# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import dialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 513)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 23))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        self.menu_Tools = QtWidgets.QMenu(self.menubar)
        self.menu_Tools.setObjectName("menu_Tools")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew_Program = QtWidgets.QAction(MainWindow)
        self.actionnew_Program.setCheckable(False)
        self.actionnew_Program.setChecked(False)
        self.actionnew_Program.setObjectName("actionnew_Program")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionsetting = QtWidgets.QAction(MainWindow)
        self.actionsetting.setObjectName("actionsetting")
        self.actionSave_All = QtWidgets.QAction(MainWindow)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menu_File.addAction(self.actionnew_Program)
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionSave_All)
        self.menu_File.addAction(self.actionsetting)
        self.menu_Help.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.actionnew_Program.triggered.connect(self.newProject)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "liaotao"))
        self.menu_File.setTitle(_translate("MainWindow", "File"))
        self.menu_Edit.setTitle(_translate("MainWindow", "Edit"))
        self.menu_View.setTitle(_translate("MainWindow", "View"))
        self.menu_Tools.setTitle(_translate("MainWindow", "Tools"))
        self.menu_Help.setTitle(_translate("MainWindow", "Help"))
        self.actionnew_Program.setText(_translate("MainWindow", "New Project"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionsetting.setText(_translate("MainWindow", "Settings..."))
        self.actionSave_All.setText(_translate("MainWindow", "Save All"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

    def newProject(self):
        Dialog = QtWidgets.QDialog(self.centralwidget)
        ui_dialog = dialog.Ui_Dialog()
        ui_dialog.setupUi(Dialog)
        Dialog.show()