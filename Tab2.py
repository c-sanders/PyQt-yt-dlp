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
                             QFileDialog,  QScrollArea, QGroupBox)
from PyQt6.QtGui     import  QKeySequence

from Options         import  listOptionsNetwork;


# Class : Tab2
# ========================

class Tab2(QScrollArea):

    useOldLayoutCode = False

    numberTab = 2
    debugTab  = True

    # Get a listing of all the keys in the dictionary.
    #
    # This will be returned as a Python list.

    keys = list(listOptionsNetwork.keys())

    controlDictionary = {}


    def __init__(self):

        # Invoke the parent class' Constructor.

        super().__init__()

        # Create this class's top level widget and layout.

        self.groupBox   = QGroupBox("Number of options = 28")
        self.layoutGrid = QGridLayout()

        # Create all the GUI controls and then populate the Control dictionary
        # with them.

        self.populateGuiControlsDictionary()


    def setupUI(self):

        # Additional steps required by this tab.

        # Set the layout for this tab and then add child widgets into
        # this layout.

        # self.setLayout(self.layoutSelf)

        # self.groupBox.setLayout(self.layoutSelf)

        # self.layoutSelf.addWidget(self.groupBox)
        # self.layoutSelf.addStretch()

        self.setupGroupBox()


    def populateGuiControlsDictionary(self) :

        nameMethod = "Tab2::populateGuiControlsDictionary"


        numKeys = len(self.keys)

        print("::::::::::::::::::::::::::::::::::::::::")
        print(nameMethod + " : Enter")
        print("::::::::::::::::::::::::::::::::::::::::")
        print("Number of keys in list = ", numKeys)
        print("::::::::::::::::::::::::::::::::::::::::")
        print("::::::::::::::::::::::::::::::::::::::::")
        print("Keys = ", self.keys)
        print("::::::::::::::::::::::::::::::::::::::::")
        print("::::::::::::::::::::::::::::::::::::::::")

        for key in self.keys :

            # For the current key, create both a label and a
            # GUI control for it.

            controlLabel, control = self.createGuiLabelAndControlFromKey(key)

            # Add the label and GUI control into the dictionary of GUI
            # controls.

            self.controlDictionary[key] = control

            numGuiControls = len(self.controlDictionary)

            print("========================================")
            print("Tab num = ", str(self.numberTab))
            print("Key             = " + key)
            print("========================================")
            print("Control label = " + str(controlLabel))
            print("Control       = " + str(control))
            print("-----")
            print("Text in Control label = " + controlLabel.text())
            print("========================================")
            print("Num elements in GUI control dictionary = " + str(len(self.controlDictionary)))
            print("========================================")

            if self.debugTab :

                print("")
                print("Press Enter to continue... ", end="")
                input()

        # End of for loop.

        print("========================================")
        print("========================================")
        print("Dictionary of controls")
        print("========================================")
        print("========================================")

        for key in self.keys :

            control = self.controlDictionary[key]

            print(str(control))

        # End of for loop.

        # print("")
        # print("Press Enter to continue... ", end="")
        # input()

        print(nameMethod + " : Exit")


    def setupGroupBox(self) :

        # Add the child widgets into this layout.

        self.addChildWidgetsToLayout()

        # Set the layout for widget.

        if self.useOldLayoutCode :

            self.groupBox.setLayout(self.layoutGrid)

        else :

            # Create a QVBoxLayout so that we can push all of the controls up.

            vboxLayout = QVBoxLayout()

            frameGrid  = QFrame()

            self.groupBox.setLayout(vboxLayout)

            vboxLayout.addWidget(frameGrid)
            vboxLayout.addStretch()

            frameGrid.setLayout(self.layoutGrid)

        # Set self.groupBox to be the main widget.

        self.setWidget(self.groupBox)
        self.setWidgetResizable(True)


    def addChildWidgetsToLayout(self) :

        testMethod = False


        if testMethod :

            self.layoutGrid.addWidget(QLabel("--geo-verification-proxy"), 0,  0)
            self.layoutGrid.addWidget(QLabel("  :  "),                    0,  1)
            self.layoutGrid.addWidget(QLineEdit("URL"),                   0,  2)

            self.layoutGrid.addWidget(QLabel("--farts"),                  1,  0)
            self.layoutGrid.addWidget(QLabel("  :  "),                    1,  1)
            self.layoutGrid.addWidget(QLineEdit("SMELLY"),                1,  2)

        # Iterate through the GUI control dictionary and add each of the GUI
        # controls to the grid layout.

        rowGridLayout = 0

        for key in self.controlDictionary :

            control = self.controlDictionary[key]

            print("========================================")
            print("Key             = " + key)
            print("Row grid layout = " + str(rowGridLayout))
            print("========================================")
            # print("Control label = " + controlLabel.text())
            print("Control       = " + str(control))
            print("========================================")

            # Add the new control into the Grid layout.

            self.layoutGrid.addWidget(QLabel(key),     rowGridLayout, 0)
            self.layoutGrid.addWidget(QLabel("  :  "), rowGridLayout, 1)
            self.layoutGrid.addWidget(control,         rowGridLayout, 2)

            rowGridLayout = rowGridLayout + 1

        # End of for loop.

        print("========================================")
        print("========================================")
        print("Dictionary of controls", self.controlDictionary)
        print("========================================")
        print("========================================")

        # self.setWidget(self.groupBox)


    def getNextControlLabel(self, key) :

        # Get the value from the dictionary which is associated
        # with the current key. The value itself will be another
        # dictionary.
        #
        # The value will be of the form;
        #
        #   {"QLineEdit" : "ALIASES OPTIONS"}

        value = listOptionsNetwork[key]
        print("Value         = ", value)

        # Get the key from the sub-dictionary.

        controlType = list(value.keys())[0]
        print("Control type  = ", controlType)

        controlValue = value[controlType]
        print("Control value = ", controlValue)

        controlLabel = QLabel(key)


        return controlLabel


    def createGuiLabelAndControlFromKey(self, key) :

        verbose = False


        # Get the value from the dictionary which is associated
        # with the current key.
        #
        # The dictionary is named;
        #
        #   > listOptionsNetwork
        #
        # The value which is returned from the dictionary, will
        # itself be another dictionary and will be of one of the
        # following forms;
        #
        #   {"QCheckBox" : "Checked"}
        #   {"QLineEdit" : "ALIASES OPTIONS"}

        controlTypeAndValue = listOptionsNetwork[key]

        if verbose :
            print("controlTypeAndValue = ", controlTypeAndValue)

        # Get the control type.

        listKeys = list(controlTypeAndValue.keys())

        controlType = listKeys[0]

        if verbose :
            print("Control type  = ", controlType)

        controlValue = controlTypeAndValue[controlType]

        if verbose :
            print("Control value = ", controlValue)

        # Create the control label.

        controlLabel = QLabel(key)

        # Ascertain the control type and then create one.

        if controlType.lower() == "QCheckBox".lower():

            if verbose :
                print(">>>>>>>>>>")
                print("QCheckBox")
                print("<<<<<<<<<<")

            control = QCheckBox()

            if controlValue == "Checked".lower() :

                control.setChecked(True)

            else :

                control.setChecked(False)

            value = controlTypeAndValue["QCheckBox"]
            if verbose :
                print("Value = ", value)

        else:

            if verbose :
                print(">>>>>>>>>>")
                print("QLineEdit")
                print("<<<<<<<<<<")

            control = QLineEdit(controlValue)


        return (controlLabel, control)


    def processJSON(self, dataJSON, optionsCategory):

        nameMethod = "Tab2::processJSON"


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