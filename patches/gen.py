#!/usr/bin/env python3

from pathlib import Path
import json
import urllib.request

textwin_template = """198,209c198,209
<     { 'd', RGBi(255, 255, 255) },  // Default   : white
<     { 'l', RGBi(100, 200, 255) },  // links     : blue
<     { 't', RGBi(255, 200, 100) },  // tree/text : yellow
<     { 'h', RGBi( 90,  90,  90) },
<     { 's', RGBi( 40, 255,  40) },  // Ok        : green
<     { 'm', RGBi(200, 200,   0) },
<     { 'r', RGBi(  0,   0,   0) },  // Reverse   : black
<     { 'x', RGBi(255,  20,  20) },  // Error     : red
<     { 'i', RGBi(  0, 255, 255) },  // Info      : cyan
<     { 'g', RGBi(128, 128, 128) },  // Disabled  : gray
<     { 'b', RGBi(200, 200, 200) },
<     { 0,   RGBi(  0,   0,   0) }
---
>     { 'd', RGBi(#text#) },  // Default   : white
>     { 'l', RGBi(#blue#) },  // links     : blue
>     { 't', RGBi(#yellow#) },  // tree/text : yellow
>     { 'h', RGBi(#overlay0#) },
>     { 's', RGBi(#green#) },  // Ok        : green
>     { 'm', RGBi(#yellow#) },
>     { 'r', RGBi(#crust#) },  // Reverse   : black
>     { 'x', RGBi(#red#) },  // Error     : red
>     { 'i', RGBi(#sky#) },  // Info      : cyan
>     { 'g', RGBi(#overlay0#) },  // Disabled  : gray
>     { 'b', RGBi(#subtext0#) },
>     { 0,   RGBi(#base#) }
213,216c213,216
<     { 'd', RGBi(  0,   0,   0) },  // Default   : black
<     { 't', RGBi( 34,  15,  15) },
<     { 'a', RGBi( 25,  25,  25) },  // Alternate : dark gray
<     { 'r', RGBi(255, 255, 255) },  // Reverse   : white
---
>     { 'd', RGBi(#base#) },  // Default   : black
>     { 't', RGBi(#surface1#) },
>     { 'a', RGBi(#surface0#) },  // Alternate : dark gray
>     { 'r', RGBi(#text#) },  // Reverse   : white
621c621
<                            /*fillColor=*/{ 30, 30, 30, 255 }, /*outlineColor=*/{});
---
>                            /*fillColor=*/{ #surface0#, 255 }, /*outlineColor=*/{});
951c951
<     lighting.backgroundColor = RGBi(0, 0, 0);
---
>     lighting.backgroundColor = RGBi(#base#);
"""

toolbar_template = """183c183
<                         /*fillColor=*/{ 30, 30, 30, 255 },
---
>                         /*fillColor=*/{ #surface0#, 255 },
201c201
<                                  /*fillColor=*/{ 45, 45, 45, 255 },
---
>                                  /*fillColor=*/{ #surface1#, 255 },
223c223
<                                  /*fillColor=*/{ 255, 255, 0, 75 },
---
>                                  /*fillColor=*/{ #yellow#, 75 },
"""

with urllib.request.urlopen('https://raw.githubusercontent.com/catppuccin/palette/v0.2.0/palette.json') as f:
  data = f.read().decode('utf-8')
  colors = json.loads(data)

  for theme in colors:
    textwin = textwin_template
    toolbar = toolbar_template
    print(theme)
    for color in colors[theme]:
      textwin = textwin.replace("#"+color+"#", colors[theme][color]["raw"])
      toolbar = toolbar.replace("#"+color+"#", colors[theme][color]["raw"])
    Path(theme + "_textwin.patch").write_text(textwin)
    Path(theme + "_toolbar.patch").write_text(toolbar)
    