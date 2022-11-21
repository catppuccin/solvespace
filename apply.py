#!/usr/bin/env python3

from pathlib import Path
import json
import sys
import urllib.request

def main():
  with urllib.request.urlopen('https://raw.githubusercontent.com/catppuccin/palette/main/palette.json') as f:
    data = f.read().decode('utf-8')
    colors = json.loads(data)

  colormap = {
    "BackgroundColor": "base",
    "ModelColor_0": "text",
    "ModelColor_1": "overlay0",
    "ModelColor_2": "base",
    "ModelColor_3": "red",
    "ModelColor_4": "green",
    "ModelColor_5": "teal",
    "ModelColor_6": "blue",
    "ModelColor_7": "mauve",
    "Style_ActiveGrp_Color": "text",
    "Style_Construction_Color": "green",
    "Style_InactiveGrp_Color": "surface0",
    "Style_Datum_Color": "green",
    "Style_SolidEdge_Color": "subtext0",
    "Style_Constraint_Color": "mauve",
    "Style_Selected_Color": "red",
    "Style_Hovered_Color": "yellow",
    "Style_ContourFill_Color": "lavender",
    "Style_Normals_Color": "blue",
    "Style_Analyze_Color": "sky",
    "Style_DrawError_Color": "red",
    "Style_DimSolid_Color": "surface0",
    "Style_HiddenEdge_Color": "overlay0",
    "Style_Outline_Color": "subtext0"
  }

  settings = {}
  settings_file = Path(sys.argv[2])
  if settings_file.exists():
    settings = json.loads(settings_file.read_text())

  for color in colormap:
    hx = colors[sys.argv[1]][colormap[color]]["hex"]
    settings[color] = int(hx[5:7]+hx[3:5]+hx[1:3], 16)

  settings_file.write_text(json.dumps(settings, indent = "  "))

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("missing arguments: ./apply.py [theme] [path]")
    exit(1)
  main()