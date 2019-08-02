# ltspicerender
ltspicerender takes subcircuits and symbols and creates macromodels from them.
The idea is that you just add a "LM324" op-amp or a "BAT48" Schottky diode
instead of fiddling with a generic diode, adding the subcircuit model and using
a SPICE directive to marry the two. It also takes care of pin mapping, which
can be a real pain (subcircuits routinely have differing pin layouts and in
manual labor it can be tedious and error-prone to correctly set them up).

However, with recent LTSpice versions this doesn't work anymore. It worked in
2013 when I first created this (honestly!), but currently is dysfunctional. I
need to fix it up to get it to work again.

## License
GNU-GPL 3.
