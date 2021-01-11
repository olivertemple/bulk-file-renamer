import os
import time
import PySimpleGUI as sg

layout = [
[sg.Text("Bulk File Renamer")],
[sg.Text("Enter the directory that contains the files"), sg.Input(default_text=os.getcwd(), key='directory'), sg.FolderBrowse()],
[sg.Text("File extension"), sg.Input(key='extension', size = (10,1))],
[sg.Text("File name"), sg.Input(key='name')],
[sg.Text("Naming Scheme:")],
[sg.Button("File0001",key='scheme0'),sg.Button("File1",key='scheme1'),sg.Button("0001File",key='scheme2'),sg.Button("1File",key='scheme3')],
[sg.Text("Start Numer: "), sg.Input(default_text=0, key='s')],
[sg.Button("Execute")]
]

window = sg.Window("Bulk File Renamer", layout,  resizable=True)
scheme0=True
scheme1=False
scheme2=False
scheme3=False
while True:
    event, values = window.read()

    if event== sg.WIN_CLOSED:
        break
    
    if event=='scheme0':
        scheme0=True
        scheme1=False
        scheme2=False
        scheme3=False
    elif event=='scheme1':
        scheme0=False
        scheme1=True
        scheme2=False
        scheme3=False
    elif event=='scheme2':
        scheme0=False
        scheme1=False
        scheme2=True
        scheme3=False
    elif event=='scheme3':
        scheme0=False
        scheme1=False
        scheme2=False
        scheme3=True
    
    
    if event=='Execute':
        if values['s']=='':
            values['s']='0'
        items_change = []
        for item in os.listdir(values['directory']):
            if item.endswith(values['extension']):
                items_change.append(item) 

        
        if scheme0 == True:
            x = len(str(len(items_change)+int(values['s'])))
            for i in range(0, len(items_change)):
                y=x-len(str(i+int(values['s'])))
                zeros = ''
                for a in range(0,y):
                    zeros += '0'
                os.rename(items_change[i],values['name']+zeros+str(i+int(values['s']))+values['extension'])
               
        elif scheme1 == True:
            for i in range(0,len(items_change)):
                os.rename(items_change[i],values['name']+str(i+int(values['s']))+values['extension'])
        elif scheme2 == True:
            x = len(str(len(items_change)+int(values['s'])))
            for i in range(0, len(items_change)):
                y=x-len(str(i+int(values['s'])))
                zeros = ''
                for a in range(0,y):
                    zeros += '0'
                os.rename(items_change[i],zeros+str(i+int(values['s']))+values['name']+values['extension'])
        elif scheme3 == True:
            for i in range(0,len(items_change)):
                os.rename(items_change[i],str(i+int(values['s']))+values['name']+values['extension'])
