import pandas as pd

import tkinter as tk
from tkinter import ttk
from tkinter import *

global iRawPay
iRawPay=0

columnNames = ['BRACKET','START','END']

rngNTG_Admin = [
    ["AO1 Band 1", 51184, 51184],
    ["AO1 Band 2", 51940, 51184],
    ["AO1 Band 3", 52690, 51940],
    ["AO1 Band 4", 53450, 52690],
    ["AO1 Band 5", 54428, 53450],
    ["AO1 Band 6", 55556, 54428],
    ["AO2 Band 1", 56261, 55556],
    ["AO2 Band 2", 57710, 56261],
    ["AO2 Band 3", 58868, 57710],
    ["AO2 Band 4", 60045, 58868],
    ["AO2 Band 5", 61252, 60045],
    ["AO3 Band 1", 62773, 61252],
    ["AO3 Band 2", 63987, 62773],
    ["AO3 Band 3", 65225, 63987],
    ["AO3 Band 4", 67746, 65225],
    ["AO4 Band 1", 71091, 67746],
    ["AO4 Band 2", 72408, 71091],
    ["AO4 Band 3", 74672, 72408],
    ["AO4 Band 4", 76938, 74672],
    ["AO4 Band 5", 79200, 76938],
    ["AO4 Band 6", 81611, 79200],
    ["AO5 Band 1", 84297, 81611],
    ["AO5 Band 2", 86492, 84297],
    ["AO5 Band 3", 88687, 86492],
    ["AO6 Band 1", 92620, 88687],
    ["AO6 Band 2", 96260, 92620],
    ["AO6 Band 3", 99899, 96260],
    ["AO6 Band 4", 103538, 99899],
    ["AO7 Band 1", 109514, 103538],
    ["AO7 Band 2", 113664, 109514],
    ["AO7 Band 3", 117815, 113664],
    ["SAO1 Band 1", 123559, 117815],
    ["SAO1 Band 2", 130369, 123559],
    ["SAO1 Band 3", 138034, 130369],
    ["SAO2 Band 1", 142543, 138034],
    ["SAO2 Band 2", 148815, 142543],
    ["SAO2 Band 3", 155362, 148815],
    ["EO2 Band 1", 158344, 155362],
    ["EO3 Band 1", 169580, 158344]
]



rngNTG_Physical = [
    ["PH1 Band 1", 48734, 48734],
    ["PH1 Band 2", 49225, 48734],
    ["PH1 Band 3", 49711, 49225],
    ["PH2 Band 1", 52146, 49711],
    ["PH2 Band 2", 52634, 52146],
    ["PH2 Band 3", 53220, 52634],
    ["PH3 Band 1", 53220, 53220],
    ["PH3 Band 2", 53803, 53220],
    ["PH3 Band 3", 54430, 53803],
    ["PH4 Band 1", 55954, 54430],
    ["PH4 Band 2", 56803, 55954],
    ["PH4 Band 3", 57622, 56803],
    ["PH5 Band 1", 58451, 57622],
    ["PH5 Band 2", 59219, 58451],
    ["PH5 Band 3", 59985, 59219],
    ["PH6 Band 1", 62746, 59985],
    ["PH6 Band 2", 63847, 62746],
    ["PH6 Band 3", 65028, 63847],
    ["PH7 Band 1", 67918, 65028],
    ["PH7 Band 2", 69177, 67918],
    ["PH7 Band 3", 70495, 69177],
    ["PH8 Band 1", 73233, 70495],
    ["PH8 Band 2", 74630, 73233],
    ["PH8 Band 3", 76107, 74630],
    ["PH9 Band 1", 79774, 76107],
    ["PH9 Band 2", 81553, 79774],
    ["PH9 Band 3", 83579, 81553]

]

rngNTG_Proffesional = [
    ["P1 Band 1", 64904, 64904],
    ["P1 Band 2", 67305, 64904],
    ["P1 Band 3", 69795, 67305],
    ["P1 Band 4", 72377, 69795],
    ["P1 Band 5", 75057, 72377],
    ["P1 Band 6", 77835, 75057],
    ["P1 Band 7", 80715, 77835],
    ["P1 Band 8", 83700, 80715],
    ["P2 Band 1", 86204, 83700],
    ["P2 Band 2", 89395, 86204],
    ["P2 Band 3", 92703, 89395],
    ["P2 Band 4", 96133, 92703],
    ["P2 Band 5", 99687, 96133],
    ["P2 Band 6", 103377, 99687],
    ["P3 Band 1", 106568, 103377],
    ["P3 Band 2", 110512, 106568],
    ["P3 Band 3", 114598, 110512],
    ["P3 Band 4", 119351, 114598],
    ["SP1 Band 1", 123559, 119351],
    ["SP1 Band 2", 130369, 123559],
    ["SP1 Band 3", 138034, 130369],
    ["SP2 Band 1", 142543, 138034],
    ["SP2 Band 2", 148815, 142543],
    ["SP2 Band 3", 15536, 148815]

]

rngNTG_Technical = [
    ["T1 Band 1", 52728, 52728],
    ["T1 Band 2", 53916, 52728],
    ["T1 Band 3", 55099, 53916],
    ["T1 Band 4", 56285, 55099],
    ["T1 Band 5", 57512, 56285],
    ["T1 Band 6", 58753, 57512],
    ["T1 Band 7", 60020, 58753],
    ["T1 Band 8", 61330, 60020],
    ["T1 Band 9", 62697, 61330],
    ["Trainee Technical Officer Band 1", 55167, 55167],
    ["Trainee Technical Officer Band 2", 57702, 55167],
    ["Trainee Technical Officer Band 3", 60872, 57702],
    ["T2 Band 1", 63408, 60872],
    ["T2 Band 2", 64795, 63408],
    ["T2 Band 3", 66175, 64795],
    ["T2 Band 4", 67601, 66175],
    ["T2 Band 5", 69022, 67601],
    ["T2 Band 6", 70451, 69022],
    ["T2 Band 7", 71885, 70451],
    ["T3 Band 1", 73575, 71885],
    ["T3 Band 2", 75927, 73575],
    ["T3 Band 3", 78281, 75927],
    ["T3 Band 4", 79774, 78281],
    ["T3 Band 5", 81565, 79774],
    ["T3 Band 6", 83579, 81565],
    ["T4 Band 1", 85637, 83579],
    ["T4 Band 2", 88492, 85637],
    ["T4 Band 3", 91355, 88492],
    ["T4 Band 1", 94223, 91355],
    ["T5 Band 2", 97083, 94223],
    ["T5 Band 3", 99950, 97083],
    ["T5 Band 4", 102813, 99950],
    ["T5 Band 5", 105770, 102813],
    ["T6 Band 1", 109101, 105770],
    ["T6 Band 2", 111664, 109101],
    ["T6 Band 3", 114227, 111664]
]

rngCDU_HEW = [
    ["HEW 1.3 Band ", 50896, 50896],
    ["HEW 2.3 Band ", 53823, 50896],
    ["HEW 3.5 Band ", 62131, 53823],
    ["HEW 4.1 Band ", 62661, 62131],
    ["HEW 4.2 Band ", 63977, 62661],
    ["HEW 4.3 Band ", 65294, 63977],
    ["HEW 4.4 Band ", 66615, 65294],
    ["HEW 5.1 Band ", 67931, 66615],
    ["HEW 5.2 Band ", 70567, 67931],
    ["HEW 5.3 Band ", 73204, 70567],
    ["HEW 5.4 Band ", 75838, 73204],
    ["HEW 5.5 Band ", 78478, 75838],
    ["HEW 6.1 Band ", 80063, 78478],
    ["HEW 6.2 Band ", 81376, 80063],
    ["HEW 6.3 Band ", 82696, 81376],
    ["HEW 6.4 Band ", 84018, 82696],
    ["HEW 6.5 Band ", 85330, 84018],
    ["HEW 7.1 Band ", 86390, 85330],
    ["HEW 7.2 Band ", 88494, 86390],
    ["HEW 7.3 Band ", 90605, 88494],
    ["HEW 7.4 Band ", 92716, 90605],
    ["HEW 7.5 Band ", 94829, 92716],
    ["HEW 8.1 Band ", 96937, 94829],
    ["HEW 8.2 Band ", 100096, 96937],
    ["HEW 8.3 Band ", 103262, 100096],
    ["HEW 8.4 Band ", 106430, 103262],
    ["HEW 8.5 Band ", 109590, 106430],
    ["HEW 9.1 Band ", 112754, 109590],
    ["HEW 9.2 Band ", 114333, 112754],
    ["HEW 9.3 Band ", 115919, 114333],
    ["HEW 9.4 Band ", 117495, 115919],
    ["HEW 9.5 Band ", 119084, 117495],
    ["HEW 10.1 Band ", 119132, 119084],
    ["HEW 10.2 Band ", 122405, 119132],
    ["HEW 10.3 Band ", 125675, 122405],
    ["HEW 10.4 Band ", 128946, 125675],
    ["HEW 10.5 Band ", 132217, 128946]

]
# Australian Resisdent Tax rate
rngTAX_INCOME1 = [
    ["Bracket1 ", 0, 18200, 0.0, 0],
    ["Bracket1 ", 18201, 45000, 19.0, 0],
    ["Bracket1 ", 45001, 120000, 32.5, 5092],
    ["Bracket1 ", 120001, 180000, 37.0, 29467],
    ["Bracket1 ", 180001, 1000000, 45.0, 51667]
]
# foreign Worker
rngTAX_INCOME2 = [
    ["Bracket1 ", 0, 120000, 32.5, 0],
    ["Bracket2 ", 120001, 180000, 37, 39000],
    ["Bracket3 ", 180001, 1000000, 45.0, 61200]
]
# Working holiday maker
rngTAX_INCOME3 = [
    ["Bracket1 ", 0, 45000, 15, 0],
    ["Bracket2 ", 45001, 120000, 32.5, 6750],
    ["Bracket3 ", 120001, 180000, 37.0, 31125],
    ["Bracket4 ", 180001, 1000000, 45.0, 53325]
]





def getIncomeAmount():
    userInput=txtPayOffer.get()
    return userInput

def getSuperPercent():
    userInput = txtSuper.get()
    return userInput

#The combo box values
def getTaxStatus():
    userInput =comboTaxStatus.get()
    return userInput






# this is the function called when the button is clicked
def btnProcessCode():
    global   iRawPay
    curTaxRate = 0
    curExtra = 0

    iRawPay = getIncomeAmount()
    if getSuperPercent() == '':
        iSuperPercent = 0.10
    else:
        iSuperPercent = getSuperPercent()
        iSuperPercent = float(iSuperPercent) / 100



    df = pd.DataFrame(rngTAX_INCOME1)
    df.columns = ['BRACKET', 'START', 'END', 'TAXRATE', 'EXTRA']
    alpha = df.query('START <=' + str(iRawPay) + ' and END >= ' + str(iRawPay))
    curTaxRate = alpha["TAXRATE"] / 100
    curExtra = alpha["EXTRA"]
    iTaxToPay = (float(iRawPay) * float(curTaxRate)) + float(curExtra)
    lsuperAmount = float(iRawPay) * float(iSuperPercent  )

    lTakeHomePay=(float(iRawPay)-iTaxToPay)-lsuperAmount
    print('Based on a income of $'+str(iRawPay)+ ' you have tax of $'+str(iTaxToPay))
    print('Your super will be '+str(lsuperAmount))
    print('Your Take Homepay will be ' + str(lTakeHomePay))

    print('Your Pay EBA comparisons for that pay level are:')

    df = pd.DataFrame(rngNTG_Admin)
    df.columns = ['BAND', 'Top', 'Bottom']
    Admin=  df[(df.Top >= float(iRawPay)) &(df.Bottom <= float(iRawPay)) ]
    print('NTG Admin Stream Equivelent')
    print(Admin.to_string())



    df = pd.DataFrame(rngNTG_Physical)
    df.columns = ['BAND', 'Top', 'Bottom']
    oPHYS =  df[(df.Top >= float(iRawPay)) &(df.Bottom <= float(iRawPay)) ]
    print('NTG Physical Stream Equivelent')
    print(oPHYS.to_string())

    df = pd.DataFrame(rngNTG_Proffesional)
    df.columns = ['BAND', 'Top', 'Bottom']
    oProf = df[(df.Top >= float(iRawPay)) &(df.Bottom <= float(iRawPay)) ]
    print('NTG Proffesional Stream Equivelent')
    print(oProf.to_string())

    df = pd.DataFrame(rngNTG_Technical)
    df.columns = ['BAND', 'Top', 'Bottom']
    oTech =  df[(df.Top >= float(iRawPay)) &(df.Bottom <= float(iRawPay)) ]
    print('NTG Technial Stream Equivelent')
    print(oTech.to_string())

    df = pd.DataFrame(rngCDU_HEW)
    df.columns = ['BAND', 'Top', 'Bottom']
    oCDU = df[(df.Top >= float(iRawPay)) &(df.Bottom <= float(iRawPay)) ]
    print('CDU HEW Stream Equivelent')
    print(oCDU.to_string())

root = Tk()

# This is the section of code which creates the main window
root.geometry('340x400')
root.configure(background='#F0F8FF')
root.title('Nicola Matarazzo s901057 Assignment 2 Part 2 HIT137')

txtPayOffer=Entry(root)
txtPayOffer.place(x=140, y=26)
Label(root,text="Pay Offer").place(x=10, y=26)



 


# This is the section of code which creates a text input box
txtSuper=Entry(root)
txtSuper.place(x=140, y=166)
Label(root,text="Super Amount %").place(x=10, y=166)




# This is the section of code which creates a button
Button(root, text='Submit', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnProcessCode).place(x=30, y=280)

root.mainloop()




