<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://solvespace.com">SolveSpace</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
	<a href="https://github.com/ndsboy/solvespace/stargazers"><img src="https://img.shields.io/github/stars/ndsboy/solvespace?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
	<a href="https://github.com/ndsboy/solvespace/issues"><img src="https://img.shields.io/github/issues/ndsboy/solvespace?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
	<a href="https://github.com/ndsboy/solvespace/contributors"><img src="https://img.shields.io/github/contributors/ndsboy/solvespace?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
	<img src="https://github.com/ndsboy/solvespace/blob/main/assets/preview.png"/>
</p>

## Previews

<details>
<summary>🌻 Latte</summary>
<img src="https://github.com/ndsboy/solvespace/blob/main/assets/latte.png"/>
</details>
<details>
<summary>🪴 Frappé</summary>
<img src="https://github.com/ndsboy/solvespace/blob/main/assets/frappe.png"/>
</details>
<details>
<summary>🌺 Macchiato</summary>
<img src="https://github.com/ndsboy/solvespace/blob/main/assets/macchiato.png"/>
</details>
<details>
<summary>🌿 Mocha</summary>
<img src="https://github.com/ndsboy/solvespace/blob/main/assets/mocha.png"/>
</details>

## Usage

### Overwriting your current settings

1. Download and replace the current `settings.json`:

   - 🌻 Latte:

     ```shell
     curl -o ~/.config/solvespace/settings.json https://raw.githubusercontent.com/ndsboy/solvespace/main/themes/latte.json
     ```

   - 🪴 Frappe:

     ```shell
     curl -o ~/.config/solvespace/settings.json https://raw.githubusercontent.com/ndsboy/solvespace/main/themes/frappe.json
     ```

   - 🌺 Macchiato:

     ```shell
     curl -o ~/.config/solvespace/settings.json https://raw.githubusercontent.com/ndsboy/solvespace/main/themes/macchiato.json
     ```

   - 🌿 Mocha:

     ```shell
     curl -o ~/.config/solvespace/settings.json https://raw.githubusercontent.com/ndsboy/solvespace/main/themes/mocha.json
     ```

### Merging with your current settings via script

1. Clone this repository locally

   ```shell
   git clone https://github.com/ndsboy/solvespace.git && cd solvespace
   ```

2. Apply the theme via script:

   - 🌻 Latte:

     ```shell
     ./apply.py latte ~/.config/solvespace/settings.json
     ```

   - 🪴 Frappe:

     ```shell
     ./apply.py frappe ~/.config/solvespace/settings.json
     ```

   - 🌺 Macchiato:

     ```shell
     ./apply.py macchiato ~/.config/solvespace/settings.json
     ```

   - 🌿 Mocha:

     ```shell
     ./apply.py mocha ~/.config/solvespace/settings.json
     ```

### Merging with your current settings manually

1. Open your theme from the `themes` folder in the browser

2. Open `~/.config/solvespace/settings.json` with your favourite text editor

3. At the second last line of the file (before the `}`), add a comma `,` and then paste the content of your theme (excluding `{` and `}`). You can ignore any warnings about duplicate keys, as SolveSpace will clean them up.

## 🙋 FAQ

- Q: **_"Why is the property window unstyled?"_**\
  A: The property window colors are [hardcoded](https://github.com/solvespace/solvespace/blob/50cbecbe7249a1a47561fca33919a08db7970e49/src/textwin.cpp#L196)

## 💝 Thanks to

- [ndsboy](https://github.com/ndsboy)

&nbsp;

<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
	Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>

<p align="center">
	<a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
