#Programmed using the Desperately-Search-and-Code-Terribly method by CubeSolver25, with immense help from NotestQ and skef. 

from pathlib import Path
import fontforge
import psMat
import re
import os  

#Don't change these. This helps find the viewBox data in the exported SVGs, and helps convert filename unfriendly charaters into their names when exporting.
viewboxkey = 'viewBox="(.*) (.*) (.*) (.*)"'
#specialchars = ' <>:"/\|?*.%^' 
#specialcharnames = ['space', 'lessthan', 'greaterthan', 'colon', 'doublequote', 'forwardslash', 'backslash', 'pipe', 'question', 'asterisk', 'period', 'percent', 'caret']
#specialchars = " !\"#$%&'*+/:<=>?@[\]^`{|}~¡¢£¤¥¦§¨©ª«¬­®¯´¶º»÷˙˚˜†•™∂∆∑√∞∫≈≠≤≥"
#specialcharnames = ['space', 'exclamation', 'quotation', 'hash', 'dollar', 'percent', 'ampersand', 'apostrophe', 'asterisk', 'plus', 'slash', 'colon', 'less', 'equal', 'greater', 'question', 'at', 'left_bracket', 'backslash', 'right_bracket', 'caret', 'backtick', 'left_brace', 'pipe', 'right_brace', 'small_tilde', 'inverted_exclamation', 'cent', 'pound', 'currency', 'yen', 'broken_bar', 'section', 'umlaut', 'copyright', 'feminine_ordinal', 'left_guillemet', 'negation', 'soft_hyphen', 'registered', 'macron', 'acute', 'paragraph', 'masculine_ordinal', 'right_guillemet', 'division', 'dot_above', 'ring_above', 'tilde', 'dagger', 'bullet', 'trademark', 'partial_derivative', 'delta', 'summation', 'root', 'infinity', 'integral', 'approximate', 'not_equal', 'less_equal', 'greater_equal']
specialchars = ' !"#$%&\'*+./:<=>?@\`{|}'
specialcharnames = ['space', 'exclamation', 'double_quote', 'hash', 'dollar', 'percent', 'ampersand', 'single_quote', 'asterisk', 'plus', 'period', 'slash', 'colon', 'less', 'equal', 'greater', 'question', 'at', 'backslash', 'backtick', 'left_brace', 'pipe', 'right_brace']

#Where the font file is located.
fontfile = fontforge.openFilename('Select the font you want to export glyphs from.')
#fontfile = fontforge.askString('Specify Font Location', 'Paste the pathname to the font you want to export glyphs from.')
fontfile = fontfile.replace('\\ ', ' ')
f = fontforge.open(fontfile)

glyphs = f.glyphs("encoding")

#Where to export the SVGs.
destinationSourceType = fontforge.ask('Select Destination', 'Where do you want to export these graphics?', ['Into a New Folder', 'Into an Existing Folder'], 0)
if destinationSourceType:
    destination = fontforge.openFilename('Select the destination you want to export the glyphs to.')
else:
    destination = str(Path(fontfile).parent / fontforge.askString('Specify Folder Name', 'Enter the name you want the folder to have.'))
    Path(destination).mkdir(parents=True, exist_ok=True)
#destination = fontforge.askString('Specify Destination', 'Paste the pathname to the directory you want to export the glyphs to.')
destination = destination.replace('\\ ', ' ')
fontforge.logWarning("Exporting glyphs to " + destination)
kerningFile = str(Path(destination) / (str(f.fontname) + '_kerning.lua'))

#What characters you want to export.
characterSourceType = fontforge.ask('Character Entry Method', 'How do you want to enter the characters you want to export?', ['From .txt File', 'Type into Text Field', 'All Glyphs in Font'], 0)

characters = ''

if characterSourceType == 0:
    charactersource = fontforge.openFilename('Select the file that contains all of the characters you want to export glyphs for.')
    with open(str(Path(charactersource)), 'r', encoding='utf-8') as file:
        characters = file.read()
        characters = characters.replace('\n', '')
        fontforge.logWarning('Exporting Characters: ' + characters)
if characterSourceType == 1:
    characters = fontforge.askString('Specify Characters', 'Type/Paste in every character you want to export glyphs for.')
   

targetEm = 'bleh'
targetColor = 'black'

while not (targetEm.isnumeric() or not len(targetEm.strip())):
        targetEm = fontforge.askString('Specify Font Size', 'What font size (in em) do you want the glyphs to be exported with? Leave this empty to export the glyphs at their original size, which is usually 1000em or 2048em.')

if len(targetEm.strip()):
    resizeType = fontforge.askChoices('Resize Method', "Select the resize method you would like to use.", ['New (Recommended): Scales the viewBox of the exported SVGs, and then applies a scale transformation via <g></g> tags to avoid distorting the glyphs.', 'Old: Applies an EM change to the font itself, resizing all glyphs by changing their path data. May lead to distorted glyphs, which you might/might not find useful.'], 0)
    if resizeType:    
        f.em = float(targetEm)
else:
    targetEm = str(f.em)

targetColor = fontforge.askString('Specify Color', 'What color do you want the glyphs to be exported with? Leave this empty to export the glyphs at the default color, which is usually black.') 

prefix = str(fontforge.askString("Specify Prefix", "What prefix do you want to apply to the filenames of these SVGs? Leave empty if you don't want a prefix."))

suffix = str(fontforge.askString("Specify Suffix", "What suffix do you want to apply to the filenames of these SVGs? Leave empty if you don't want a suffix."))

allupperchars = ""

filedata = ''
#ASCII 0-127 Characters (Whitespace included):
# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
#ASCII 0-255 Characters (Whitespace included):
# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞ


#with open(str(Path(destination) / "em.txt"), 'w') as emtxt:
#    emtxt.write(str(f.em))

def scaleGlyph(data, scale):
    i = 0
    viewBoxData = re.search(viewboxkey, data)
    originalViewBoxDimensions = viewBoxData.group(0)
    viewBoxDimensions = viewBoxData.group(1, 2, 3, 4)
    viewBoxDimensions = list(viewBoxDimensions)
    finalviewbox = 'viewBox="'
    for dimension in viewBoxDimensions:
        finalviewbox = finalviewbox + str(float(dimension) * (scale))
        if not viewBoxDimensions.index(dimension) == 3:
            finalviewbox = finalviewbox + ' '
        else: 
            finalviewbox = finalviewbox + '"'
        i+=1
    data = data.replace(originalViewBoxDimensions, finalviewbox)
    if '<path' in data:
        data = data.replace('<path', '<g transform="scale(' + str(scale) + ')">\n<path')
        data = data.replace('</svg>', '</g>\n</svg>')
    return data


def changeGlyphColor(data, color):
    if(len(color)):
        return data.replace('fill="currentColor"', 'fill="' + str(color) + '"')
    else:
        return data

def modifySVG(path):
    with open(path, 'r') as file:  
        filedata = file.read()
    if len(targetColor.strip()):
        filedata = changeGlyphColor(filedata, targetColor)
    if len(targetEm.strip()):
        filedata = scaleGlyph(filedata, (float(targetEm)/f.em))
    with open(path, 'w') as file:
        file.write(filedata)


def appendToKerningFile(path, character, advancewidth, scale):
    exceptionCharacters = '"\'[\]'
    replacedCharacter = character
    if replacedCharacter == ' ':
        replacedCharacter = 'space'
    elif replacedCharacter in exceptionCharacters:
        replacedCharacter = '\\' + replacedCharacter
    characterString = "  ['" + replacedCharacter + "'] = " + str(float(advancewidth * scale)) + ',\n'
    with open(path, 'a', encoding='utf-8') as file:
        file.write(characterString)
    fontforge.logWarning(str(os.path.getsize(path)))


try:
    with open(kerningFile, 'w') as file:
        file.write('return {\n')
except EnvironmentError:
    pass


if not characterSourceType == 2:
    characters_written = set() # by saiketsu, who did not realize there is a duplicate character in his set.

    for i, char in enumerate(characters):
        #if isinstance(char, int):
        #    char = chr(char)'
        encoding = ord(char)
        fontforge.logWarning("Attempting to export glyph " + str(encoding))
        try: 
            g = f[encoding]
        except:
            fontforge.logWarning("Failed to load glyph in Unicode slot " + str(encoding))    
        else:
            characterName = char
            fontforge.logWarning(str(g.boundingBox()))    
            fontforge.logWarning(str(g.vwidth))  
            appendToKerningFile(kerningFile, char, g.width, (float(targetEm)/f.em))

            if char in specialchars:
                characterName = specialcharnames[specialchars.index(char)]
                print("Special Character Detected")
            elif char.isalpha():
                if char.isupper():
                    allupperchars = allupperchars + char
                    characterName = "u" + char

            if char in characters_written:
                fontforge.logWarning(f"Duplicate character in your character set: {char}")
                continue

            originalFilename = str(Path(destination) / (str(encoding) + '.svg'))
            targetFilename = str(Path(destination) / (prefix + characterName + suffix + '.svg'))
            g.export(originalFilename)
            modifySVG(originalFilename)
            os.rename(originalFilename, targetFilename)

            characters_written.add(char)
else:
    fontforge.logWarning('woo')
    for i in glyphs:
        try:
            encoding = i.unicode
            fontforge.logWarning(str(encoding))
            char = chr(encoding)
        except:
            fontforge.logWarning("Failed to load glyph")    
        else:
            characterName = char
            fontforge.logWarning(str(i.boundingBox()))    
            fontforge.logWarning(str(i.vwidth))  
            appendToKerningFile(kerningFile, char, i.width, (float(targetEm)/f.em))
            if char in specialchars:
                characterName = specialcharnames[specialchars.index(char)]
                print("Special Character Detected")
            elif char.isalpha():
                if char.isupper():
                    allupperchars = allupperchars + char
                    characterName = char
            originalFilename = str(Path(destination) / (str(encoding) + '.svg'))
            targetFilename = str(Path(destination) / (prefix + characterName + suffix + '.svg'))
            i.export(originalFilename)
            modifySVG(originalFilename)
            os.rename(originalFilename, targetFilename)
            
with open(kerningFile, 'a') as file:
    file.write('}')
fontforge.logWarning(str(f.ascent))  
fontforge.logWarning(str(f.descent))  
fontforge.logWarning(str(f.ascent + f.descent))  

# Read in the file
# with open(file, 'r') as file :
#  filedata = file.read()

# Replace the target string
#filedata = filedata.replace('ram', 'abcd')
#filedata = filedata.replace(')

# Write the file out again
#with open('file.txt', 'w') as file:
#  file.write(filedata)
