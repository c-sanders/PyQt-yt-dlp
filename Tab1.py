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


# Class : Tab1
# ========================

# scrollAreaTab1 = QScrollArea()
# scrollAreaTab1.setWidget(self.tab1)

class Tab1(QScrollArea):

    def __init__(self):

        # Invoke the parent class' Constructor.

        super().__init__()


    def setup(self):

        elementIndex    = 0
        controlsGeneral = {}


        # Tab 1 : General Options

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

        labelSpacer1  = QLabel("  :  ")
        labelSpacer2  = QLabel("  :  ")
        labelSpacer3  = QLabel("  :  ")
        labelSpacer4  = QLabel("  :  ")
        labelSpacer5  = QLabel("  :  ")
        labelSpacer6  = QLabel("  :  ")
        labelSpacer7  = QLabel("  :  ")
        labelSpacer8  = QLabel("  :  ")
        labelSpacer9  = QLabel("  :  ")
        labelSpacer10 = QLabel("  :  ")
        labelSpacer11 = QLabel("  :  ")
        labelSpacer12 = QLabel("  :  ")
        labelSpacer13 = QLabel("  :  ")
        labelSpacer14 = QLabel("  :  ")
        labelSpacer15 = QLabel("  :  ")
        labelSpacer16 = QLabel("  :  ")
        labelSpacer17 = QLabel("  :  ")
        labelSpacer18 = QLabel("  :  ")
        labelSpacer19 = QLabel("  :  ")
        labelSpacer20 = QLabel("  :  ")
        labelSpacer21 = QLabel("  :  ")
        labelSpacer22 = QLabel("  :  ")
        labelSpacer23 = QLabel("  :  ")
        labelSpacer24 = QLabel("  :  ")
        labelSpacer25 = QLabel("  :  ")
        labelSpacer26 = QLabel("  :  ")
        labelSpacer27 = QLabel("  :  ")
        labelSpacer28 = QLabel("  :  ")


        # List/array of dictionaries.
        #
        # Each element can be accessed by an integer index value.

        optionsList  =  {"-h, --help"              : {"QCheckBox" : "Unchecked"},
                        "--version"                : {"QCheckBox" : "Unchecked"},
                        "-U, --update"             : {"QCheckBox" : "Unchecked"},
                        "--no-update"              : {"QCheckBox" : "Unchecked"},
                        "--update-to"              : {"QLineEdit" : "[CHANNEL]@[TAG]"},
                        "-i, --ignore-errors"      : {"QCheckBox" : "Unchecked"},
                        "--no-abort-on-error"      : {"QCheckBox" : "Unchecked"},
                        "--abort-on-error"         : {"QCheckBox" : "Unchecked"},
                        "--dump-user-agent"        : {"QCheckBox" : "Unchecked"},
                        "--list-extractors"        : {"QCheckBox" : "Unchecked"},

                        "--extractor-descriptions" : {"QCheckBox" : "Unchecked"},
                        "--use-extractors"         : {"QLineEdit" : "NAMES"},
                        "--default-search"         : {"QLineEdit" : "PREFIX"},
                        "--ignore-config"          : {"QCheckBox" : "Unchecked"},
                        "--no-config-locations"    : {"QCheckBox" : "Unchecked"},
                        "--config-locations"       : {"QLineEdit" : "PATH"},
                        "--plugin-dirs"            : {"QLineEdit" : "PATH"},
                        "--flat-playlist"          : {"QCheckBox" : "Unchecked"},
                        "--no-flat-playlist"       : {"QCheckBox" : "Unchecked"},
                        "--live-from-start"        : {"QCheckBox" : "Unchecked"},

                        "--no-live-from-start"     : {"QCheckBox" : "Unchecked"},
                        "--wait-for-video"         : {"QLineEdit" : "MIN[-MAX]"},
                        "--no-wait-for-video"      : {"QCheckBox" : "Unchecked"},
                        "--mark-watched"           : {"QCheckBox" : "Unchecked"},
                        "--no-mark-watched"        : {"QCheckBox" : "Unchecked"},
                        "--color"                  : {"QLineEdit" : "[STREAM:]POLICY"},
                        "--compat-options"         : {"QLineEdit" : "OPTS"},
                        "--alias"                  : {"QLineEdit" : "ALIASES OPTIONS"}}

        # self.control11 = QCheckBox()
        # self.control12 = QLineEdit("NAMES")
        # self.control13 = QLineEdit("PREFIX")
        # self.control14 = QCheckBox()
        # self.control15 = QCheckBox()
        # self.control16 = QLineEdit("PATH")
        # self.control17 = QLineEdit("PATH")
        # self.control18 = QCheckBox()
        # self.control19 = QCheckBox()
        # self.control20 = QCheckBox()

        # CB : --no-live-from-start            
        # LE : --wait-for-video MIN[-MAX]      
        # CB : --no-wait-for-video             
        # CB : --mark-watched                  
        # CB : --no-mark-watched               
        # LE : --color [STREAM:]POLICY
        # LE : --compat-options OPTS           
        # LE : --alias ALIASES OPTIONS

        # Get a list of all the keys in the dictionary.

        keys = list(optionsList.keys())
        print("keys = ", keys)

        for key in keys :

            print("========================================")
            print("Key = ", key)
            print("========================================")

            # entry = optionsList[indexList]
            # print("Entry = ", entry)

            # element will be of the form;
            #
            #   {"-h, --help" : {"QCheckBox" : "Unchecked"}}
            
            # key = list(element.keys())[0]

            # Get the value from the dictionary which is associated
            # with the current key.

            value = optionsList[key]
            print("Value = ", value)

            # Get a list of all the keys in the dictionary.

            controlType = list(value.keys())[0]
            print("Control type = ", controlType)
            
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
                
                controlsGeneral[key] = controlNew

                value = value["QCheckBox"]
                print("Value = ", value)

            else:

                print(">>>>>>>>>>")
                print("QLineEdit")
                print("<<<<<<<<<<")

                controlNew = QLineEdit()
                controlsGeneral[key] = controlNew

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Array of controls = ", controlsGeneral)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

        for element in controlsGeneral:

            print(element)

            key = element.keys()

            print("Keys = ", keys)

            # Create a QLabel from the element's key.

            controlLabel = QLabel(element)

            # Get the control associated with the element's key.

            layoutGrid.addWidget(controlLabel,  elementIndex, 0)
            layoutGrid.addWidget(labelSpacer1,  elementIndex, 1)
            layoutGrid.addWidget(self.control1, elementIndex, 2)

            elementIndex = elementIndex + 1

        # TODO
        #
        # Rename these to something more appropriate.
        #
        #   - control

        # CB : -h, --help                      
        # CB : --version                       
        # CB : -U, --update                    
        # CB : --no-update                     
        # LE : --update-to [CHANNEL]@[TAG]     
        # CB : -i, --ignore-errors             
        # CB : --no-abort-on-error             
        # CB : --abort-on-error                
        # CB : --dump-user-agent               
        # CB : --list-extractors               

        label1  = QLabel("-h, --help")
        label2  = QLabel("--version")
        label3  = QLabel("-U, --update")
        label4  = QLabel("--no-update")
        label5  = QLabel("--update-to")
        label6  = QLabel("-i, --ignore-errors")
        label7  = QLabel("--no-abort-on-error")
        label8  = QLabel("--abort-on-error")
        label9  = QLabel("--dump-user-agent")
        label10 = QLabel("--list-extractors")

        self.control1  = QCheckBox()
        self.control2  = QCheckBox()
        self.control3  = QCheckBox()
        self.control4  = QCheckBox()
        self.control5  = QLineEdit("[CHANNEL]@[TAG]")
        self.control6  = QCheckBox()
        self.control7  = QCheckBox()
        self.control8  = QCheckBox()
        self.control9  = QCheckBox()
        self.control10 = QCheckBox()
     
        # CB : --extractor-descriptions        
        # LE : --use-extractors NAMES          
        # LE : --default-search PREFIX         
        # CB : --ignore-config                 
        # CB : --no-config-locations           
        # LE : --config-locations PATH         
        # LE : --plugin-dirs PATH              
        # CB : --flat-playlist                 
        # CB : --no-flat-playlist              
        # CB : --live-from-start           

        label11 = QLabel("--extractor-descriptions")
        label12 = QLabel("--use-extractors")
        label13 = QLabel("--default-search")
        label14 = QLabel("--ignore-config")
        label15 = QLabel("--no-config-locations")
        label16 = QLabel("--config-locations")
        label17 = QLabel("--plugin-dirs")
        label18 = QLabel("--flat-playlist")
        label19 = QLabel("--no-flat-playlist")
        label20 = QLabel("--live-from-start")

        self.control11 = QCheckBox()
        self.control12 = QLineEdit("NAMES")
        self.control13 = QLineEdit("PREFIX")
        self.control14 = QCheckBox()
        self.control15 = QCheckBox()
        self.control16 = QLineEdit("PATH")
        self.control17 = QLineEdit("PATH")
        self.control18 = QCheckBox()
        self.control19 = QCheckBox()
        self.control20 = QCheckBox()

        # CB : --no-live-from-start            
        # LE : --wait-for-video MIN[-MAX]      
        # CB : --no-wait-for-video             
        # CB : --mark-watched                  
        # CB : --no-mark-watched               
        # LE : --color [STREAM:]POLICY 
        # LE : --compat-options OPTS           
        # LE : --alias ALIASES OPTIONS

        label21 = QLabel("--no-live-from-start")
        label22 = QLabel("--wait-for-video")
        label23 = QLabel("--no-wait-for-video")
        label24 = QLabel("--mark-watched")
        label25 = QLabel("--no-mark-watched")
        label26 = QLabel("--color")
        label27 = QLabel("--compat-options")
        label28 = QLabel("--alias")

        self.control21 = QCheckBox()
        self.control22 = QLineEdit()
        self.control23 = QCheckBox()
        self.control24 = QCheckBox()
        self.control25 = QCheckBox()
        self.control26 = QLineEdit()
        self.control27 = QLineEdit()
        self.control28 = QLineEdit()

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

        layoutGrid.addWidget(label9,         8,  0)
        layoutGrid.addWidget(labelSpacer9,   8,  1)
        layoutGrid.addWidget(self.control9,  8,  2)

        layoutGrid.addWidget(label10,        9,  0)
        layoutGrid.addWidget(labelSpacer10,  9,  1)
        layoutGrid.addWidget(self.control10, 9,  2)

        layoutGrid.addWidget(label11,        10, 0)
        layoutGrid.addWidget(labelSpacer11,  10, 1)
        layoutGrid.addWidget(self.control11, 10, 2)

        layoutGrid.addWidget(label12,        11, 0)
        layoutGrid.addWidget(labelSpacer12,  11, 1)
        layoutGrid.addWidget(self.control12, 11, 2)

        layoutGrid.addWidget(label13,        12, 0)
        layoutGrid.addWidget(labelSpacer13,  12, 1)
        layoutGrid.addWidget(self.control13, 12, 2)

        layoutGrid.addWidget(label14,        13, 0)
        layoutGrid.addWidget(labelSpacer14,  13, 1)
        layoutGrid.addWidget(self.control14, 13, 2)

        layoutGrid.addWidget(label15,        14, 0)
        layoutGrid.addWidget(labelSpacer15,  14, 1)
        layoutGrid.addWidget(self.control15, 14, 2)

        layoutGrid.addWidget(label16,        15, 0)
        layoutGrid.addWidget(labelSpacer16,  15, 1)
        layoutGrid.addWidget(self.control16, 15, 2)

        layoutGrid.addWidget(label17,        16, 0)
        layoutGrid.addWidget(labelSpacer17,  16, 1)
        layoutGrid.addWidget(self.control17, 16, 2)

        layoutGrid.addWidget(label18,        17, 0)
        layoutGrid.addWidget(labelSpacer18,  17, 1)
        layoutGrid.addWidget(self.control18, 17, 2)

        layoutGrid.addWidget(label19,        18, 0)
        layoutGrid.addWidget(labelSpacer19,  18, 1)
        layoutGrid.addWidget(self.control19, 18, 2)

        layoutGrid.addWidget(label20,        19, 0)
        layoutGrid.addWidget(labelSpacer20,  19, 1)
        layoutGrid.addWidget(self.control20, 19, 2)

        layoutGrid.addWidget(label21,        20, 0)
        layoutGrid.addWidget(labelSpacer21,  20, 1)
        layoutGrid.addWidget(self.control21, 20, 2)

        layoutGrid.addWidget(label22,        21, 0)
        layoutGrid.addWidget(labelSpacer22,  21, 1)
        layoutGrid.addWidget(self.control22, 21, 2)

        layoutGrid.addWidget(label23,        22, 0)
        layoutGrid.addWidget(labelSpacer23,  22, 1)
        layoutGrid.addWidget(self.control23, 22, 2)

        layoutGrid.addWidget(label24,        23, 0)
        layoutGrid.addWidget(labelSpacer24,  23, 1)
        layoutGrid.addWidget(self.control24, 23, 2)

        layoutGrid.addWidget(label25,        24, 0)
        layoutGrid.addWidget(labelSpacer25,  24, 1)
        layoutGrid.addWidget(self.control25, 24, 2)

        layoutGrid.addWidget(label26,        25, 0)
        layoutGrid.addWidget(labelSpacer26,  25, 1)
        layoutGrid.addWidget(self.control26, 25, 2)

        layoutGrid.addWidget(label27,        26, 0)
        layoutGrid.addWidget(labelSpacer27,  26, 1)
        layoutGrid.addWidget(self.control27, 26, 2)

        layoutGrid.addWidget(label28,        27, 0)
        layoutGrid.addWidget(labelSpacer28,  27, 1)
        layoutGrid.addWidget(self.control28, 27, 2)

        self.setWidget(frameTopLevel)


    def processJSON(self, dataJSON):

        # Retrieve the child element from the JSON.

        try:
            dataGeneral                = dataJSON["General"]
        except :
            print("Caught an exception : Probably no General element in JSON")

        print(dataGeneral)

        print("--help = ",    dataGeneral["--help"])
        print("--version = ", dataGeneral["--version"])

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