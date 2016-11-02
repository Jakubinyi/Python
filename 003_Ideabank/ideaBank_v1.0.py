import locale
import sys
print(locale.getpreferredencoding())
lines = []
n = 0
file = open("ideas.txt", "w")

with open('ideas.txt', mode='r', encoding='utf-8') as i_file:  # READS IN FILE
        for line in i_file:
            lines.append(line)
for delArg in sys.argv:
    n = n + 1
if n == 1:
    delArg = ''
print(len(lines))
if delArg != '':
    if len(lines) < int(delArg):
        print('Hiba a rendszerben:(')
    elif delArg == "":
        print('HIBA A RENDSZERBEN :()')
    elif len(lines) == int(delArg):
        print('Hiba a Rendszerben:)')
    else:
        del lines[int(delArg)]
        print('Line %d was deleted.' % int(delArg))
with open('ideas.txt', mode='w', encoding='utf-8') as i_file:
    i_file.write('\n'.join(lines))

openFile = input('Do you wish to open your Idea Bank? Y/N ')        # PRINTS OUT FILE
while True:
    if openFile != 'n' and openFile != 'N' and openFile != 'y' and openFile != 'Y':
        openFile = input('Do you wish to open your Idea Bank? Y/N ')
    else:
        break
if openFile == 'y' or openFile == 'Y':
    with open('ideas.txt', mode='r', encoding='utf-8') as i_file:
        print('Your Idea Bank:')
        print(i_file.read())
wipeFile = input('Do you wish to wipe your Idea Bank? Y/N ')        # WIPES FILE
while True:
    if wipeFile != 'n' and wipeFile != 'N' and wipeFile != 'y' and wipeFile != 'Y':
        wipeFile = input('Do you wish to wipe your Idea Bank? Y/N ')
    else:
        break
if wipeFile == 'y' or wipeFile == 'Y':
    with open('ideas.txt', mode='w', encoding='utf-8') as i_file:
        i_file.write('')
        print('Idea Bank wiped.')
addIdea = input('Do you wish to add to your Idea Bank? Y/N ')       # ADDS TO FILE
while True:
    if addIdea != 'n' and addIdea != 'N' and addIdea != 'y' and addIdea != 'Y':
        addIdea = input('Do you wish to add to your Idea Bank? Y/N ')
    else:
        break
if addIdea == 'y' or addIdea == 'Y':
    with open('ideas.txt', mode='a', encoding='utf-8') as i_file:
        i_file.write(input('Write your idea here: \n'))
        i_file.write('\n')

        



    

