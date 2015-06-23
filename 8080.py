##########################################################################
#
# Processor specific code

# CPU = "8080"
# Description = "Intel 8080 8-bit microprocessor."
# DataWidth = 8  # 8-bit data
# AddressWidth = 16  # 16-bit addresses

# Maximum length of an instruction (for formatting purposes)
maxLength = 3

# Leadin bytes for multibyte instructions
leadInBytes = []

# Addressing mode table
# List of addressing modes and corresponding format strings for operands.
addressModeTable = {
"implied"    : "",
"rega"       : "a",
"regb"       : "b",
"regc"       : "c",
"regd"       : "d",
"rege"       : "e",
"regh"       : "h",
"regl"       : "h",
"regm"       : "m",
"regsp"      : "sp",
"regbb"      : "b,b",
"regbc"      : "b,c",
"regbd"      : "b,d",
"regbe"      : "b,e",
"regbh"      : "b,h",
"regbl"      : "b,l",
"regbm"      : "b,m",
"regba"      : "b,a",
"regcb"      : "c,b",
"regcc"      : "c,c",
"regcd"      : "c,d",
"regce"      : "c,e",
"regch"      : "c,h",
"regcl"      : "c,l",
"regcm"      : "c,m",
"regca"      : "c,a",
"regdb"      : "d,b",
"regdc"      : "d,c",
"regdd"      : "d,d",
"regde"      : "d,e",
"regdh"      : "d,h",
"regdl"      : "d,l",
"regdm"      : "d,m",
"regda"      : "d,a",
"regeb"      : "e,b",
"regec"      : "e,c",
"reged"      : "e,d",
"regee"      : "e,e",
"regeh"      : "e,h",
"regel"      : "e,l",
"regem"      : "e,m",
"regea"      : "e,a",
"reghb"      : "h,b",
"reghc"      : "h,c",
"reghd"      : "h,d",
"reghe"      : "h,e",
"reghh"      : "h,h",
"reghl"      : "h,l",
"reghm"      : "h,m",
"regha"      : "h,a",
"reglb"      : "l,b",
"reglc"      : "l,c",
"regld"      : "l,d",
"regle"      : "l,e",
"reglh"      : "l,h",
"regll"      : "l,l",
"reglm"      : "l,m",
"regla"      : "l,a",
"regmb"      : "m,b",
"regmc"      : "m,c",
"regmd"      : "m,d",
"regme"      : "m,e",
"regmh"      : "m,h",
"regml"      : "m,l",
"regma"      : "m,a",
"regab"      : "a,b",
"regac"      : "a,c",
"regad"      : "a,d",
"regae"      : "a,e",
"regah"      : "a,h",
"regal"      : "a,l",
"regam"      : "a,m",
"regaa"      : "a,a",
"regpsw"     : "psw",
"imm"        : "${0:02X}",
"immb"       : "b,${0:02X}",
"immc"       : "c,${0:02X}",
"immd"       : "d,${0:02X}",
"immh"       : "h,${0:02X}",
"immm"       : "m,${0:02X}",
"immxb"      : "b,${1:02X}{0:02X}",
"immxd"      : "d,${1:02X}{0:02X}",
"immxh"      : "h,${1:02X}{0:02X}",
"immxsp"     : "sp,${1:02X}{0:02X}",
"direct"     : "${1:02X}{0:02X}",
"0"          : "0",
"1"          : "1",
"2"          : "2",
"3"          : "3",
"4"          : "4",
"5"          : "5",
"6"          : "6",
"7"          : "7",
}

# Op Code Table
# Key is numeric opcode (possibly multiple bytes)
# Value is a list:
#   # bytes
#   mnemonic
#   addressing mode
#   flags (e.g. pcr)
opcodeTable = {

0x00 : [ 1, "nop",  "implied"    ],
0x01 : [ 3, "lxi",  "immxb"      ],
0x02 : [ 1, "stax", "regb"       ],
0x03 : [ 1, "inx",  "regb"       ],
0x04 : [ 1, "inr",  "regb"       ],
0x05 : [ 1, "dcr",  "regb"       ],
0x06 : [ 2, "mvi",  "immb"       ],
0x07 : [ 1, "rlc",  "implied"    ],
0x09 : [ 1, "dad",  "regb"       ],
0x0a : [ 1, "ldax", "regb"       ],
0x0b : [ 1, "dcx",  "regb"       ],
0x0c : [ 1, "inr",  "regc"       ],
0x0d : [ 1, "dcr",  "regc"       ],
0x0e : [ 2, "mvi",  "immc"       ],
0x0f : [ 1, "rrc",  "implied"    ],

0x11 : [ 3, "lxi",  "immxd"      ],
0x12 : [ 1, "stax", "regd"       ],
0x13 : [ 1, "inx",  "regd"       ],
0x14 : [ 1, "inr",  "regd"       ],
0x15 : [ 1, "dcr",  "regd"       ],
0x16 : [ 2, "mvi",  "immd"       ],
0x17 : [ 1, "ral",  "implied"    ],
0x19 : [ 1, "dad",  "implied"    ],
0x1a : [ 1, "ldax", "regd"       ],
0x1b : [ 1, "dcx",  "regd"       ],
0x1c : [ 1, "inr",  "rege"       ],
0x1d : [ 1, "dcr",  "rege"       ],
0x1e : [ 1, "mvi",  "rege"       ],
0x1f : [ 1, "rar",  "implied"    ],

0x21 : [ 3, "lxi",  "immh"      ],
0x22 : [ 1, "shld", "implied"   ],
0x23 : [ 1, "inx",  "regh"      ],
0x24 : [ 1, "inr",  "regh"      ],
0x25 : [ 1, "dcr",  "regh"      ],
0x26 : [ 2, "mvi",  "regh"      ],
0x27 : [ 1, "daa",  "implied"   ],
0x29 : [ 1, "dad",  "regh"      ],
0x2a : [ 3, "lhld", "direct"    ],
0x2b : [ 1, "dcx",  "regh"      ],
0x2c : [ 1, "inr",  "regl"      ],
0x2d : [ 1, "dcr",  "regl"      ],
0x2e : [ 2, "mvi",  "regl"      ],
0x2f : [ 1, "cma",  "implied"   ],

0x31 : [ 3, "lxi",  "immxsp"    ],
0x32 : [ 3, "sta",  "direct"    ],
0x33 : [ 1, "inx",  "regsp"     ],
0x34 : [ 1, "inr",  "regm"      ],
0x35 : [ 1, "dcr",  "regm"      ],
0x36 : [ 2, "mvi",  "immm"      ],
0x37 : [ 1, "stc",  "implied"   ],
0x39 : [ 1, "dad",  "regsp"     ],
0x3a : [ 3, "lda",  "direct"    ],
0x3b : [ 1, "dcx",  "regsp"     ],
0x3c : [ 1, "inr",  "rega"      ],
0x3d : [ 1, "dcr",  "rega"      ],
0x3e : [ 2, "mvi",  "rega"      ],
0x3f : [ 1, "cmc",  "implied"   ],

0x40 : [ 1, "mov",  "regbb"     ],
0x41 : [ 1, "mov",  "regbc"     ],
0x42 : [ 1, "mov",  "regbd"     ],
0x43 : [ 1, "mov",  "regbe"     ],
0x44 : [ 1, "mov",  "regbh"     ],
0x45 : [ 1, "mov",  "regbl"     ],
0x46 : [ 1, "mov",  "regbm"     ],
0x47 : [ 1, "mov",  "regba"     ],
0x48 : [ 1, "mov",  "regcb"     ],
0x49 : [ 1, "mov",  "regcc"     ],
0x4a : [ 1, "mov",  "regcd"     ],
0x4b : [ 1, "mov",  "regce"     ],
0x4c : [ 1, "mov",  "regch"     ],
0x4d : [ 1, "mov",  "regcl"     ],
0x4e : [ 1, "mov",  "regcm"     ],
0x4f : [ 1, "mov",  "regca"     ],

0x50 : [ 1, "mov",  "regdb"     ],
0x51 : [ 1, "mov",  "regdc"     ],
0x52 : [ 1, "mov",  "regdd"     ],
0x53 : [ 1, "mov",  "regde"     ],
0x54 : [ 1, "mov",  "regdh"     ],
0x55 : [ 1, "mov",  "regdl"     ],
0x56 : [ 1, "mov",  "regdm"     ],
0x57 : [ 1, "mov",  "regda"     ],
0x58 : [ 1, "mov",  "regeb"     ],
0x59 : [ 1, "mov",  "regec"     ],
0x5a : [ 1, "mov",  "reged"     ],
0x5b : [ 1, "mov",  "regee"     ],
0x5c : [ 1, "mov",  "regeh"     ],
0x5d : [ 1, "mov",  "regel"     ],
0x5e : [ 1, "mov",  "regem"     ],
0x5f : [ 1, "mov",  "regea"     ],

0x60 : [ 1, "mov",  "reghb"     ],
0x61 : [ 1, "mov",  "reghc"     ],
0x62 : [ 1, "mov",  "reghd"     ],
0x63 : [ 1, "mov",  "reghe"     ],
0x64 : [ 1, "mov",  "reghh"     ],
0x65 : [ 1, "mov",  "reghl"     ],
0x66 : [ 1, "mov",  "reghm"     ],
0x67 : [ 1, "mov",  "regha"     ],
0x68 : [ 1, "mov",  "reglb"     ],
0x69 : [ 1, "mov",  "reglc"     ],
0x6a : [ 1, "mov",  "regld"     ],
0x6b : [ 1, "mov",  "regle"     ],
0x6c : [ 1, "mov",  "reglh"     ],
0x6d : [ 1, "mov",  "regll"     ],
0x6e : [ 1, "mov",  "reglm"     ],
0x6f : [ 1, "mov",  "regla"     ],

0x70 : [ 1, "mov",  "regmb"     ],
0x71 : [ 1, "mov",  "regmc"     ],
0x72 : [ 1, "mov",  "regmd"     ],
0x73 : [ 1, "mov",  "regme"     ],
0x74 : [ 1, "mov",  "regmh"     ],
0x75 : [ 1, "mov",  "regml"     ],
0x76 : [ 1, "hlt",  "implied"   ],
0x77 : [ 1, "mov",  "regma"     ],
0x78 : [ 1, "mov",  "regab"     ],
0x79 : [ 1, "mov",  "regac"     ],
0x7a : [ 1, "mov",  "regad"     ],
0x7b : [ 1, "mov",  "regae"     ],
0x7c : [ 1, "mov",  "regah"     ],
0x7d : [ 1, "mov",  "regal"     ],
0x7e : [ 1, "mov",  "regam"     ],
0x7f : [ 1, "mov",  "regaa"     ],

0x80 : [ 1, "add",  "regb"      ],
0x81 : [ 1, "add",  "regc"      ],
0x82 : [ 1, "add",  "regd"      ],
0x83 : [ 1, "add",  "rege"      ],
0x84 : [ 1, "add",  "regh"      ],
0x85 : [ 1, "add",  "regl"      ],
0x86 : [ 1, "add",  "regm"      ],
0x87 : [ 1, "add",  "rega"      ],
0x88 : [ 1, "adc",  "regb"      ],
0x89 : [ 1, "adc",  "regc"      ],
0x8a : [ 1, "adc",  "regd"      ],
0x8b : [ 1, "adc",  "rege"      ],
0x8c : [ 1, "adc",  "regh"      ],
0x8d : [ 1, "adc",  "regl"      ],
0x8e : [ 1, "adc",  "regm"      ],
0x8f : [ 1, "adc",  "rega"      ],

0x90 : [ 1, "sub",  "regb"      ],
0x91 : [ 1, "sub",  "regc"      ],
0x92 : [ 1, "sub",  "regd"      ],
0x93 : [ 1, "sub",  "rege"      ],
0x94 : [ 1, "sub",  "regh"      ],
0x95 : [ 1, "sub",  "regl"      ],
0x96 : [ 1, "sub",  "regm"      ],
0x97 : [ 1, "sub",  "rega"      ],
0x98 : [ 1, "sbb",  "regb"      ],
0x99 : [ 1, "sbb",  "regc"      ],
0x9a : [ 1, "sbb",  "regd"      ],
0x9b : [ 1, "sbb",  "rege"      ],
0x9c : [ 1, "sbb",  "regh"      ],
0x9d : [ 1, "sbb",  "regl"      ],
0x9e : [ 1, "sbb",  "regm"      ],
0x9f : [ 1, "sbb",  "rega"      ],

0xa0 : [ 1, "ana",  "regb"      ],
0xa1 : [ 1, "ana",  "regc"      ],
0xa2 : [ 1, "ana",  "regd"      ],
0xa3 : [ 1, "ana",  "rege"      ],
0xa4 : [ 1, "ana",  "regh"      ],
0xa5 : [ 1, "ana",  "regl"      ],
0xa6 : [ 1, "ana",  "regm"      ],
0xa7 : [ 1, "ana",  "rega"      ],
0xa8 : [ 1, "xra",  "regb"      ],
0xa9 : [ 1, "xra",  "regc"      ],
0xaa : [ 1, "xra",  "regd"      ],
0xab : [ 1, "xra",  "rege"      ],
0xac : [ 1, "xra",  "regh"      ],
0xad : [ 1, "xra",  "regl"      ],
0xae : [ 1, "xra",  "regm"      ],
0xaf : [ 1, "xra",  "rega"      ],

0xb0 : [ 1, "ora",  "regb"      ],
0xb1 : [ 1, "ora",  "regc"      ],
0xb2 : [ 1, "ora",  "regd"      ],
0xb3 : [ 1, "ora",  "rege"      ],
0xb4 : [ 1, "ora",  "regh"      ],
0xb5 : [ 1, "ora",  "regl"      ],
0xb6 : [ 1, "ora",  "regm"      ],
0xb7 : [ 1, "ora",  "rega"      ],
0xb8 : [ 1, "cmp",  "regb"      ],
0xb9 : [ 1, "cmp",  "regc"      ],
0xba : [ 1, "cmp",  "regd"      ],
0xbb : [ 1, "cmp",  "rege"      ],
0xbc : [ 1, "cmp",  "regh"      ],
0xbd : [ 1, "cmp",  "regl"      ],
0xbe : [ 1, "cmp",  "regm"      ],
0xbf : [ 1, "cmp",  "rega"      ],

0xc0 : [ 1, "rnz",  "implied"   ],
0xc1 : [ 1, "pop",  "regb"      ],
0xc2 : [ 3, "jnz",  "direct"    ],
0xc3 : [ 3, "jmp",  "direct"    ],
0xc4 : [ 3, "cnz",  "direct"    ],
0xc5 : [ 1, "push", "regb"      ],
0xc6 : [ 2, "adi",  "imm"       ],
0xc7 : [ 1, "rst",  "0"         ],
0xc8 : [ 1, "rz",   "implied"   ],
0xc9 : [ 1, "ret",  "implied"   ],
0xca : [ 3, "jz",   "direct"    ],
0xcc : [ 3, "cz",   "direct"    ],
0xcd : [ 3, "call", "direct"    ],
0xce : [ 2, "aci",  "imm"       ],
0xcf : [ 1, "rst",  "1"         ],

0xd0 : [ 1, "rnc",  "implied"   ],
0xd1 : [ 1, "pop",  "regd"      ],
0xd2 : [ 3, "jnc",  "direct"    ],
0xd3 : [ 2, "out",  "imm"       ],
0xd4 : [ 3, "cnc",  "direct"    ],
0xd5 : [ 1, "push", "regd"      ],
0xd6 : [ 2, "sui",  "imm"       ],
0xd7 : [ 1, "rst",  "2"         ],
0xd8 : [ 1, "rc",   "implied"   ],
0xda : [ 3, "jc",   "direct"    ],
0xdb : [ 2, "in",   "imm"       ],
0xdc : [ 3, "cc",   "direct"    ],
0xde : [ 2, "sbi",  "imm"       ],
0xdf : [ 1, "rst",  "3"         ],

0xe0 : [ 1, "rpo",  "implied"   ],
0xe1 : [ 1, "pop",  "regh"      ],
0xe2 : [ 3, "jpo",  "direct"    ],
0xe3 : [ 1, "xthl", "implied"   ],
0xe4 : [ 3, "cpo",  "direct"    ],
0xe5 : [ 1, "push", "regh"      ],
0xe6 : [ 2, "ani",  "imm"       ],
0xe7 : [ 1, "rst",  "4"         ],
0xe8 : [ 1, "rpe",  "implied"   ],
0xe9 : [ 1, "pchl", "implied"   ],
0xea : [ 3, "jpe",  "direct"    ],
0xeb : [ 1, "xchg", "implied"   ],
0xec : [ 3, "cpe",  "direct"    ],
0xee : [ 2, "xri",  "imm"       ],
0xef : [ 1, "rst",  "5"         ],

0xf0 : [ 1, "rp",   "implied"   ],
0xf1 : [ 1, "pop",  "regpsw"    ],
0xf2 : [ 3, "jp",   "direct"    ],
0xf3 : [ 1, "di",   "implied"   ],
0xf4 : [ 3, "cp",   "direct"    ],
0xf5 : [ 1, "push", "regpsw"    ],
0xf6 : [ 2, "ori",  "imm"       ],
0xf7 : [ 1, "rst",  "6"         ],
0xf8 : [ 1, "rm",   "implied"   ],
0xf9 : [ 1, "sphl", "implied"   ],
0xfa : [ 3, "jm",   "direct"    ],
0xfb : [ 1, "ei",   "implied"   ],
0xfc : [ 3, "cm",   "direct"    ],
0xfe : [ 2, "cpi",  "imm"       ],
0xff : [ 1, "rst",  "7"         ],

}

# End of processor specific code
##########################################################################
