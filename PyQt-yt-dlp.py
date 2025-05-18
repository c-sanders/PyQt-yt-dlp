# The PyQt6 package has been installed in the following location;
#
#   /home/craig/python3/venv/lib/python3.13/site-packages/PyQt6
#
# To enable Python to use it, set the PYTHONPATH environment
# variable as follows;
#
#   export PYTHONPATH=/home/craig/python3/venv/lib/python3.13/site-packages


import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout,  QHBoxLayout, QTabWidget,
                             QLabel,       QPushButton, QFrame,
                             QLineEdit,    QCheckBox,   QGridLayout,
                             QFileDialog,  QScrollArea, QGroupBox,
                             QMenu)
from PyQt6.QtGui     import (QKeySequence, QAction)

# import yt_dlp
import json

import Tab1, Tab2, Tab3, Tab4


# Note : The layout looks as expected when the qss stylesheet is NOT
#        applied to this class.

useStylesheet = False


# Class : MyMainWindow
# ====================
#
# Inherits directly from class QWidget

class MyMainWindow(QMainWindow):

    def __init__(self, app):

        super().__init__()

        self.app = app

        self.createObjects()


    def setupUI(self):

        # Setup the widget which will be used as the main widget
        # by this class.

        self.setupMainWidget()

        self.connectSignalsToSlots()


    def createObjects(self):

        # The central pane is comprised of the following;
        #
        #   - URL pane  (groupBoxURL)
        #   - Config pane

        self.widgetCentral  = QWidget(parent=self)
        self.layoutCentral  = QVBoxLayout()

        self.createUrlPaneObjects()
        self.createConfigPaneObjects()
        self.createButtonPaneObjects()


    def createUrlPaneObjects(self) :

        # The URL pane.

        # Top-level container and layout.

        self.groupBoxURL      = QGroupBox("URL of filename to download :")
        self.layoutURL        = QVBoxLayout()

        # Child widgets.

        self.lineEditURL      = QLineEdit("https://www.youtube.com/watch?v=O89_U1gZfYU")
        # self.lineEditURL      = QLineEdit("https://www.youtube.com/watch?v=slbEMW05Y7A")

        self.frameButtonsURL  = QFrame()
        self.layoutButtonsURL = QHBoxLayout()

        self.buttonClear      = QPushButton("Clear URL")
        self.buttonHistory    = QPushButton("History")


    def createConfigPaneObjects(self) :

        # The config pane.

        # Top-level container and layout.

        self.groupBoxConfig      = QGroupBox("yt-dlp config :")
        self.layoutConfig        = QVBoxLayout()

        # Child widgets.

        self.labelOptions        = QLabel("Config filename :")
        self.lineEditOptions     = QLineEdit("/home/craig/source_code/python/PyQt/yt-dlp-options.json")

        self.frameButtonsConfig  = QFrame()
        self.layoutButtonsConfig = QHBoxLayout()

        self.buttonOpen          = QPushButton("Select")
        self.buttonLoad          = QPushButton("Load")
        self.buttonSave          = QPushButton("Save Config")

        self.createTabWidgetAndTabs()


    def createTabWidgetAndTabs(self) :

        # Tabbed widget and the 16 tabs which it contains.

        self.tabWidget      = QTabWidget()

        self.tab1           = Tab1.Tab1()
        self.tab2           = Tab2.Tab2()
        self.tab3           = Tab3.Tab3()
        self.tab4           = Tab4.Tab4()
        self.tab5           = QWidget()
        self.tab6           = QWidget()
        self.tab7           = QWidget()
        self.tab8           = QWidget()
        self.tab9           = QWidget()
        self.tab10          = QWidget()
        self.tab11          = QWidget()
        self.tab12          = QWidget()
        self.tab13          = QWidget()
        self.tab14          = QWidget()
        self.tab15          = QWidget()
        self.tab16          = QWidget()


    def createButtonPaneObjects(self) :

        # The config pane.

        # Top-level container and layout.

        self.frameButtons        = QFrame()
        self.layoutButtons       = QHBoxLayout()

        # Child widgets.

        self.buttonDownload      = QPushButton("Download")
        self.buttonExit          = QPushButton("Exit")


    def applyStylesheet(self) :

        if useStylesheet:

            with open("stylesheet_1.qss", "r") as qssFile :

                style = qssFile.read()

                print("++++++++++++++++++++++++++++++++++++++++")
                print("++++++++++++++++++++++++++++++++++++++++")
                print("Stylesheet = ", style)
                print("++++++++++++++++++++++++++++++++++++++++")
                print("++++++++++++++++++++++++++++++++++++++++")

                self.setStyleSheet(style)


    def setupMainWidget(self) :

        self.setWindowTitle("GUI frontend to yt-dlp")
        self.setCentralWidget(self.widgetCentral)

        self.widgetCentral.setLayout(self.layoutCentral)

        # Setup the menu bar.

        self.create_menu_bar()

        # Setup the central pane.

        self.setupCentralPane()


    def setupCentralPane(self) :

        self.layoutCentral.addWidget(self.groupBoxURL)
        self.layoutCentral.addWidget(self.groupBoxConfig)
        # self.layoutCentral.addWidget(self.frameTabs)
        self.layoutCentral.addWidget(self.frameButtons)

        # Setup the horizontal button pane for the URL.

        self.frameButtonsURL.setLayout(self.layoutButtonsURL)
        self.layoutButtonsURL.addWidget(self.buttonClear)
        self.layoutButtonsURL.addWidget(self.buttonHistory)

        # Setup the horizontal button pane for the yt-dlp config.

        self.frameButtonsConfig.setLayout(self.layoutButtonsConfig)
        self.layoutButtonsConfig.addWidget(self.buttonOpen)
        self.layoutButtonsConfig.addWidget(self.buttonLoad)
        self.layoutButtonsConfig.addWidget(self.buttonSave)

        # Setup the URL pane and the frame that surrounds it.

        # self.frameURL.setLayout(self.layoutURL)
        self.groupBoxURL.setLayout(self.layoutURL)
        # self.frameURL.setStyleSheet("border: 1px solid lightgrey;");
        # self.layoutURL.addWidget(self.labelURL)
        self.layoutURL.addWidget(self.lineEditURL)
        self.layoutURL.addWidget(self.frameButtonsURL)

        # self.layoutURL.addWidget(self.buttonOpen)
        # self.layoutURL.addWidget(self.buttonLoad)

        # Setup the Config pane and the frame that surrounds it.

        self.groupBoxConfig.setLayout(self.layoutConfig)
        self.layoutConfig.addWidget(self.labelOptions)
        self.layoutConfig.addWidget(self.lineEditOptions)
        self.layoutConfig.addWidget(self.frameButtonsConfig)
        self.layoutConfig.addWidget(self.tabWidget)

        # self.frameConfig.setStyleSheet(style)

        # self.frameURL.setStyleSheet("QFrame {border : 1px solid lightgrey;}")
        # self.frameConfig.setStyleSheet("QFrame {border : 1px solid pink;}")
        # self.labelOptions.setStyleSheet("QFrame {border : none;}")
        self.frameButtonsConfig.setStyleSheet("QFrame {border : 0px solid grey;}")

        self.lineEditURL.setStyleSheet("QLineEdit {border : 1px solid;}")

        self.groupBoxConfig.setObjectName("groupBoxConfig")

        # Setup the tabbed pane and the frame that surrounds it.

        # self.frameTabs.setLayout(self.layoutTabs)
        # self.layoutTabs.addWidget(self.tabWidget)

        # frameTab1 = QFrame()

        # Setup each of the 16 tabs.

        self.tab1.setupUI()
        self.tab2.setupUI()
        self.tab3.setupUI()
        self.tab4.setupUI()

        # TODO :
        # ======
        #
        # Put the following code into the Tab1, Tab2, etc
        # classes.

        # scrollAreaTab1 = QScrollArea()
        # scrollAreaTab1.setWidget(self.tab1)

        self.tabWidget.addTab(self.tab1, "1) General                  ")
        self.tabWidget.addTab(self.tab2, "2) Network                  ")
        self.tabWidget.addTab(self.tab3, "3) Geo-restriction          ")
        self.tabWidget.addTab(self.tab4, "4) Video Selection          ")
        self.tabWidget.addTab(self.tab5, "5) Download                 ")
        self.tabWidget.addTab(self.tab6, "6) Filesystem               ")
        self.tabWidget.addTab(self.tab8, "7) Thumbnail                ")
        self.tabWidget.addTab(self.tab9, "8) Internet Shortcut        ")
        self.tabWidget.addTab(self.tab10, "9) Verbosity and Simulation")
        self.tabWidget.addTab(self.tab11, "10) Workarounds            ")
        self.tabWidget.addTab(self.tab11, "11) Video Format            ")
        self.tabWidget.addTab(self.tab12, "12) Subtitle                ")
        self.tabWidget.addTab(self.tab13, "13) Authentication          ")
        self.tabWidget.addTab(self.tab14, "14) Post-Processing         ")
        self.tabWidget.addTab(self.tab15, "15) SponsorBlock            ")
        self.tabWidget.addTab(self.tab16, "16) Extractor               ")

        # layoutTab1 = QVBoxLayout()

        # frameTab1.setLayout(layoutTab1)
        # layoutTab1.addWidget(self.tab1)

        # Setup the buttons and the frame that surrounds them.

        # self.frameURL.setStyleSheet("border: 1px solid lightgrey;");

        self.frameButtons.setLayout(self.layoutButtons)
        self.layoutButtons.addWidget(self.buttonDownload)
        self.layoutButtons.addWidget(self.buttonExit)

        self.buttonHistory.setFixedSize(100, 30)
        self.buttonOpen.setFixedSize(100, 30)
        self.buttonLoad.setFixedSize(100, 30)
        self.buttonSave.setFixedSize(100, 30)
        self.buttonClear.setFixedSize(100, 30)
        self.buttonDownload.setFixedSize(100, 30)
        self.buttonExit.setFixedSize(100, 30)

        self.buttonExit.setToolTip("Exit the program.")
        self.buttonExit.setShortcut(QKeySequence("Ctrl+X"))


    def create_menu_bar(self) :

        menu_bar = self.menuBar()

        # Setup the File dropdown menu.

        fileMenu = QMenu("&File", self)

        self.quitAction = QAction("&Quit", self)
        self.exitAction = QAction("&Exit", self)

        # Setup the Edit dropdown menu.

        fileMenu.addAction(self.quitAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)

        # Setup the Help dropdown menu.

        helpMenu    = QMenu("&Help", self)
        aboutAction = QAction("&About", self)
        # paste_action = QAction("&Paste", self)

        helpMenu.addAction(aboutAction)
        # edit_menu.addAction(paste_action)

        menu_bar.addMenu(fileMenu)
        menu_bar.addMenu(helpMenu)


    def openFileNameDialog(self):

        # fileTypes should receive the type of files which were
        # searched for, i.e. *.json or *.*

        filename, blah = QFileDialog.getOpenFileName(
                           None,
                           "Open File",
                           "",
                           "JSON Files (*.json);; All Files (*.*)"
                         )

        print("JSON filename = ", filename)
        print("blah          = ", blah)

        # If a file has been selected

        if filename:

            self.lineEditOptions.setText(filename)

        # self.processJsonFile(filename)


    def processJsonFile(self):

        filenameJSON = open(self.lineEditOptions.text(), 'r')
 
        self.data = json.load(filenameJSON)

        print(self.data)

        self.tab1.processJSON(self.data, "General")
        self.tab2.processJSON(self.data, "Network")


    def connectSignalsToSlots(self):

        # Connect signals to slots.

        # Menu bar items.

        self.quitAction.triggered.connect(self.app.closeAllWindows)
        self.exitAction.triggered.connect(self.app.closeAllWindows)

        # Button items.

        self.buttonOpen.clicked.connect(self.openFileNameDialog)
        self.buttonLoad.clicked.connect(self.processJsonFile)
        self.buttonClear.clicked.connect(self.lineEditURL.clear)
        self.buttonDownload.clicked.connect(self.downloadFile)
        self.buttonExit.clicked.connect(self.app.closeAllWindows)

    
    def downloadFile(self):

        print("Value of --help checkbox = ", self.configControl1_1.isChecked())

        # Invoke yt-dlp


# Function : main
# ===============

app = QApplication(sys.argv)

window = MyMainWindow(app)
window.setupUI()
window.show()
window.applyStylesheet()

sys.exit(app.exec())