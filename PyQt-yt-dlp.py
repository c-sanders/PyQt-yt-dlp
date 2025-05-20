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

useStylesheet             = True
testStylesheetInheritance = True
applyStylesToWidgets      = True


# Class : MyMainWindow
# ====================
#
# Inherits directly from class QWidget

class MyMainWindow(QMainWindow):

    #
    # Define : Public methods
    #

    def __init__(self, app):

        super().__init__()

        self.app = app

        # Create the widgets that are required.

        self.__createWidgets()


    def setupUI(self):

        # Setup the widget which will be used as the main widget
        # by this class.

        self.__setupMainWidget()

        self.__connectSignalsToSlots()


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


    #
    # Define : Private methods
    #

    def __createWidgets(self):

        # The central pane is comprised of the following;
        #
        #   - URL pane      (self.__groupBoxURL)
        #   - Config pane   (self.__groupBoxConfig)
        #   - Buttons pane  (self.__frameButtons)

        self.__widgetCentral  = QWidget(parent=self)
        self.__layoutCentral  = QVBoxLayout()

        self.__createUrlPaneWidgets()
        self.__createConfigPaneWidgets()
        self.__createButtonPaneWidgets()


    def __createUrlPaneWidgets(self) :

        # The URL pane.

        # Top-level container and layout.

        self.__groupBoxURL      = QGroupBox("URL of filename to download :")
        self.__layoutURL        = QVBoxLayout()

        # Child widgets.

        self.__lineEditURL      = QLineEdit("https://www.youtube.com/watch?v=O89_U1gZfYU")
        # self.lineEditURL      = QLineEdit("https://www.youtube.com/watch?v=slbEMW05Y7A")

        self.__frameButtonsURL  = QFrame()
        self.__layoutButtonsURL = QHBoxLayout()

        self.__buttonClear      = QPushButton("Clear URL")
        self.__buttonHistory    = QPushButton("History")


    def __createConfigPaneWidgets(self) :

        # The config pane.

        # Top-level container and layout.

        self.__groupBoxConfig      = QGroupBox("yt-dlp config :")
        self.__layoutConfig        = QVBoxLayout()

        # Child widgets.

        # Label and line edit.

        self.__labelOptions        = QLabel("Config filename :")
        self.__lineEditOptions     = QLineEdit("/home/craig/source_code/python/PyQt/yt-dlp-options.json")

        # Buttons and their container.

        self.__frameButtonsConfig  = QFrame()
        self.__layoutButtonsConfig = QHBoxLayout()

        self.__buttonOpen          = QPushButton("Select")
        self.__buttonLoad          = QPushButton("Load Config")
        self.__buttonSave          = QPushButton("Save Config")

        self.__createTabbedAndTabWidgets()


    def __createButtonPaneWidgets(self) :

        # The config pane.

        # Top-level container and layout.

        self.__frameButtons   = QFrame()
        self.__layoutButtons  = QHBoxLayout()

        # Child widgets.

        self.__buttonDownload = QPushButton("Download")
        self.__buttonExit     = QPushButton("Exit")


    def __createTabbedAndTabWidgets(self) :

        # Tabbed widget and the 16 tabs which it contains.

        self.__tabWidget      = QTabWidget()

        self.__tab1           = Tab1.Tab1()
        self.__tab2           = Tab2.Tab2()
        self.__tab3           = Tab3.Tab3()
        self.__tab4           = Tab4.Tab4()
        self.__tab5           = QWidget()
        self.__tab6           = QWidget()
        self.__tab7           = QWidget()
        self.__tab8           = QWidget()
        self.__tab9           = QWidget()
        self.__tab10          = QWidget()
        self.__tab11          = QWidget()
        self.__tab12          = QWidget()
        self.__tab13          = QWidget()
        self.__tab14          = QWidget()
        self.__tab15          = QWidget()
        self.__tab16          = QWidget()


    def __setupMainWidget(self) :

        self.setWindowTitle("GUI frontend to yt-dlp")

        self.setCentralWidget(self.__widgetCentral)
        self.__widgetCentral.setLayout(self.__layoutCentral)

        # Setup the menu bar and the central pane.

        self.__createMenubar()
        self.__setupCentralPane()

        if applyStylesToWidgets :

            self.__applyStylesToWidgets()


    def __setupCentralPane(self) :

        self.__layoutCentral.addWidget(self.__groupBoxURL)
        self.__layoutCentral.addWidget(self.__groupBoxConfig)
        # self.__layoutCentral.addWidget(self.__frameTabs)
        self.__layoutCentral.addWidget(self.__frameButtons)

        self.__setupUrlPane()
        self.__setupConfigPane()
        #self.setup


    def __setupUrlPane(self) :

        # Setup the URL pane and the group box that contains it.

        # Setup the child pane that contains this pane's buttons.

        self.__setupUrlButtonFrame()

        # Set the layout for this pane and then add the widgets to it.

        self.__groupBoxURL.setLayout(self.__layoutURL)
        self.__layoutURL.addWidget(self.__lineEditURL)
        self.__layoutURL.addWidget(self.__frameButtonsURL)


    def __setupUrlButtonFrame(self) :

        # Setup the horizontal button pane for the URL pane.

        self.__frameButtonsURL.setLayout(self.__layoutButtonsURL)
        self.__layoutButtonsURL.addWidget(self.__buttonClear)
        self.__layoutButtonsURL.addWidget(self.__buttonHistory)

        # Apply styles to those widgets that require it.

        self.__buttonClear.setObjectName("buttonClear")
        # self.buttonClear.setStyleSheet("""
        #                                border: 1px solid yellow;
        #                                border-color : purple;
        #                                color : green;
        #                                """)

        # The following works.

        # self.buttonHistory.setStyleSheet("color : deeppink;");


    def __setupConfigPane(self) :

        # Setup the Config pane and the frame that surrounds it.

        self.__groupBoxConfig.setLayout(self.__layoutConfig)
        self.__layoutConfig.addWidget(self.__labelOptions)
        self.__layoutConfig.addWidget(self.__lineEditOptions)
        self.__layoutConfig.addWidget(self.__frameButtonsConfig)
        self.__layoutConfig.addWidget(self.__tabWidget)

        # Setup the horizontal button pane for the yt-dlp config.

        self.__frameButtonsConfig.setLayout(self.__layoutButtonsConfig)
        self.__layoutButtonsConfig.addWidget(self.__buttonOpen)
        self.__layoutButtonsConfig.addWidget(self.__buttonLoad)
        self.__layoutButtonsConfig.addWidget(self.__buttonSave)

        # self.frameConfig.setStyleSheet(style)

        # self.frameURL.setStyleSheet("QFrame {border : 1px solid lightgrey;}")
        # self.frameConfig.setStyleSheet("QFrame {border : 1px solid pink;}")
        # self.labelOptions.setStyleSheet("QFrame {border : none;}")
        self.__frameButtonsConfig.setStyleSheet("QFrame {border : 0px solid grey;}")

        self.__lineEditURL.setStyleSheet("QLineEdit {border : 1px solid;}")

        self.__groupBoxConfig.setObjectName("groupBoxConfig")

        # Setup the tabbed pane and the frame that surrounds it.

        # self.frameTabs.setLayout(self.layoutTabs)
        # self.layoutTabs.addWidget(self.tabWidget)

        # frameTab1 = QFrame()

        self.__setupTabbedWidget()

        # layoutTab1 = QVBoxLayout()

        # frameTab1.setLayout(layoutTab1)
        # layoutTab1.addWidget(self.tab1)

        # Setup the buttons and the frame that surrounds them.

        # self.frameURL.setStyleSheet("border: 1px solid lightgrey;");

        self.__frameButtons.setLayout(self.__layoutButtons)
        self.__layoutButtons.addWidget(self.__buttonDownload)
        self.__layoutButtons.addWidget(self.__buttonExit)

        self.__buttonHistory.setFixedSize(100, 30)
        self.__buttonOpen.setFixedSize(100, 30)
        self.__buttonLoad.setFixedSize(100, 30)
        self.__buttonSave.setFixedSize(100, 30)
        self.__buttonClear.setFixedSize(100, 30)
        self.__buttonDownload.setFixedSize(100, 30)
        self.__buttonExit.setFixedSize(100, 30)

        self.__buttonExit.setToolTip("Exit the program.")
        self.__buttonExit.setShortcut(QKeySequence("Ctrl+X"))


    def __setupTabbedWidget(self) :

        self.__setupAllTabs()

        self.__tabWidget.addTab(self.__tab1, "1) General                  ")
        self.__tabWidget.addTab(self.__tab2, "2) Network                  ")
        self.__tabWidget.addTab(self.__tab3, "3) Geo-restriction          ")
        self.__tabWidget.addTab(self.__tab4, "4) Video Selection          ")
        self.__tabWidget.addTab(self.__tab5, "5) Download                 ")
        self.__tabWidget.addTab(self.__tab6, "6) Filesystem               ")
        self.__tabWidget.addTab(self.__tab8, "7) Thumbnail                ")
        self.__tabWidget.addTab(self.__tab9, "8) Internet Shortcut        ")
        self.__tabWidget.addTab(self.__tab10, "9) Verbosity and Simulation")
        self.__tabWidget.addTab(self.__tab11, "10) Workarounds            ")
        self.__tabWidget.addTab(self.__tab11, "11) Video Format            ")
        self.__tabWidget.addTab(self.__tab12, "12) Subtitle                ")
        self.__tabWidget.addTab(self.__tab13, "13) Authentication          ")
        self.__tabWidget.addTab(self.__tab14, "14) Post-Processing         ")
        self.__tabWidget.addTab(self.__tab15, "15) SponsorBlock            ")
        self.__tabWidget.addTab(self.__tab16, "16) Extractor               ")


    def __setupAllTabs(self) :

        # Setup each of the 16 tabs.

        self.__tab1.setupUI()
        self.__tab2.setupUI()
        self.__tab3.setupUI()
        self.__tab4.setupUI()


    def __applyStylesToWidgets(self) :

        # Apply styles to those widgets that require it.
        #
        # Child widgets will inherit the style from their parent widget.
        # This can be observed from the following command.

        # self.lineEditURL.setStyleSheet("border: 1px solid deeppink;");

        # From what I can gather, Qt objects by default, aren't
        # assigned names when they are created.

        print("Name of object = " + str(self.__frameButtonsURL.objectName()))
        self.__frameButtonsURL.setObjectName("MyMainWindow::frameButtonsURL")
        print("Name of object = " + str(self.__frameButtonsURL.objectName()))

        self.__frameButtonsURL.setStyleSheet("border: 1px solid deeppink;");


    def __createMenubar(self) :

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


    def __openFileNameDialog(self) :

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


    def __processJsonFile(self) :

        filenameJSON = open(self.lineEditOptions.text(), 'r')
 
        self.data = json.load(filenameJSON)

        print(self.data)

        self.__tab1.processJsonToDictionary(self.data, "General")
        self.__tab2.processJSON(self.data, "Network")


    def __saveConfigToFile(self) :

        nameMethod = "MyMainWindow::__saveConfigToFile"


        print(nameMethod + " : Enter")

        # Get all of the config settings and write them into a dictionary.
        #
        # Convert the dictionary into JSON.
        #
        # Save the JSON

        self.__tab1.processDictionaryToJson()

        print(nameMethod + " : Exit")


    def __connectSignalsToSlots(self):

        # Connect signals to slots.

        # Menu bar items.

        self.quitAction.triggered.connect(self.app.closeAllWindows)
        self.exitAction.triggered.connect(self.app.closeAllWindows)

        # Button items.

        self.__buttonOpen.clicked.connect(self.__openFileNameDialog)
        self.__buttonLoad.clicked.connect(self.__processJsonFile)
        self.__buttonSave.clicked.connect(self.__saveConfigToFile)
        self.__buttonClear.clicked.connect(self.__lineEditURL.clear)
        self.__buttonDownload.clicked.connect(self.__downloadFile)
        self.__buttonExit.clicked.connect(self.app.closeAllWindows)

    
    def __downloadFile(self):

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