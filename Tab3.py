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
                             QFileDialog,  QGroupBox)
from PyQt6.QtGui     import QKeySequence


# Class : Tab3
# ========================

class Tab3(QWidget):

    def __init__(self):

        # Invoke the parent class' Constructor.

        super().__init__()

        # Create this class' top level widgets.

        self.layoutSelf = QVBoxLayout()
        self.groupBox   = QGroupBox("Number of options = 2")
        self.layoutGrid = QGridLayout()


    def setupUI(self):

        # Set the layout for this tab and then add child widgets into
        # this layout.

        self.setLayout(self.layoutSelf)

        self.layoutSelf.addWidget(self.groupBox)
        self.layoutSelf.addStretch()

        self.setupGroupBox()


    def setupGroupBox(self) :

        # Set the layout for this widget and then add child widgets into
        # this layout.

        # - Set the layout for this class of widget.

        self.groupBox.setLayout(self.layoutGrid)

        # - Add the child widgets into this layout.

        self.addChildWidgetsToLayout()


    def addChildWidgetsToLayout(self) :

        self.layoutGrid.addWidget(QLabel("--geo-verification-proxy"), 0,  0)
        self.layoutGrid.addWidget(QLabel("  :  "),                    0,  1)
        self.layoutGrid.addWidget(QLineEdit("URL"),                   0,  2)

        self.layoutGrid.addWidget(QLabel("--xff"),                    1,  0)
        self.layoutGrid.addWidget(QLabel("  :  "),                    1,  1)
        self.layoutGrid.addWidget(QLineEdit("VALUE"),                 1,  2)


    def processJSON(self, dataJSON):

        # Retrieve the child element from the JSON.

        try:
            dataGeoRestriction = dataJSON["GeoRestriction"][0]
        except :
            print("Caught an exception : Probably no GeoRestriction element in JSON")

        print(dataGeoRestriction)

        # print("--help = ",    dataGeneral["--help"])
        # print("--version = ", dataGeneral["--version"])

        if dataGeneral["--help"] == "True":
            self.control1.setChecked(True)
        else:
            self.control1.setChecked(False)

        if dataGeneral["--version"] == "True":
            self.control2.setChecked(True)
        else:
            self.control2.setChecked(False)

        if dataGeneral["--update"] == "True":
            self.control3.setChecked(True)
        else:
            self.control3.setChecked(False)

        if dataGeneral["--no-update"] == "True":
            self.control4.setChecked(True)
        else:
            self.control4.setChecked(False)