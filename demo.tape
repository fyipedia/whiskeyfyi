# whiskeyfyi — Python Whiskey Encyclopedia Demo
Output demo.gif

Set FontSize 14
Set Width 920
Set Height 620
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 35ms
Set Padding 20

Type `curl -s 'https://whiskeyfyi.com/api/search/?q=bourbon' | jq '.results[:3][] | {name, type}'`
Enter
Sleep 3s

Type `curl -s 'https://whiskeyfyi.com/api/type/bourbon/' | jq '{name, region}'`
Enter
Sleep 3s

Type `curl -s 'https://whiskeyfyi.com/api/random/' | jq '{name, type}'`
Enter
Sleep 3s

Sleep 2s
