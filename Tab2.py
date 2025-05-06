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
from PyQt6.QtGui     import QKeySequence

from Options         import listOptionsGeneral;


# Class : Tab2
# ========================

# scrollAreaTab1 = QScrollArea()
# scrollAreaTab1.setWidget(self.tab1)

class Tab2(QScrollArea):

    # Get a listing of all the keys in the dictionary.
    #
    # This will be returned as a Python list.

    keys = list(listOptionsGeneral.keys())

    controlDictionary = {}


    def __init__(self):

        # Invoke the parent class' Constructor.

        super().__init__()


    def setup(self):

        rowGridLayout     = 0
        controlsGeneral   = {}


        # Tab 2 : General Options

        frameTopLevel = QFrame()
        layoutSelf    = QVBoxLayout()
        countLabel    = QLabel("Number of options in this group = 28")
        frameGrid     = QFrame()
        layoutGrid    = QGridLayout()


        # Don't set the widget for self here.
        # This is because the widget has not been
        # properly setup as yet.

        frameTopLevel.setLayout(layoutSelf)
        layoutSelf.addWidget(countLabel)
        layoutSelf.addWidget(frameGrid)
        layoutSelf.addStretch()

        frameGrid.setLayout(layoutGrid)

        font = countLabel.font()
        # font.setBold(True)
        font.setUnderline(True)
        # font.setBorder(True)
        countLabel.setFont(font)
        
        # countLabel.setStyleSheet("border: 1px solid lightgrey;");

        print("List of keys = ", self.keys)

        rowGridLayout = 0

        for key in self.keys :

            print("========================================")
            print("Key           = ", key)
            print("========================================")

            # Get the value from the dictionary which is associated
            # with the current key. The value itself will be another
            # dictionary.
            #
            # The value will be of the form;
            #
            #   {"QLineEdit" : "ALIASES OPTIONS"}

            value = listOptionsGeneral[key]
            print("Value         = ", value)

            # Get the key from the sub-dictionary.

            controlType = list(value.keys())[0]
            print("Control type  = ", controlType)
            
            controlValue = value[controlType]
            print("Control value = ", controlValue)

            controlLabel = QLabel(key)

            if controlType.lower() == "QCheckBox".lower():

                print(">>>>>>>>>>")
                print("QCheckBox")
                print("<<<<<<<<<<")

                controlNew = QCheckBox()

                if controlValue == "Checked".lower() :

                    controlNew.setChecked(True)

                else :

                    controlNew.setChecked(False)
                
                value = value["QCheckBox"]
                print("Value = ", value)

            else:

                print(">>>>>>>>>>")
                print("QLineEdit")
                print("<<<<<<<<<<")

                controlNew = QLineEdit(controlValue)

            # Add a new entry into the dictionary.

            self.controlDictionary[key] = controlNew

            # Add the new control into the Grid layout.

            labelSpacer = QLabel("  :  ")

            layoutGrid.addWidget(controlLabel, rowGridLayout, 0)
            layoutGrid.addWidget(labelSpacer,  rowGridLayout, 1)
            layoutGrid.addWidget(controlNew,   rowGridLayout, 2)

            rowGridLayout = rowGridLayout + 1

        print("========================================")
        print("========================================")
        print("Dictionary of controls", self.controlDictionary)
        print("========================================")
        print("========================================")

        self.setWidget(frameTopLevel)


    def processJSON(self, dataJSON, optionsCategory):

        nameMethod = "Tab1::processJSON" 


        print(nameMethod + " : Enter")

        # Retrieve the child element from the JSON.

        try:
            dataOptions = dataJSON[optionsCategory]
        except :
            print("Caught an exception : Probably no " + optionsCategory + " element in JSON")

        print("****************************************")
        print("****************************************")
        print("self.keys = ", self.keys)
        print("****************************************")
        print("****************************************")
        print("dataOptions = ", dataOptions)
        print("****************************************")
        print("****************************************")
        print("self.controlDictionary = ", self.controlDictionary)
        print("****************************************")
        print("****************************************")

        # print("--help = ",    dataGeneral["--help"])
        # print("--version = ", dataGeneral["--version"])

        for key in self.keys :
            
            masterConfig_value    = ""
            controlCurrent_object = ""


            print("Key :")
            print("----*----|----*----|----*----|----*----|")
            print(key)
            print("---------|---------|---------|---------|")

            # Master config : (Stored in the Options.py file)

            #   - masterConfig_key
            #   - masterConfig_value  *
            #   - masterConfig_controlType
            #   - masterConfig_controlValue

            # User config   : (Stored in a JSON file)

            #   - userConfig_key
            #   - userConfig_value

            # GUI control dictionary

            #   - controlCurrent_object  *
            #   - controlCurrent_value

            # Please note that the current key might not being
            # used in the JSON config. Therefore, enclose the
            # following operations in a try-catch block.

            try:

                # Get the value from the JSON config which is
                # associated with the current key.

                # $$$$$ Here $$$$$

                userConfig_value = dataOptions[key]

                print("userConfig_value = ", userConfig_value)

                # Get the value from the master config which
                # is associated with the current key.

                masterConfig_value = listOptionsGeneral[key]
                print("masterConfig_value = ", masterConfig_value)

                # Get the GUI control object which is associated
                # with the current key.

                controlCurrent_object = self.controlDictionary[key]
                print("Current GUI control = ", controlCurrent_object)

                # 

                masterConfig_controlType = list(listOptionsGeneral[key].keys())[0]
                print("Control key       = ", masterConfig_controlType)

                # 

                print("userConfig_value = ", userConfig_value)
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

                if masterConfig_controlType.lower() == "QCheckBox".lower() :

                    print(">>>>> QCheckBox <<<<<")

                    if userConfig_value.lower() == "True".lower() :

                        controlCurrent_object.setChecked(True)

                    else :

                        controlCurrent_object.setChecked(False)

                # print("Control key value = ", value[controlKey])

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            except:

                print("The current key does not appear to be used in the JSON config.")

        print(nameMethod + " : Exit")