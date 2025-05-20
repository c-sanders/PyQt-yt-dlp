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

import json

from Options         import  listOptionsGeneral as listOptions;


# * Dictionaries
# ==============
#
# The class which is defined in this file, i.e. Tab1, deals with two
# distinct types of dictionaries.
#
#   Type 1) : Dictionary of GUI widget specifications.
#   --------------------------------------------------
#
#   --> dictionaryGuiSpecifications
#
#   This type of dictionary contains specifications which are used for
#   the creation of GUI widgets.
#
#   For each one of the yt-dlp utility's command line options, this
#   dictionary specifies what type of GUI control should be associated
#   with it, along with a default value for that GUI control. In case
#   it is not obvious, this type of dictionary uses the yt-dlp utility's
#   command line options as the key to the dictionary.
#
#   This type of dictionary is important, as it tells this program what
#   type of GUI control it should display on the screen in order to
#   represent each of the yt-dlp command line options. As a result, every
#   entry in the dictionaries defines an option-control-value triple of
#   values.
#
#   This program makes use of 16 instances of this type of
#   dictionary - one for each of the categories of yt-dlp command
#   line options. These 16 dictionaries are defined in the file;
#
#     > Options.py
#
#   Every one of these option-control-value triple of values has the
#   following form;
#
#     "-h, --help" : {"QCheckBox" : "Checked"}
#
#   In this case;
#
#     - the yt-dlp command line option       = "-h, --help"
#     - the type of GUI control to use       = QCheckBox
#     - the default value of the GUI control = Checked
#
#     > The control specifies the type of GUI control which should be
#       used, i.e. a check box (QCheckBox) or a line edit (QLineEdit).
#
#      The dictionary that this tab needs to use is named;
#
#        > listOptionsGeneral
#
#      but is imported by this file using the alias;
#
#        > listOptions
#
#      The value which is returned from the dictionary, will
#      itself be another dictionary and will be of one of the
#      following forms;
#
#   {"QCheckBox" : "Checked"}
#   {"QLineEdit" : "ALIASES OPTIONS"}
#
#
#   Type 2) Dictionary of GUI widgets.
#   ----------------------------------
#
#   --> dictionaryGuiWidgets
#
#   This type of dictionary contains the GUI widgets that have been
#   created in response to the specifications.


# ========================
# Class : Tab1
# ========================
#
# Parent class : QScrollArea
#
# ------------------------


class Tab1(QScrollArea):

    debug_populateDictionaryGuiWidgets = False
    displayNumberOptions               = False
    useOldLayoutCode                   = False

    mainWidgetTitle      = "Number of options = 28"

    # Get a listing of all the keys in the GUI widget specifications
    # dictionary.
    #
    # This will be returned as a Python list.

    keys = list(listOptions.keys())

    dictionaryGuiWidgets = {}


    def __init__(self):

        # Invoke the parent class' Constructor.

        super().__init__()

        # Create this class's top level widget and layout.

        self.createMainWidgetAndLayout()

        # Create all the GUI labels and controls. Once this is done,
        # populate the Control dictionary with them.

        # self.populateGuiLabelAndControlDictionary()
        self.populateDictionaryGuiWidgets()


    def setupUI(self):

        # Setup the widget which will be used as the main widget
        # by this class.

        self.setupMainWidget()

        # Set the main widget for this class.

        self.setWidget(self.mainWidget)
        self.setWidgetResizable(True)


    def createMainWidgetAndLayout(self) :

        if self.displayNumberOptions :

            self.mainWidget = QGroupBox(self.mainWidgetTitle)

        else :

            self.mainWidget = QGroupBox()

        self.layoutGrid = QGridLayout()


    def populateDictionaryGuiWidgets(self) :

        nameMethod = "Tab1::populateDictionaryGuiWidgets"


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

            # For the current key, create a label and a
            # GUI control for it.

            # controlLabel = self.getNextControlLabel(key)
            # control      = self.createGuiControlFromKey(key, False)

            controlLabel, control = self.createGuiLabelAndControlFromKey(key)

            # Add this control into the dictionary of GUI controls.

            self.dictionaryGuiWidgets[key] = control

            numGuiControls = len(self.dictionaryGuiWidgets)

            print("========================================")
            print("Key             = " + key)
            print("========================================")
            print("Control label = " + str(controlLabel))
            print("Control       = " + str(control))
            print("-----")
            print("Text in Control label = " + controlLabel.text())
            print("========================================")
            print("Num elements in GUI control dictionary = " + str(len(self.dictionaryGuiWidgets)))
            print("========================================")

            if self.debug_populateDictionaryGuiWidgets :

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

            control = self.dictionaryGuiWidgets[key]

            print(str(control))

        # End of for loop.

        if self.debug_populateDictionaryGuiWidgets:

            print("")
            print("Press Enter to continue... ", end="")
            input()

        print(nameMethod + " : Exit")


    def setupMainWidget(self) :

        # Set the layout for widget.
        #
        # We use a QVBoxLayout so that all of the child widgets get pushed
        # to the top. We do this in case there aren't enough child widgets
        # to fill out the layout properly.

        self.layoutMainWidget = QVBoxLayout()

        self.createFrameGridAndLayout()

        # Add the child widgets into this layout.

        self.addChildWidgetsToLayout()


    def createFrameGridAndLayout(self) :

        frameGrid  = QFrame()
        frameGrid.setObjectName("Tab1_frameGrid")
        frameGrid.setStyleSheet("""
                                QFrame { border : none; margin-top: 0px; } 
                                QLabel { border : none; }")  
                                /* QLineEdit { border : 1px; }" */
                                """)

        self.mainWidget.setStyleSheet("""
                                      QGroupBox
                                      {
                                        border : none;
                                        margin-top: 0px;
                                      }
                                      QLineEdit
                                      {
                                        border : 1px;
                                        /* background-color : orange; */
                                      }
                                      """)

        self.mainWidget.setLayout(self.layoutMainWidget)

        self.layoutMainWidget.addWidget(frameGrid)
        self.layoutMainWidget.addStretch()

        frameGrid.setLayout(self.layoutGrid)


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

        for key in self.dictionaryGuiWidgets :

            control = self.dictionaryGuiWidgets[key]

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
        print("Dictionary of controls", self.dictionaryGuiWidgets)
        print("========================================")
        print("========================================")

        # self.setWidget(self.mainWidget)


    def getNextControlLabel(self, key) :

        # Get the value from the dictionary which is associated
        # with the current key. The value itself will be another
        # dictionary.
        #
        # The value will be of the form;
        #
        #   {"QLineEdit" : "ALIASES OPTIONS"}

        value = listOptions[key]
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


        controlTypeAndValue = listOptions[key]

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
            control.setStyleSheet("""
                                  QLineEdit 
                                  {
                                    /* background-color : green; */
                                    border           : 1px solid; 
                                  }
                                  """)

        self.mainWidget.setStyleSheet("""
                                      QGroupBox
                                      {
                                        border : none; margin-top: 0px;
                                      }
                                      QLineEdit
                                      {
                                        border : 1px;
                                        /* background-color : orange; */ 
                                      }
                                      """)


        return (controlLabel, control)


    def processJsonToDictionary(self, dataJSON, optionsCategory):
    # def getDictionaryFromJson

        nameMethod = "Tab1::processJsonToDictionary"


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

                masterConfig_value = listOptions[key]
                print("masterConfig_value = ", masterConfig_value)

                # Get the GUI control object which is associated
                # with the current key.

                controlCurrent_object = self.controlDictionary[key]
                print("Current GUI control = ", controlCurrent_object)

                # 

                masterConfig_controlType = list(listOptions[key].keys())[0]
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


    def processDictionaryToJson(self) :

        nameMethod = "Tab1::processDictionaryToJson"


        print(nameMethod + " : Enter")

        tempDict = {}

        for key in self.dictionaryGuiWidgets :

            value = self.dictionaryGuiWidgets[key]

            # Get the label and GUI value associated with this key.

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Key   = " + key)

            tempSubDict = {}

            if value.inherits("QLineEdit") :

                print("Widget is of type QLineEdit")
                print("Value = ", value.text())

                tempSubDict["QLineEdit"] = value.text()
                tempDict[key] = tempSubDict

            else :

                print("Widget is of type QCheckBox")

                value = value.isChecked()

                if value :

                    print("Value = Checked")

                    tempSubDict["QCheckBox"] = "Checked"

                else :

                    print("Value = Unchecked")

                    tempSubDict["QCheckBox"] = "Unchecked"

                tempDict[key] = tempSubDict

            print(json.dumps(tempDict, indent = 0))  # Pretty print JSON
            # print(json.dumps(d, sort_keys=True))  # Sorted keys
            # print(json.dumps(d, ensure_ascii=False))  # Non-ASCII encoding
            # print(json.dumps([{k: d[k]} for k in d]))  # Convert to JSON array format

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print(nameMethod + " : Exit")