"""
Making a duplicate file finder, i got this idea from my dada ji ,
while he was trying to delete all same photos. So this is for him :)
"""
from os import remove, listdir
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.filedialog import askdirectory


def bro():
    global text
    global folder_name
    browse_text.set('Loading..')
    file_dir = askdirectory(title='Choose Folder')
    browse_text.set('Select Folder')
    text = str(file_dir)
    path = text.split('/')
    folder_name = path[-1]
    folder_text.set(f'Folder Name: {folder_name}')
    del path
    if folder_name == '':
        r1['state'] = DISABLED
        r2['state'] = DISABLED
        r3['state'] = DISABLED
        r4['state'] = DISABLED
        r5['state'] = DISABLED
        r6['state'] = DISABLED
    else:
        r1['state'] = NORMAL
        r2['state'] = NORMAL
        r3['state'] = NORMAL
        r4['state'] = NORMAL
        r5['state'] = NORMAL
        r6['state'] = NORMAL


def radio(x):
    global rad
    rad = x
    start_btn['state'] = NORMAL


def start(t, r):
    if r == 2:
        flist = [f for f in listdir(t) if f.endswith('.txt') or f.endswith('.rtf')]
        read_type = 'r'

    elif r == 3:
        flist = [f for f in listdir(t) if f.endswith('.doc') or f.endswith('.docx') or f.endswith('.pdf')]
        read_type = 'rb'

    elif r == 4:
        flist = [f for f in listdir(t) if f.endswith('.mp4') or f.endswith('.mkv') or f.endswith('.avi')
                 or f.endswith('.3gp') or f.endswith('.webm')]
        read_type = 'rb'

    elif r == 5:  # aud
        flist = [f for f in listdir(t) if f.endswith('.mp3') or f.endswith('.wav') or f.endswith('.aac')
                 or f.endswith('.mka') or f.endswith('.tta')]
        read_type = 'rb'

    elif r == 6:
        flist = [f for f in listdir(t)]
        read_type = 'rb'

    else:
        flist = [f for f in listdir(t) if f.endswith('.jpg') or f.endswith('.jpeg')
                 or f.endswith('.png') or f.endswith('.tiff') or f.endswith('.bmp') or f.endswith('.gif')]
        read_type = 'rb'

    if len(flist) == 0:
        end(0)
        return

    main_count = 0
    loadstr = StringVar()
    while main_count <= len(flist) - 1:
        count = main_count + 1
        with open(t + '/' + flist[main_count], read_type) as f:
            fr = f.read()

        while count < len(flist):
            with open(t + '/' + flist[count], read_type) as f1:
                fr1 = f1.read()

            if fr == fr1:
                remove(t + '/' + flist[count])
                flist.pop(count)
                count -= 1

            count += 1
        main_count += 1

        # --------------------Loading screen---------------------
        bar = Progressbar(root, orient=HORIZONTAL, length=600)
        bar.place(x=200, y=520)

        loadstr = StringVar()
        load = Label(root, textvariable=loadstr, bg='#00FA9A', font=("Arial", 13))
        loadstr.set('Loading')
        load.place(x=130, y=518)
        per = StringVar()
        percent = Label(root, textvariable=per, bg='#00FA9A', font=("Arial", 13))
        percent.place(x=830, y=518)

        percentage = int((main_count / len(flist)) * 100)
        per.set(str(percentage) + '%    ')
        bar['value'] += percentage
        root.update_idletasks()
        # -------------------------------------------------------
    loadstr.set('Done   ')
    end(r)


def end(r):
    endtxt = StringVar()
    ending = Label(root, textvariable=endtxt, bg='#00FA9A', font=("Arial", 13))
    ending.place(x=200,y=550)

    if r == 1: endtxt.set('Successfully Deleted All Duplicate Image Files!!       ')
    elif r == 2: endtxt.set('Successfully Deleted All Duplicate Text Files!!        ')
    elif r == 3: endtxt.set('Successfully Deleted All Duplicate Rich Text Files!!   ')
    elif r == 4: endtxt.set('Successfully Deleted All Duplicate Video Files!!       ')
    elif r == 5: endtxt.set('Successfully Deleted All Duplicate Sound Files!!       ')
    elif r == 6: endtxt.set('Successfully Deleted All Duplicate Files!!             ')
    else: endtxt.set('There Are No Valid Files To Delete In The Folder!!     ')


root = Tk()
root.title('Created By Kairav, With Love!!    --Ver 1.3')
root.maxsize(1000, 600)
root.minsize(1000, 600)
root.configure(bg='#00FA9A')
root.geometry('1000x600')
# MAIN BG-- #00FA9A BG-- #93FFE8 #7FFFD4 FG-- #008B8B

# ----------------------------------------------------------------------------------------------------------------------
Label(root, text='Duplicate File Finder', bg='#00FA9A', fg='#008B8B', font=("Arial", 55)).place(x=180, y=20)
Label(root, text=' By Kairav Bhatia ', bg='#00FA9A', fg='#008B8B', font=("Arial", 12)).place(x=620, y=120)

browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda: bro(), font=("Arial", 13), bg='purple', fg='white', width=11, height=2)
browse_text.set('Select Folder')
browse_btn.place(x=480, y=200)

rvar = IntVar()
r1 = Radiobutton(root, state=DISABLED, bg='#7FFFD4', fg='#008B8B', font=("Arial", 13), text='Image', variable=rvar, value=1, command=lambda: radio(1))
r1.place(x=450, y=290)

r2 = Radiobutton(root, state=DISABLED, bg='#7FFFD4', fg='#008B8B', font=("Arial", 13), text='Text (.txt only)', variable=rvar, value=2, command=lambda: radio(2))
r2.place(x=540, y=290)

r3 = Radiobutton(root, state=DISABLED, bg='#7FFFD4', fg='#008B8B', font=("Arial", 13), text='Rich Text (all text files)', variable=rvar, value=3, command=lambda: radio(3))
r3.place(x=685, y=290)

r4 = Radiobutton(root, state=DISABLED, bg='#7FFFD4', fg='#008B8B', font=("Arial", 13), text='Video', variable=rvar, value=4, command=lambda: radio(4))
r4.place(x=450, y=370)

r5 = Radiobutton(root, state=DISABLED, bg='#7FFFD4', fg='#008B8B', font=("Arial", 13), text='Audio', variable=rvar, value=5, command=lambda: radio(5))
r5.place(x=540, y=370)

r6 = Radiobutton(root, state=DISABLED, bg='#7FFFD4', fg='#008B8B', font=("Arial", 13), text='All Types (slower)', variable=rvar, value=6, command=lambda: radio(6))
r6.place(x=685, y=370)


start_btn = Button(root, state=DISABLED, text='Start', command=lambda: start(text, rad), font=("Arial", 13), bg='purple', fg='white', width=11, height=2)
start_btn.place(x=480, y=450)

Label(root, text='STEP #1  Select Folder In which Files are Present ==>', bg='#93FFE8', fg='#008B8B', font=("Arial", 13)).place(x=30, y=210)
Label(root, text='STEP #2  Images, Text or Rich Text Files?? ==>', bg='#93FFE8', fg='#008B8B', font=("Arial", 13)).place(x=30, y=293)
Label(root, text='STEP #3  Start The Process ==>', bg='#93FFE8', fg='#008B8B', font=("Arial", 13)).place(x=30, y=460)

folder_text = StringVar()
Label(root, textvariable=folder_text, bg='#93FFE8', fg='#008B8B', font=("Arial", 13)).place(x=700, y=210)
folder_text.set('Folder Name: ')


# ----------------------------------------------------------------------------------------------------------------------

root.mainloop()
