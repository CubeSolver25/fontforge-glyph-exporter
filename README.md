# fontforge-glyph-exporter
A Fontforge Python script for automatically exporting glyphs in SVG format.

# Instructions:
1. Open any font in FontForge.
2. In FontForge, go to "File -> Execute Script"
3. Open 'Glyph SVG Exporter.py' in any text editor, like Notepad or TextEdit. 
4. Copy everything inside the Python file, and paste it into the FontForge Script Window.
5. Select the bubble that says Python, and then run the script.
6. Run the script, and follow the instructions that the program gives you.
7. Assuming no errors were displayed, you should now have a folder containing all of your desired glyphs alongisde a "kerning" file which contains the spacing data for every exported character. Use these to help create your own text engine if desired.

# Motivation:
This script was originally created to aid in the development of a Scratch project which contained a text engine. Due to a lack of adequate glyph exporters at the time, I resorted to creating my own which runs with the assistance of FontForge, a font editing program.

# Notes for Scratchers:
If you're using the Sprite Folders addon from Scratch Addons, create a folder for each unique font for easier organization. If you cannot install the addon, you can set the prefix of the exported glyphs to '[FontName]//' instead.

If you want to create more copies of the same font to allow different saturation levels, you are free to do so, but in most cases you only need the RED and BLACK versions of the glyphs. You can use brightness instead to simulate saturation to limited degrees.