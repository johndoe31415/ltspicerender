Version 4
SymbolType CELL
LINE Normal 48 0 48 16
LINE Normal 48 80 4 80
LINE Normal 48 96 48 80
LINE Normal 4 16 48 16
LINE Normal 4 16 4 80
LINE Normal 4 4 4 16
LINE Normal 4 80 4 92
LINE Normal -7 72 -15 80
LINE Normal -7 88 -15 80
LINE Normal -7 72 -7 88
LINE Normal -48 80 -15 80
LINE Normal 4 80 -7 80
WINDOW 0 56 32 Left 2
WINDOW 3 56 72 Left 2
SYMATTR Value ${subckt.assigned_name}
SYMATTR Prefix X
SYMATTR SpiceModel ${subfile}
SYMATTR Value2 ${subckt.name}
SYMATTR Description P-Channel JFET ${subckt.assigned_name}
PIN 48 0 NONE 0
PINATTR PinName D
PINATTR SpiceOrder 1
PIN -48 80 NONE 0
PINATTR PinName G
PINATTR SpiceOrder 2
PIN 48 96 NONE 0
PINATTR PinName S
PINATTR SpiceOrder 3
