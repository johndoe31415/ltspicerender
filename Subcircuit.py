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

import re
import mako

class Subcircuit():
	_SUBCKT_RE = re.compile(r"\.SUBCKT\s+(?P<name>[a-zA-Z0-9_-]+)\s(?P<pins>[^#]+)", flags = re.IGNORECASE)

	def __init__(self, filename):
		self._filename = filename
		with open(filename) as f:
			self._source = f.read()
		self._pins = None
		self._name = None
		self._assigned_name = None
		self._parse()

	@property
	def filename(self):
		return self._filename

	@property
	def pins(self):
		return self._pins

	@property
	def pincnt(self):
		return len(self._pins)

	@property
	def name(self):
		return self._name

	@property
	def assigned_name(self):
		return self._assigned_name

	@assigned_name.setter
	def assigned_name(self, value):
		assert(self._assigned_name is None)
		self._assigned_name = value

	def _parse(self):
		for line in self._source.split("\n"):
			line = line.rstrip("\r\n")
			match = self._SUBCKT_RE.fullmatch(line)
			if match:
				break
		else:
			raise Exception("Cannot determine number of pins in subcircuit: %s" % (self.filename))
		match = match.groupdict()
		self._name = match["name"].strip()
		self._pins = re.split(r"\s+", match["pins"].strip(" \t\r\n"))

	def render(self, symbol_pin_order = None, subckt_pin_order = None):
		if (symbol_pin_order is not None) and (subckt_pin_order is not None):
			symbol_pin_order = [ pin.lower() for pin in symbol_pin_order ]
			subckt_pin_order = [ pin.lower() for pin in subckt_pin_order ]
			order_index = [ subckt_pin_order.index(pin) for pin in symbol_pin_order ]
		else:
			order_index = list(len(self.pins))

		rendering = [ ]
		match = None
		for line in self._source.split("\n"):
			line = line.rstrip("\r\n")
			if match is None:
				match = self._SUBCKT_RE.fullmatch(line)
				if match:
					match = match.groupdict()
					rearranged_pin_names = [ self.pins[index] for index in order_index ]
					rendering.append("* Rearranged pin indices: %s" % (rearranged_pin_names))
					line = ".SUBCKT %s %s" % (match["name"], " ".join(rearranged_pin_names))
			rendering.append(line)
		return "\n".join(rendering)

	def __str__(self):
		return "Subckt<%s {%s}>" % (self.name, " ".join(self.pins))
