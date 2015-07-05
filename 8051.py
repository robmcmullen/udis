##########################################################################
#
# Processor specific code

# CPU = "8080"
# Description = "Intel 8051 8-bit microprocessor."
# DataWidth = 8  # 8-bit data
# AddressWidth = 16  # 16-bit addresses

# Maximum length of an instruction (for formatting purposes)
maxLength = 3

# Leadin bytes for multibyte instructions
leadInBytes = []

# Addressing mode table
# List of addressing modes and corresponding format strings for operands.
addressModeTable = {
""           : "",
"addr11"     : "${0:02X}",
"addr16"     : "${1:02X}{0:02X}",
"direct"     : "${0:02X}",
"a"          : "a",
"r0"         : "r0",
"r1"         : "r1",
"r2"         : "r2",
"r3"         : "r3",
"r4"         : "r4",
"r5"         : "r5",
"r6"         : "r6",
"r7"         : "r7",
"@r0"        : "@r0",
"@r1"        : "@r1",
}

# Op Code Table
# Key is numeric opcode (possibly multiple bytes)
# Value is a list:
#   # bytes
#   mnemonic
#   addressing mode
#   flags (e.g. pcr)
opcodeTable = {

0x00 : [ 1, "nop",  ""           ],
0x01 : [ 2, "ajmp", "addr11"     ],
0x02 : [ 3, "ljmp", "addr16"     ],
0x03 : [ 1, "rr",   "a"          ],
0x04 : [ 1, "inc",  "a"          ],
0x05 : [ 2, "inc",  "direct"     ],
0x06 : [ 1, "inc",  "@r0"        ],
0x07 : [ 1, "inc",  "@r1"        ],
0x08 : [ 1, "inc",  "r0"         ],
0x09 : [ 1, "inc",  "r1"         ],
0x0a : [ 1, "inc",  "r2"         ],
0x0b : [ 1, "inc",  "r3"         ],
0x0c : [ 1, "inc",  "r4"         ],
0x0d : [ 1, "inc",  "r5"         ],
0x0e : [ 1, "inc",  "r6"         ],
0x0f : [ 1, "inc",  "r7"         ],

0x10 : [ 3, "jbc",  "bit,offset" ],
0x11 : [ 2, "acall", "addr11"    ],
0x12 : [ 3, "lcall", "addr16"    ],
0x13 : [ 1, "rrc",  "a"          ],
0x14 : [ 1, "dec",  "a"          ],
0x15 : [ 2, "dec",  "direct"     ],
0x16 : [ 1, "dec",  "r0"         ],
0x17 : [ 1, "dec",  "@r1"        ],
0x18 : [ 1, "dec",  "r0"         ],
0x19 : [ 1, "dec",  "r1"         ],
0x1a : [ 1, "dec",  "r2"         ],
0x1b : [ 1, "dec",  "r3"         ],
0x1c : [ 1, "dec",  "r4"         ],
0x1d : [ 1, "dec",  "r5"         ],
0x1e : [ 1, "dec",  "r6"         ],
0x1f : [ 1, "dec",  "r7"         ],

0x20 : [ 3, "jb",   "bit,offset" ],
0x21 : [ 2, "ajmp", "addr11"     ],
0x22 : [ 1, "ret",  ""           ],  
0x23 : [ 1, "rl",   "a"          ],
0x24 : [ 2, "add",  "a,immed"    ],
0x25 : [ 2, "add",  "a,direct"   ],
0x26 : [ 1, "add",  "a,r0"       ],
0x27 : [ 1, "add",  "a,@r1"      ],
0x28 : [ 1, "add",  "a,r0"       ],
0x29 : [ 1, "add",  "a,r1"       ],
0x2a : [ 1, "add",  "a,r2"       ],
0x2b : [ 1, "add",  "a,r3"       ],
0x2c : [ 1, "add",  "a,r4"       ],
0x2d : [ 1, "add",  "a,r5"       ],
0x2e : [ 1, "add",  "a,r6"       ],
0x2f : [ 1, "add",  "a,r7"       ],

0x30 : [ 3, "jnb", "bit,offset"  ],
0x31 : [ 2, "acall", "addr11"    ],
0x32 : [ 1, "reti", ""           ],
0x33 : [ 1, "rlc", "a"           ],
0x34 : [ 2, "addc", "a,immed"    ],
0x35 : [ 2, "addc", "a,direct"   ],
0x36 : [ 1, "addc", "a,@r0"      ],
0x37 : [ 1, "addc", "a,@r1"      ],
0x38 : [ 1, "addc", "a,r0"       ],
0x39 : [ 1, "addc", "a,r1"       ],
0x3a : [ 1, "addc", "a,r2"       ],
0x3b : [ 1, "addc", "a,r3"       ],
0x3c : [ 1, "addc", "a,r4"       ],
0x3d : [ 1, "addc", "a,r5"       ],
0x3e : [ 1, "addc", "a,r6"       ],
0x3f : [ 1, "addc", "a,r7"       ],

0x40 : [ 2, "jc offset
0x41 : [ 2, "ajmp addr11
0x42 : [ 2, "orl", "direct", a
0x43 : [ 3, "orl", "direct", #immed
0x44 : [ 2, "orl a, #immed
0x45 : [ 2, "orl a,", "direct"
0x46 : [ 1, "orl a, @r0
0x47 : [ 1, "orl a, @r1
0x48 : [ 1, "orl a, r0
0x49 : [ 1, "orl a, r1
0x4a : [ 1, "orl a, r2
0x4b : [ 1, "orl a, r3
0x4c : [ 1, "orl a, r4
0x4d : [ 1, "orl a, r5
0x4e : [ 1, "orl a, r6
0x4f : [ 1, "orl a, r7

0x50 : [ 2, "jnc offset
0x51 : [ 2, "acall addr11
0x52 : [ 2, "anl direct, a
0x53 : [ 3, "anl direct, #immed
0x54 : [ 2, "anl a, #immed
0x55 : [ 2, "anl a,", "direct"
0x56 : [ 1, "anl a, @r0
0x57 : [ 1, "anl a, @r1
0x58 : [ 1, "anl a, r0
0x59 : [ 1, "anl a, r1
0x5a : [ 1, "anl a, r2
0x5b : [ 1, "anl a, r3
0x5c : [ 1, "anl a, r4
0x5d : [ 1, "anl a, r5
0x5e : [ 1, "anl a, r6
0x5f : [ 1, "anl a, r7

0x60 : [ 2, "jz offset
0x61 : [ 2, "ajmp addr11
0x62 : [ 2, "xrl direct, a
0x63 : [ 3, "xrl direct, #immed
0x64 : [ 2, "xrl a, #immed
0x65 : [ 2, "xrl a,", "direct"
0x66 : [ 1, "xrl a, @r0
0x67 : [ 1, "xrl a, @r1
0x68 : [ 1, "xrl a, r0
0x69 : [ 1, "xrl a, r1
0x6a : [ 1, "xrl a, r2
0x6b : [ 1, "xrl a, r3
0x6c : [ 1, "xrl a, r4
0x6d : [ 1, "xrl a, r5
0x6e : [ 1, "xrl a, r6
0x6f : [ 1, "xrl a, r7

0x70 : [ 2, "jnz offset
0x71 : [ 2, "acall addr11
0x72 : [ 2, "orl c, bit
0x73 : [ 1, "jmp @a+dptr
0x74 : [ 2, "mov a, #immed
0x75 : [ 3, "mov direct, #immed
0x76 : [ 2, "mov @r0, #immed
0x77 : [ 2, "mov @r1, #immed
0x78 : [ 2, "mov r0, #immed
0x79 : [ 2, "mov r1, #immed
0x7a : [ 2, "mov r2, #immed
0x7b : [ 2, "mov r3, #immed
0x7c : [ 2, "mov r4, #immed
0x7d : [ 2, "mov r5, #immed
0x7e : [ 2, "mov r6, #immed
0x7f : [ 2, "mov r7, #immed

0x80 : [ 2, "sjmp offset
0x81 : [ 2, "ajmp addr11
0x82 : [ 2, "anl c, bit
0x83 : [ 1, "movc a, @a+pc
0x84 : [ 1, "div ab
0x85 : [ 3, "mov direct, direct
0x86 : [ 2, "mov direct, @r0
0x87 : [ 2, "mov direct, @r1
0x88 : [ 2, "mov direct, r0
0x89 : [ 2, "mov direct, r1
0x8a : [ 2, "mov direct, r2
0x8b : [ 2, "mov direct, r3
0x8c : [ 2, "mov direct, r4
0x8d : [ 2, "mov direct, r5
0x8e : [ 2, "mov direct, r6
0x8f : [ 2, "mov direct, r7

0x90 : [ 3, "mov dptr, #immed
0x91 : [ 2, "acall addr11
0x92 : [ 2, "mov bit, c
0x93 : [ 1, "movc a, @a+dptr
0x94 : [ 2, "subb a, #immed
0x95 : [ 2, "subb a, direct
0x96 : [ 1, "subb a, @r0
0x97 : [ 1, "subb a, @r1
0x98 : [ 1, "subb a, r0
0x99 : [ 1, "subb a, r1
0x9a : [ 1, "subb a, r2
0x9b : [ 1, "subb a, r3
0x9c : [ 1, "subb a, r4
0x9d : [ 1, "subb a, r5
0x9e : [ 1, "subb a, r6
0x9f : [ 1, "subb a, r7

0xa0 : [ 2, "orl c, /bit
0xa1 : [ 2, "ajmp addr11
0xa2 : [ 2, "mov c, bit
0xa3 : [ 1, "inc dptr
0xa4 : [ 1, "mul ab
0xa5   reserved  
0xa6 : [ 2, "mov @r0, direct
0xa7 : [ 2, "mov @r1, direct
0xa8 : [ 2, "mov r0, direct
0xa9 : [ 2, "mov r1, direct
0xaa : [ 2, "mov r2, direct
0xab : [ 2, "mov r3, direct
0xac : [ 2, "mov r4, direct
0xad : [ 2, "mov r5, direct
0xae : [ 2, "mov r6, direct
0xaf : [ 2, "mov r7, direct

0xb0 : [ 2, "anl c, /bit
0xb1 : [ 2, "acall addr11
0xb2 : [ 2, "cpl bit
0xb3 : [ 1, "cpl c
0xb4 : [ 3, "cjne a, #immed, offset
0xb5 : [ 3, "cjne a, direct, offset
0xb6 : [ 3, "cjne @r0, #immed, offset
0xb7 : [ 3, "cjne @r1, #immed, offset
0xb8 : [ 3, "cjne r0, #immed, offset
0xb9 : [ 3, "cjne r1, #immed, offset
0xba : [ 3, "cjne r2, #immed, offset
0xbb : [ 3, "cjne r3, #immed, offset
0xbc : [ 3, "cjne r4, #immed, offset
0xbd : [ 3, "cjne r5, #immed, offset
0xbe : [ 3, "cjne r6, #immed, offset
0xbf : [ 3, "cjne r7, #immed, offset

0xc0 : [ 2, "push direct
0xc1 : [ 2, "ajmp addr11
0xc2 : [ 2, "clr bit
0xc3 : [ 1, "clr c
0xc4 : [ 1, "swap a
0xc5 : [ 2, "xch a, direct
0xc6 : [ 1, "xch a, @r0
0xc7 : [ 1, "xch a, @r1
0xc8 : [ 1, "xch a, r0
0xc9 : [ 1, "xch a, r1
0xca : [ 1, "xch a, r2
0xcb : [ 1, "xch a, r3
0xcc : [ 1, "xch a, r4
0xcd : [ 1, "xch a, r5
0xce : [ 1, "xch a, r6
0xcf : [ 1, "xch a, r7

0xd0 : [ 2, "pop", "direct"
0xd1 : [ 2, "acall addr11
0xd2 : [ 2, "setb bit
0xd3 : [ 1, "setb c
0xd4 : [ 1, "da a
0xd5 : [ 3, "djnz direct, offset
0xd6 : [ 1, "xchd a, @r0
0xd7 : [ 1, "xchd a, @r1
0xd8 : [ 2, "djnz r0, offset
0xd9 : [ 2, "djnz r1, offset
0xda : [ 2, "djnz r2, offset
0xdb : [ 2, "djnz r3, offset
0xdc : [ 2, "djnz r4, offset
0xdd : [ 2, "djnz r5, offset
0xde : [ 2, "djnz r6, offset
0xdf : [ 2, "djnz r7, offset

0xe0 : [ 1, "movx a, @dptr
0xe1 : [ 2, "ajmp addr11
0xe2 : [ 1, "movx a, @r0
0xe3 : [ 1, "movx a, @r1
0xe4 : [ 1, "clr a
0xe5 : [ 2, "mov a, direct
0xe6 : [ 1, "mov a, @r0
0xe7 : [ 1, "mov a, @r1
0xe8 : [ 1, "mov a, r0
0xe9 : [ 1, "mov a, r1
0xea : [ 1, "mov a, r2
0xeb : [ 1, "mov a, r3
0xec : [ 1, "mov a, r4
0xed : [ 1, "mov a, r5
0xee : [ 1, "mov a, r6
0xef : [ 1, "mov a, r7

0xf0 : [ 1, "movx @dptr, a
0xf1 : [ 2, "acall addr11
0xf2 : [ 1, "movx @r0, a
0xf3 : [ 1, "movx @r1, a
0xf4 : [ 1, "cpl a
0xf5 : [ 2, "mov direct, a
0xf6 : [ 1, "mov @r0, a
0xf7 : [ 1, "mov @r1, a
0xf8 : [ 1, "mov r0, a
0xf9 : [ 1, "mov r1, a
0xfa : [ 1, "mov r2, a
0xfb : [ 1, "mov r3, a
0xfc : [ 1, "mov r4, a
0xfd : [ 1, "mov r5, a
0xfe : [ 1, "mov r6, a
0xff : [ 1, "mov r7, a

}

# End of processor specific code
##########################################################################
