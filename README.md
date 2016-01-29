# Show Global Glyph

## Plugin for Glyphsapp

This is a Plugin for the great [Glyphs Font Editor](http://glyphsapp.com/).

It displays a Glyph called *_global* in the Background of other Glyphs. 
This can give an alternative to Global Guidelines.

###### Up till Glyphs Version 2.3


### How to use

You have do add a Glyph called *_global*. This one will show in Background of each Glyph while using this Plugin.
Now you can draw every Form or stroke to be shown.

To show only strokes use an absolute setup form and use a overlayed double path (see Screenshot below).
That gives you the opportunity to setup just lines or filled form.

You can also use open contours to draw blue fields (see Screenshot below). Drawing strokes separately seems not to be possible ...


### Examples

![Show Global Glyph](ShowGlobalGlyph.png)


Some tricks on how to build those elements ...

![Show Global Glyph](BuildGlobalGlyph.png)


### Install

Download or clone the whole `Glyphsapp-Plugins`repo (it will contain more plugins soon) and copy the `NAMEOFTHEPLUGIN.glyphsReporter` into your Glyphsapp Plugins folder (eg. `/Library/Application\ Support/Glyphs/Plugins`), restart Glyphs and when ever you need it, toggle Plugin from the view menu.


### Known issues / ToDo

- Can't draw strokes on open contours
- For now there seems to be a Bug, that Inactive Layers wouldn't be shown ... I try to fix


### Pull Requests

Feel free to comment or pull requests for any improvements.


### License

Made possible with the GlyphsSDK by Georg Seifert (@schriftgestalt) and Rainer Erich Scheichelbauer (@mekkablue).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
