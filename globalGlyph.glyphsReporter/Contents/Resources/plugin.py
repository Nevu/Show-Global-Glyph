# encoding: utf-8

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


from GlyphsApp.plugins import *
import traceback

class classGlobalGlyph(ReporterPlugin):

	def settings(self):
		self.menuName = Glyphs.localize({'en': u'global glyph', 'de': u'Globale Glyphe'})

	def drawGlobalGlyph(self, Layer):
		Glyph = Layer.parent
		Font = Glyph.parent
		thisMaster = Font.selectedFontMaster
		globalGlyph = Font.glyphForName_("_global")
		if globalGlyph is None:
			return
		globalLayer = globalGlyph.layers[thisMaster.id]

		#draw path AND components for strokes and form:
		try:
			globalBezierPath = globalLayer.completeBezierPath() # for Glyphs 2.3.1
		except:
			globalBezierPath = globalLayer.copyDecomposedLayer().bezierPath   # for Glyphs 2.3

		if globalBezierPath:
			NSColor.colorWithCalibratedRed_green_blue_alpha_(1.0, 0.7, 0.2, 0.1).set()
			globalBezierPath.fill()
			NSColor.colorWithCalibratedRed_green_blue_alpha_(1.0, 0.7, 0.2, 1.0).set()
			globalBezierPath.stroke()

		# draw path for open forms

		try:
			globalBezierPath = globalLayer.completeOpenBezierPath() # for Glyphs 2.3.1
		except:
			globalBezierPath = globalLayer.openBezierPath # for Glyphs 2.3

		if globalBezierPath:
			NSColor.colorWithCalibratedRed_green_blue_alpha_(0.0, 0.0, 1.0, 0.1).set()
			globalBezierPath.fill()
			NSColor.colorWithCalibratedRed_green_blue_alpha_(0.0, 0.0, 1.0, 0.9).set()
			globalBezierPath.stroke()

	def background(self, Layer):
		try:
			self.drawGlobalGlyph(Layer)
		except:
			self.logError(traceback.format_exc())

	def inactiveLayers(self, Layer):
		try:
			self.drawGlobalGlyph(Layer)
		except:
			self.logError(traceback.format_exc())

	def needsExtraMainOutlineDrawingForInactiveLayer_(self, Layer):
		return True

	def preview(self, Layer):
		try:
			self.drawGlobalGlyph(Layer)
		except:
			self.logError(traceback.format_exc())
