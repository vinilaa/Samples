#! py -3
#pySelecFinder.py - A simple webscrapping tool made in python to extract elements from html. This is not a pro work, i made it as a small project to improve my skills with python. Since im a beginner self taught programmer, this is a way to improve my skills.
import os,sys,pyperclip,requests,bs4,webbrowser
#defs################################################################################################################################################################
def checkCsss():
    while True:
        menuHead()
        selector=input(str('\tEnter CSS Selector(A brief explanation of what is a CSS Selector and how to compile then can be found in:https://www.w3schools.com/cssref/css_selectors.asp)\n\tThe code is supose to search for a CSS selector. If the user search for a bad CSSS, blame the user not the code.\n\tInput: '))
        if selector == '':
            print('\tBlank Selector. Reenter.')
            continue
        elif bool(soupOb.select(selector)):
            break
        else:
            print('\tNo results found for '+selector+'.')
            continue
    return str(selector)    
def menuHead():
    os.system('cls')
    print('\tUrl: '+str(reqOb.url)+' | Status: '+str(reqOb.status_code)+'\n')
def checkReq():
    while True:
        inpReq=input(str('\tEnter the url of the site to be scrapped(it must begin with https://) or enter \'-p\' to copy a link from your clipboard: '))
        if inpReq == '-p':
            inpReq=pyperclip.paste()
        if inpReq.startswith(r'www.'):
            inpReq='https://'+inpReq
        if not inpReq.startswith(r'https://'):
            os.system('cls')
            print('\t'+inpReq+' is not a valid link.')
            continue
        else:
            try:
                requests.get(inpReq).raise_for_status()
            except Exception as err:
                os.system('cls')
                print('\tSomething is not right: '+str(err))
                continue
            else:
                print('\tConnection granted.')
                break
    return inpReq
def saver():
    os.system('cls')
    while True:
        print('\tSave Menu | Current Working Directory(cwd):'+os.getcwd()+'\n\tLines:')
        for i in range(len(parseOb)):
                print('\t'+str(i).ljust(189,'-')+'\n\t'+str(parseOb[i]))
        print('\t'+'-'*189)
        print('\tMenu:\n\t\'c\' to change the cwd\n\t\'s\' to save the results in a .txt file on the cwd\n\t\'e\' to return to menu')
        inpSaver=input('\tInput:')
        if inpSaver == 'c':
            while True:
                inpPath=input(str('\tEnter the path to be the new cwd(it can be realtive or absolute); enter \'-p\' to copy it from your clipboard; or \'e\' to abort changing the cwd: '))
                if inpPath == '-p':
                    inpPath=pyperclip.paste()
                elif inpPath == 'e':
                    break
                if os.path.exists(inpPath):
                    os.chdir(inpPath)
                    break
                else:
                    print('\t'+inpPath+' is not a valid path.')
                    continue
            del inpPath
            os.system('cls')
            continue
        elif inpSaver == 's':
            try:
                fileOb=open(input(str('\tInsert the name of the .txt file(without the .txt):'))+'.txt','w')
                for i in range(len(parseOb)):
                    fileOb.write(str(parseOb[i])+'\n')
                fileOb.close()
            except Exception as err:
                print('Something is not right:'+str(err))
            os.system('cls')
            continue
        elif inpSaver == 'e':
            os.system('cls')
            break
        else:
            print('\t\''+inpSaver+'\' is not a valid input.')
            continue
#body################################################################################################################################################################
menuOp=('e','s','o','re','css')
while True:
    os.system('cls')
    reqOb=requests.get(checkReq())
    soupOb=bs4.BeautifulSoup(reqOb.text)
####Select menu######################################################################################################################################################    
    while True:
        parseOb=soupOb.select(checkCsss())
        while True:
            menuHead()
            print('\tResults:')
            for i in range(len(parseOb)):
                print('\t'+str(i).ljust(189,'-')+'\n\t'+str(parseOb[i]))
            print('\t'+'-'*189)
############Menu options###########################################################################################################################################
            print('\n\tMenu:\n\t\'e\' to exit\n\t\'re\' to search for another domain\n\t\'css\' to search for another CSS Selector\n\t\'o\' to open the current URL on the browser\n\t\'s\' to save all the results on a .txt\n\tOr select one of the element\'s index to send it to the clipboard.')
            menuInp=input(str('\n\tInput:'))
############Options out of index###################################################################################################################################
            if menuInp in menuOp:
                if menuInp == 'e':
                    os.system('cls')
                    sys.exit('Thanks for using my code ^^\nIf you are looking for a intern, you can contact me in vinicius.l.a@live.com or in my github profile https://github.com/vinilaa')
                elif menuInp == 'css':
                    re=False
                    break
                elif menuInp == 're':
                    re=True
                    break
                elif menuInp == 'o':
                    webbrowser.open(str(reqOb.url))
                    continue
                elif menuInp == 's':
                    saver()
                    continue
############Index options############################################################################################################################################
            elif menuInp.isdigit():
                if int(menuInp) <= (len(parseOb)-1):
                    if input(str('\tSend \''+str(parseOb[int(menuInp)])+'\' to the clipboard?(y/n)').lower()) == 'y':
                        pyperclip.copy(str(parseOb[int(menuInp)]))
                        input('\tDone ;)')
                        continue
                    else:
                        continue
                else:
                    input('\tOut of index')
                    continue
#################################################################################################################################################################            
            else:
                print('\t\''+menuInp+'\' is not a valid option.')
                input()
                continue
        if re == True:
            re == False
            break
        else:
            continue
                
            
            
        

            





