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

class NameAssigner():
	_ACCEPTABLE_CHAR_RE = re.compile("[^A-Za-z0-9]")

	def __init__(self):
		self._names = set()

	def assign(self, name):
		prefix = self._sanitize(name)
		for i in range(1000):
			name = prefix if (i == 0) else "%s_%03d" % (prefix, i)
			if name not in self._names:
				self._names.add(name)
				return name
		else:
			raise Exception("Duplicate overflow.")

	@classmethod
	def _sanitize(cls, text):
		text = text.replace("/", "_")
		text = cls._ACCEPTABLE_CHAR_RE.sub("", text)
		return text
