import osascript
import pyautogui
import sys
import keyboard


keyboard.press_and_release('shift+s, spaceS ')

def runAction(gesture):
    
    if gesture == 'volume up':
        
    
        # get volume settings

        result = osascript.osascript('get volume settings')
        volInfo = result[1].split(',')
        outputVol = volInfo[0].replace('output volume:', '')
        print(outputVol)

        # set volume

        target_volume = outputVol + 20
        osascript.osascript("set volume output volume {}".format(target_volume))
        
    #elif gesture == 'click':

    
    
    
    #jsdbcdhjsbchdjsbbhdshddhxs achxsd bchdsbcbh
    #jxdbschkbsdkchbdsbcljdsb
    #hjcxdbscjkbsdjkcbdsjbcjbdsckjdsbjkc
    #hcsdbchbdshkcbjksd
    #xchbdsjchbdsjhbcjds
    

    



        

#jsdbcdhjsbchdjsbbhdshddhxs achxsd bchdsbcbh
    #jxdbschkbsdkchbdsbcljdsb
    #hjcxdbscjkbsdjkcbdsjbcjbdsckjdsbjkc
    #hcsdbchbdshkcbjksd
    #xchbdsjchbdsjhbcjds
    #jsdbcdhjsbchdjsbbhdshddhxs achxsd bchdsbcbh
    #jxdbschkbsdkchbdsbcljdsb
    #hjcxdbscjkbsdjkcbdsjbcjbdsckjdsbjkc
    #hcsdbchbdshkcbjksd
    #xchbdsjchbdsjhbcjds
    #jsdbcdhjsbchdjsbbhdshddhxs achxsd bchdsbcbh
    #jxdbschkbsdkchbdsbcljdsb
    #hjcxdbscjkbsdjkcbdsjbcjbdsckjdsbjkc
    #hcsdbchbdshkcbjksd
    #xchbdsjchbdsjhbcjds
    #jsdbcdhjsbchdjsbbhdshddhxs achxsd bchdsbcbh
    #jxdbschkbsdkchbdsbcljdsb
    #hjcxdbscjkbsdjkcbdsjbcjbdsckjdsbjkc
    #hcsdbchbdshkcbjksd
    #xchbdsjchbdsjhbcjds
    #jsdbcdhjsbchdjsbbhdshddhxs achxsd bchdsbcbh
    #jxdbschkbsdkchbdsbcljdsb
    #hjcxdbscjkbsdjkcbdsjbcjbdsckjdsbjkc
    #hcsdbchbdshkcbjksd
    #xchbdsjchbdsjhbcjds
    #jsdbcdhjsbchdjsbbhdshddhxs achxsd bchdsbcbh
    #jxdbschkbsdkchbdsbcljdsb
    #hjcxdbscjkbsdjkcbdsjbcjbdsckjdsbjkc
    #hcsdbchbdshkcbjksd
    #xchbdsjchbdsjhbcjds
    #jsdbcdhjsbchdjsbbhdshddhxs achxsd bchdsbcbh
    #jxdbschkbsdkchbdsbcljdsb
    #hjcxdbscjkbsdjkcbdsjbcjbdsckjdsbjkc
    #hcsdbchbdshkcbjksd
    #xchbdsjchbdsjhbcjds
    #jsdbcdhjsbchdjsbbhdshddhxs achxsd bchdsbcbh
    #jxdbschkbsdkchbdsbcljdsb
    #hjcxdbscjkbsdjkcbdsjbcjbdsckjdsbjkc
    #hcsdbchbdshkcbjksd
    #xchbdsjchbdsjhbcjds
    #jsdbcdhjsbchdjsbbhdshddhxs achxsd bchdsbcbh
    #jxdbschkbsdkchbdsbcljdsb
    #hjcxdbscjkbsdjkcbdsjbcjbdsckjdsbjkc
    #hcsdbchbdshkcbjksd
    #xchbdsjchbdsjhbcjds
    



