# Dictionary of options and controls.

listOptionsGeneral = {"-h, --help"               : {"QCheckBox" : "Checked"},
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


listOptionsNetwork = {"--proxy"                    : {"QLineEdit" : "192.168.0.1"},
                      "--socket-timeout"           : {"QLineEdit" : "5"},
                      "--source-address"           : {"QLineEdit" : "192.168.0.200"},
                      "--impersonate"              : {"QLineEdit" : "foo@bar.com"},
                      "--list-impersonate-targets" : {"QLineEdit" : "True"},
                      "--force-ipv4"               : {"QLineEdit" : "False"},
                      "--force-ipv6"               : {"QLineEdit" : "True"},
                      "--enable-file-urls"         : {"QLineEdit" : "True"}}
