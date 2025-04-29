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
                             QFileDialog)
from PyQt6.QtGui     import QKeySequence


# Class : Tab3
# ========================

class Tab3(QWidget):

    def __init__(self):

        # Invoke the parent class' Constructor.

        super().__init__()


    def setup(self):

        # Tab 3 : Geo-restriction Options

        layoutSelf = QVBoxLayout()
        frameGrid  = QFrame()
        layoutGrid = QGridLayout()

        self.setLayout(layoutSelf)

        layoutSelf.addWidget(frameGrid)
        layoutSelf.addStretch()

        frameGrid.setLayout(layoutGrid)
        
        labelSpacer1  = QLabel("  :  ")
        labelSpacer2  = QLabel("  :  ")

        # TODO
        #
        # Rename these to something more appropriate.
        #
        #   - control

        # CB : --geo-verification-proxy URL
        # CB : --xff VALUE

        label1  = QLabel("--geo-verification-proxy")
        label2  = QLabel("--xff")

        self.control1  = QLineEdit("URL")
        self.control2  = QLineEdit("VALUE")

        layoutGrid.addWidget(label1,         0,  0)
        layoutGrid.addWidget(labelSpacer1,   0,  1)
        layoutGrid.addWidget(self.control1,  0,  2)

        layoutGrid.addWidget(label2,         1,  0)
        layoutGrid.addWidget(labelSpacer2,   1,  1)
        layoutGrid.addWidget(self.control2,  1,  2)


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