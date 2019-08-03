Version 4
SymbolType CELL
LINE Normal 0 44 0 36
LINE Normal 0 44 32 44
LINE Normal 32 44 32 52
LINE Normal 0 20 32 20
LINE Normal 32 20 16 44
LINE Normal 0 20 16 44
LINE Normal 16 0 16 20
LINE Normal 16 44 16 64
LINE Normal 8 32 -16 32
WINDOW 0 24 0 Left 2
WINDOW 3 24 64 Left 2
SYMATTR Value ${subckt.assigned_name}
SYMATTR Prefix X
SYMATTR SpiceModel ${subfile}
SYMATTR Value2 ${subckt.name}
SYMATTR Description Adjustable Shunt Regulator ${subckt.assigned_name}
PIN 16 64 NONE 0
PINATTR PinName -
PINATTR SpiceOrder 1
PIN 16 0 NONE 0
PINATTR PinName +
PINATTR SpiceOrder 2
PIN -16 32 NONE 0
PINATTR PinName Adj
PINATTR SpiceOrder 3
