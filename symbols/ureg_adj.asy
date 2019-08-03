Version 4
SymbolType CELL
RECTANGLE Normal 48 32 -48 -32
TEXT 1 -46 Center 2 ${subckt.name}
SYMATTR Value ${subckt.assigned_name}
SYMATTR Prefix X
SYMATTR SpiceModel ${subfile}
SYMATTR Value2 ${subckt.name}
SYMATTR Description Adjustable Voltage Regulator ${subckt.assigned_name}
PIN -48 -16 LEFT 8
PINATTR PinName In
PINATTR SpiceOrder 1
PIN 0 32 BOTTOM 8
PINATTR PinName Adj
PINATTR SpiceOrder 2
PIN 48 -16 RIGHT 8
PINATTR PinName Out
PINATTR SpiceOrder 3
