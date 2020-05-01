# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
import traceback

class classGlobalGlyph(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'global glyph',
			'de': 'Globale Glyphe',
			'es': 'glifo global',
			'fr': 'glyphe global',
		})
		
		self.globalGlyphName = "_global"

	@objc.python_method
	def drawGlobalGlyph(self, Layer):
		Glyph = Layer.parent
		if Glyph.name == self.globalGlyphName:
			return
			
		Font = Glyph.parent
		globalGlyph = Font.glyphForName_(self.globalGlyphName)
		if globalGlyph is None:
			return
			
		thisMasterID = Layer.master.id
		globalLayer = globalGlyph.layers[thisMasterID]

		#draw path AND components for strokes and form:
		globalBezierPath = globalLayer.completeBezierPath
		if globalBezierPath:
			NSColor.colorWithCalibratedRed_green_blue_alpha_(1.0, 0.7, 0.2, 0.1).set()
			globalBezierPath.fill()
			NSColor.colorWithCalibratedRed_green_blue_alpha_(1.0, 0.7, 0.2, 1.0).set()
			globalBezierPath.stroke()

		# draw path for open forms
		globalBezierPath = globalLayer.openBezierPath
		if globalBezierPath:
			NSColor.colorWithCalibratedRed_green_blue_alpha_(0.0, 0.0, 1.0, 0.1).set()
			globalBezierPath.fill()
			NSColor.colorWithCalibratedRed_green_blue_alpha_(0.0, 0.0, 1.0, 0.9).set()
			globalBezierPath.stroke()

	@objc.python_method
	def background(self, Layer):
		try:
			self.drawGlobalGlyph(Layer)
		except:
			self.logError(traceback.format_exc())

	@objc.python_method
	def inactiveLayerBackground(self, Layer):
		try:
			self.drawGlobalGlyph(Layer)
		except:
			self.logError(traceback.format_exc())

	@objc.python_method
	def needsExtraMainOutlineDrawingForInactiveLayer_(self, Layer):
		return True

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
