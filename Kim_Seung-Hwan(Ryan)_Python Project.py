#Kim Seung-Hwan(Ryan) - Python Project

#Importing and using Python Module
import pandas as pd

sunsetFileName = 'C:/Users/ryank/Desktop/Fall 2022/Programming with Python (ISGB-7943-003)/Homework/Homework IX Part I - Proposal/data.csv'
reservationFileName = 'C:/Users/ryank/Desktop/Fall 2022/Programming with Python (ISGB-7943-003)/Homework/Homework IX Part I - Proposal/dataReservationStatus.csv'

#Using Python Module - pandas for showing Data Frame
sunsetDataFrame = pd.read_csv(sunsetFileName)
print(sunsetDataFrame)

#Data types, such as strings and integers
brideFirstName = input('What is first name of the bride?\n>>')
brideLastName = input('What is last name of the bride?\n>>')
groomFirstName = input('What is first name of the groom?\n>>')
groomLastName = input('What is last name of the groom?\n>>')
weddingDate = input('When is your wedding date in the year of 2022? (Note: Should enter in format of 1/1/2022 (not 01/01/2022))\n>>')
#Error handling and debugging (for handling ValueError)
weddingTimeConfirmed = 'n'
#Control flow via while loop used for handling the error
while weddingTimeConfirmed != 'y':
    try:
        weddingTime = input('What time does your wedding start? (Note: Should enter in format of 5:30:00PM)\n>>')
        adjustedWeddingTime = int(weddingTime.replace(':','').replace(' ','').replace('PM','').replace('pm','').replace('pM','').replace('Pm',''))
        weddingTimeConfirmed = 'y'
    except ValueError:
        print('"The photo studio only operates from 1:00:00PM to 8:00:00PM. So, if you mistype it, please enter a valid wedding time within the PM hours."')
        print()
#Error handling and debugging (for handling ValueError)
contractHoursConfirmed = 'n'
#Control flow via while loop used for handling the error
while contractHoursConfirmed != 'y':
    try:
        contractHours = int(input('How many hour(s) do you want to contract with my photo studio on your wedding date?\n>>'))
        contractHoursConfirmed = 'y'
    except ValueError:
        print('"Please enter a positive integer value for the number of hour(s) of the contract with my photo studio."')
        print()

#Python function and parameters, both defining and calling
def combineBrideGroom(brideFirstName, brideLastName, groomFirstName, groomLastName):
    a = brideFirstName + ' ' + brideLastName + '  ' + '*' + '  ' + groomFirstName + ' ' + groomLastName
    return a

#Error handling and debugging (for handling PermissionError)
try:
    #Reading and appending to files
    with open(sunsetFileName, 'r', encoding = 'utf8') as sunsetFile, open(reservationFileName, 'a', encoding = 'utf8') as reservationFile:
        line = sunsetFile.readline().replace('\n','')
        line = sunsetFile.readline().replace('\n','')
        #Control flow via while loop used for reading and appending to files
        while line != '':
            line = line.replace('\n', '')
            #Data structure - lists used
            lineList = line.split(',')
            date = lineList[0]
            sunrise = lineList[1]
            sunrise = sunrise.replace(' ','')
            sunset = lineList[2]
            sunset = sunset.replace(' ','')
            dayLength = lineList[3]
            adjustedSunset = int(sunset.replace(':','').replace(' ','').replace('PM','').replace('pm','').replace('pM','').replace('Pm',''))
            adjustedContractHours = contractHours * 10000
            #Python function and parameters, called
            brideGroom = combineBrideGroom(brideFirstName, brideLastName, groomFirstName, groomLastName)
            if weddingDate == date:
                #Conditional logic, if statement
                if adjustedSunset - adjustedWeddingTime > adjustedContractHours:
                    print('Your wedding starts too early to take sunset photo shoots (based on your desired contract hour(s)).')
                    print('<', 'Your Wedding Time:', weddingTime, '/', 'Sunset Time:', sunset, '/', 'Contract Hour(s):', contractHours, '>')
                elif adjustedSunset - adjustedWeddingTime <= adjustedContractHours and adjustedSunset - adjustedWeddingTime > 0:
                    print('Great! I am glad to have the opportunity to take the most beautiful and gorgeous sunset photo shoots for your weeding.')
                    print('< Time for taking the sunset photo shoots is', sunset, '>')
                    #Writing to file
                    reservationFile.write(date + ',' + weddingTime + ',' + sunset + ',' + str(contractHours) + ',' + brideGroom + '\n')
                else:
                    print('Your wedding starts too late to take sunset photo shoots (based on your desired contract hour(s)).')
                    print('<', 'Your Wedding Time:', weddingTime, '/', 'Sunset Time:', sunset, '/', 'Contract Hour(s):', contractHours, '>')
            line = sunsetFile.readline().replace('\n','')
except PermissionError:
    print('"Please close the csv data file(dataReservationStatus.csv) to avoid this conflict and save the record successfully."')
print()

#Using Python Module - pandas for showing Data Frame
reservationDataFrame = pd.read_csv(reservationFileName)
print(reservationDataFrame)
