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
		self.generalContextMenus = [
			{'name': Glyphs.localize({'en': u'Do something', 'de': u'Tu etwas'}), 'action': self.doSomething},
		]
		
	def drawGlobalGlyph( self, Layer ):

		Glyph = Layer.parent
		Font = Glyph.parent
		thisMaster = Font.selectedFontMaster
		masters = Font.masters

		try:
			# Glyphs 2 (Python 2.7)
			activeMasterIndex = masters.index(thisMaster)
		except:
			# Glyphs 1 (Python 2.6)
			for i, k in enumerate(masters):
				if thisMaster == masters[i]:
					activeMasterIndex = i

		globalGlyph = Font.glyphForName_("_global")
		if globalGlyph is None:
			return
		thisLayer = globalGlyph.layers[activeMasterIndex]

		#draw path AND components for strokes and form:

		try:
			thisBezierPathWithComponent = thisLayer.copyDecomposedLayer().bezierPath() # for Glyphs 2.2
		except:
			thisBezierPathWithComponent = thisLayer.copyDecomposedLayer().bezierPath   # for Glyphs 2.3

		if thisBezierPathWithComponent:
			NSColor.colorWithCalibratedRed_green_blue_alpha_( 1.0, 0.7, 0.2, 0.1 ).set()
			thisBezierPathWithComponent.fill()
			NSColor.colorWithCalibratedRed_green_blue_alpha_( 1.0, 0.7, 0.2, 1.0 ).set()
			thisBezierPathWithComponent.stroke()

		# draw path for open forms

		try:
			thisOpenBezierPath = thisLayer.openBezierPath() # for Glyphs 2.2
		except:
			thisOpenBezierPath = thisLayer.openBezierPath # for Glyphs 2.3

		if thisOpenBezierPath:
			NSColor.colorWithCalibratedRed_green_blue_alpha_( 0.0, 0.0, 1.0, 0.1 ).set()
			thisOpenBezierPath.fill()
			NSColor.colorWithCalibratedRed_green_blue_alpha_( 0.0, 0.0, 1.0, 0.9 ).set()
			thisOpenBezierPath.stroke()


	def background(self, Layer):
		try:
			self.drawGlobalGlyph( Layer )
		except:
			self.logError(traceback.format_exc())

	def inactiveLayers(self, Layer):
		try:
			self.drawGlobalGlyph( Layer )
		except:
			self.logError(traceback.format_exc())

	def preview(self, Layer):
		try:
			self.drawGlobalGlyph( Layer )



	def doSomething(self):
		print 'Just did something'
		
	def conditionalContextMenus(self):

		# Empty list of context menu items
		contextMenus = []

		# Execute only if layers are actually selected
		if Glyphs.font.selectedLayers:
			layer = Glyphs.font.selectedLayers[0]
			
			# Exactly one object is selected and it’s an anchor
			if len(layer.selection) == 1 and type(layer.selection[0]) == GSAnchor:
					
				# Add context menu item
				contextMenus.append({'name': Glyphs.localize({'en': u'Do something else', 'de': u'Tu etwas anderes'}), 'action': self.doSomethingElse})

		# Return list of context menu items
		return contextMenus

	def doSomethingElse(self):
		print 'Just did something else'
		except:
			self.logError(traceback.format_exc())
