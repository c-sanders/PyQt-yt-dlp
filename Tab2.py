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


# Class : Tab2
# ========================

class Tab2(QWidget):

    def __init__(self):

        # Invoke the parent class' Constructor.

        super().__init__()


    def setup(self):

        # Tab 2 : Geo-restriction Options

        layoutSelf = QVBoxLayout()
        frameGrid  = QFrame()
        layoutGrid = QGridLayout()

        self.setLayout(layoutSelf)

        layoutSelf.addWidget(frameGrid)
        layoutSelf.addStretch()

        frameGrid.setLayout(layoutGrid)
        
        labelSpacer1  = QLabel("  :  ")
        labelSpacer2  = QLabel("  :  ")
        labelSpacer3  = QLabel("  :  ")
        labelSpacer4  = QLabel("  :  ")
        labelSpacer5  = QLabel("  :  ")
        labelSpacer6  = QLabel("  :  ")
        labelSpacer7  = QLabel("  :  ")
        labelSpacer8  = QLabel("  :  ")

        # TODO
        #
        # Rename these to something more appropriate.
        #
        #   - control

        # CB : --geo-verification-proxy URL
        # CB : --xff VALUE

        label1  = QLabel("--proxy URL")
        label2  = QLabel("--socket-timeout SECONDS")
        label3  = QLabel("--source-address IP")
        label4  = QLabel("--impersonate CLIENT[:OS]")
        label5  = QLabel("--list-impersonate-targets")
        label6  = QLabel("-4, --force-ipv4")
        label7  = QLabel("-6, --force-ipv6")
        label8  = QLabel("--enable-file-urls")

        self.control1  = QLineEdit("URL")
        self.control2  = QLineEdit("SECONDS")
        self.control3  = QLineEdit("IP")
        self.control4  = QLineEdit("CLIENT[:OS]")
        self.control5  = QCheckBox()
        self.control6  = QCheckBox()
        self.control7  = QCheckBox()
        self.control8  = QCheckBox()

        layoutGrid.addWidget(label1,         0,  0)
        layoutGrid.addWidget(labelSpacer1,   0,  1)
        layoutGrid.addWidget(self.control1,  0,  2)

        layoutGrid.addWidget(label2,         1,  0)
        layoutGrid.addWidget(labelSpacer2,   1,  1)
        layoutGrid.addWidget(self.control2,  1,  2)

        layoutGrid.addWidget(label3,         2,  0)
        layoutGrid.addWidget(labelSpacer3,   2,  1)
        layoutGrid.addWidget(self.control3,  2,  2)

        layoutGrid.addWidget(label4,         3,  0)
        layoutGrid.addWidget(labelSpacer4,   3,  1)
        layoutGrid.addWidget(self.control4,  3,  2)

        layoutGrid.addWidget(label5,         4,  0)
        layoutGrid.addWidget(labelSpacer5,   4,  1)
        layoutGrid.addWidget(self.control5,  4,  2)

        layoutGrid.addWidget(label6,         5,  0)
        layoutGrid.addWidget(labelSpacer6,   5,  1)
        layoutGrid.addWidget(self.control6,  5,  2)

        layoutGrid.addWidget(label7,         6,  0)
        layoutGrid.addWidget(labelSpacer7,   6,  1)
        layoutGrid.addWidget(self.control7,  6,  2)

        layoutGrid.addWidget(label8,         7,  0)
        layoutGrid.addWidget(labelSpacer8,   7,  1)
        layoutGrid.addWidget(self.control8,  7,  2)


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