#!/usr/bin/python3
#	ltspicerender - Process LTSpice Subcicuits to macromodels
#	Copyright (C) 2013-2019 Johannes Bauer
#
#	This file is part of ltspicerender.
#
#	ltspicerender is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; this program is ONLY licensed under
#	version 3 of the License, later versions are explicitly excluded.
#
#	ltspicerender is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#	Johannes Bauer <JohannesBauer@gmx.de>

import os
from Symbol import Symbol

class Symbols():
	def __init__(self):
		self._symbols = { }

	def add_symbol(self, symbol):
		self._symbols[symbol.name] = symbol

	@classmethod
	def scan_directory(cls, dirname):
		symbols = cls()
		for filename in os.listdir(dirname):
			if filename.startswith("."):
				continue
			if not filename.endswith(".asy"):
				continue
			full_filename = dirname + "/" + filename
			name = filename[:-4]
			symbol = Symbol(name, full_filename)
			symbols.add_symbol(symbol)
		return symbols

	def dump(self):
		print("%d symbol(s) found:" % (len(self._symbols)))
		for (name, symbol) in sorted(self._symbols.items()):
			symbol.dump()

	def __getitem__(self, name):
		return self._symbols[name]
