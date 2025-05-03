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
                             QFileDialog,  QScrollArea)
from PyQt6.QtGui     import (QKeySequence)

# import yt_dlp
import json

import Tab1, Tab2, Tab3


# Class : MyMainWindow
# ====================
#
# Inherits directly from class QWidget

class MyMainWindow(QMainWindow):

    def __init__(self, app):

        super().__init__()

        self.app = app

        self.createObjects()


    def createObjects(self):

        self.widgetCentral  = QWidget(parent=self)
        self.layoutCentral  = QVBoxLayout()

        # Filenames and the frame that surrounds them.

        self.frameURL        = QFrame()
        self.layoutURL       = QVBoxLayout()

        self.labelURL        = QLabel("URL of filename to download :")
        self.lineEditURL     = QLineEdit("https://www.youtube.com/watch?v=O89_U1gZfYU  https://www.youtube.com/watch?v=slbEMW05Y7A")

        self.labelOptions    = QLabel("Config filename :")
        self.lineEditOptions = QLineEdit("/home/craig/source_code/python/PyQt/yt-dlp-options.json")

        self.frameConfigButtons = QFrame()

        # Tabbed widget and the frame that surrounds it.

        self.frameTabs      = QFrame()
        self.layoutTabs     = QVBoxLayout()
        self.tabWidget      = QTabWidget()
        self.tab1           = Tab1.Tab1()
        self.tab2           = Tab2.Tab2()
        self.tab3           = Tab3.Tab3()
        self.tab4           = QWidget()
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

        # Buttons and the frame that surrounds them.

        self.frameButtons   = QFrame()
        self.layoutButtons  = QHBoxLayout()
        self.buttonOpen     = QPushButton("Select")
        self.buttonLoad     = QPushButton("Load")
        self.buttonSave     = QPushButton("Save")
        self.buttonClear    = QPushButton("Clear URL")
        self.buttonDownload = QPushButton("Download")
        self.buttonExit     = QPushButton("Exit")


    def setup(self):

        self.setWindowTitle("PyQt-Example-1")
        self.setCentralWidget(self.widgetCentral)

        self.widgetCentral.setLayout(self.layoutCentral)

        # Setup the central pane.

        self.layoutCentral.addWidget(self.frameURL)
        self.layoutCentral.addWidget(self.frameTabs)
        self.layoutCentral.addWidget(self.frameButtons)

        # Setup the URL pane and the frame that surrounds it.

        self.frameURL.setLayout(self.layoutURL)
        # self.frameURL.setStyleSheet("border: 1px solid lightgrey;");
        self.layoutURL.addWidget(self.labelURL)
        self.layoutURL.addWidget(self.lineEditURL)
        self.layoutURL.addWidget(self.labelOptions)
        self.layoutURL.addWidget(self.lineEditOptions)
        self.layoutURL.addWidget(self.buttonOpen)
        self.layoutURL.addWidget(self.buttonLoad)

        # Setup the tabbed pane and the frame that surrounds it.

        self.frameTabs.setLayout(self.layoutTabs)
        self.layoutTabs.addWidget(self.tabWidget)

        # frameTab1 = QFrame()

        # Setup each of the 16 tabs.

        self.tab1.setup()
        self.tab2.setup()
        self.tab3.setup()

        # TODO :
        # ======
        #
        # Put the following code into the Tab1, Tab2, etc
        # classes.

        # scrollAreaTab1 = QScrollArea()
        # scrollAreaTab1.setWidget(self.tab1)

        self.tabWidget.addTab(self.tab1,  "1) General                  ")
        self.tabWidget.addTab(self.tab2,  "2) Network                  ")
        self.tabWidget.addTab(self.tab3,  "3) Geo-restriction          ")
        self.tabWidget.addTab(self.tab4,  "4) Video Selection          ")
        self.tabWidget.addTab(self.tab5,  "5) Download                 ")
        self.tabWidget.addTab(self.tab6,  "6) Filesystem               ")
        self.tabWidget.addTab(self.tab8,  "7) Thumbnail                ")
        self.tabWidget.addTab(self.tab9,  "8) Internet Shortcut        ")
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

        self.frameURL.setStyleSheet("border: 1px solid lightgrey;");

        self.frameButtons.setLayout(self.layoutButtons)
        self.layoutButtons.addWidget(self.buttonClear)
        self.layoutButtons.addWidget(self.buttonDownload)
        self.layoutButtons.addWidget(self.buttonExit)
        
        self.buttonOpen.setFixedSize(80, 30)
        self.buttonLoad.setFixedSize(80, 30)
        self.buttonClear.setFixedSize(80, 30)
        self.buttonDownload.setFixedSize(80, 30)
        self.buttonExit.setFixedSize(80, 30)

        self.buttonExit.setToolTip("Exit the program.")
        self.buttonExit.setShortcut(QKeySequence("Ctrl+X"))

        self.connectSignalsToSlots()


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

        self.tab1.processJSON(self.data)
        self.tab2.processJSON(self.data)

        try:
            dataGeoRestriction         = self.data["GeoRestriction"][0]
        except :
            print("Caught an exception : Probably no GeoRestriction element in JSON")

        try:
            dataVideoSelection         = self.data["VideoSelection"][0]
        except :
            print("Caught an exception : Probably no VideoSelection element in JSON")

        try:
            dataDownload               = self.data["Download"][0]
        except :
            print("Caught an exception : Probably no Download element in JSON")

        try:
            dataFilesystem             = self.data["Filesystem"][0]
        except :
            print("Caught an exception : Probably no Filesystem element in JSON")

        try:
            dataThumbnail              = self.data["Thumbnail"][0]
        except :
            print("Caught an exception : Probably no Thumbnail element in JSON")

        try:
            dataInternetShortcut       = self.data["InternetShortcut"][0]
        except :
            print("Caught an exception : Probably no InternetShortcut element in JSON")

        try:
            dataVerbosityAndSimulation = self.data["VerbosityAndSimulation"][0]
        except :
            print("Caught an exception : Probably no VerbosityAndSimulation element in JSON")

        try:
            dataWorkarounds            = self.data["Workarounds"][0]
        except :
            print("Caught an exception : Probably no Workarounds element in JSON")

        try:
            dataVideoFormat            = self.data["VideoFormat"][0]
        except :
            print("Caught an exception : Probably no VideoFormat element in JSON")

        try:
            dataSubtitle               = self.data["Subtitle"][0]
        except :
            print("Caught an exception : Probably no Subtitle element in JSON")

        try:
            dataAuthentication         = self.data["Authentication"][0]
        except :
            print("Caught an exception : Probably no Authentication element in JSON")

        try:
            dataPostProcessing         = self.data["PostProcessing"][0]
        except :
            print("Caught an exception : Probably no PostProcessing element in JSON")

        try:
            dataSponsorBlock           = self.data["SponsorBlock"][0]
        except :
            print("Caught an exception : Probably no SponsorBlock element in JSON")

        try:
            dataExtractor              = self.data["Extractor"][0]
        except :
            print("Caught an exception : Probably no Extractor element in JSON")


    def connectSignalsToSlots(self):

        # Connect signals to slots.

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
window.setup()
window.show()

sys.exit(app.exec())