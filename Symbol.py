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
import mako.template
import collections
from MultiRegex import MultiRegex, NoRegexMatchedException

class InvalidSymbolException(Exception): pass

class _Pin():
	def __init__(self):
		self.name = None
		self.order = None

	def __lt__(self, other):
		# TODO Implement when no SpiceOrder PINATTR is given
		return (self.order < other.order)

class _Pins():
	def __init__(self):
		self.pins = [ ]

	def sort(self):
		self.pins.sort()

	def _match_pin(self, result):
		self.pins.append(_Pin())

	def _match_pinattr(self, result):
		if len(self.pins) == 0:
			print("Warning: PINATTR without preceding PIN ignored.")
			return
		pin = self.pins[-1]
		key = result["key"].lower()
		if key == "pinname":
			pin.name = result["value"]
		elif key == "spiceorder":
			pin.order = int(result["value"])


class Symbol():
	_MultiRegex = MultiRegex(collections.OrderedDict((
		("pin", re.compile("PIN\s+.*", flags = re.IGNORECASE)),
		("pinattr", re.compile("PINATTR\s+(?P<key>[-A-Za-z0-9_]+)\s+(?P<value>.*)", flags = re.IGNORECASE)),
	)))

	def __init__(self, name, asy_filename):
		self._name = name
		self._filename = asy_filename
		self._pins = self._scan_pins()
		self._template = None

	@property
	def filename(self):
		return self._filename

	@property
	def template(self):
		if self._template is None:
			self._template = mako.template.Template(filename = self._filename, input_encoding = "utf-8", strict_undefined = True)
		return self._template

	def _scan_pins(self):
		with open(self._filename) as f:
			pins = _Pins()
			for line in f:
				line = line.rstrip("\r\n")
				try:
					self._MultiRegex.fullmatch(line, callback = pins, groupdict = True)
				except NoRegexMatchedException:
					pass
		pins.sort()
		pinnames = [ pin.name for pin in pins.pins ]
		lc_names = set(pinname.lower() for pinname in pinnames)
		if len(lc_names) != len(pinnames):
			raise InvalidSymbolException("Symbol %s contains ambiguous pin names: %s" % (self._filename, ", ".join(pinnames)))
		return pinnames

	@property
	def name(self):
		return self._name

	@property
	def pincnt(self):
		return len(self.pins)

	@property
	def pins(self):
		return self._pins

	def dump(self):
		print("    %s" % (self))

	def render(self, subckt, subfile = None):
		return self.template.render(symbol = self, subckt = subckt, subfile = subfile)

	def __str__(self):
		return "Symbol<%s>: %s" % (self.name, ", ".join(self.pins))
