import osascript
import sys


def runAction(gesture):
    
    if gesture == 'volume up':
        
    
        # get volume settings

        result = osascript.osascript('get volume settings')
        volInfo = result[1].split(',')
        outputVol = volInfo[0].replace('output volume:', '')
        print(outputVol)

        # set volume

        target_volume = 40
        osascript.osascript("set volume output volume {}".format(target_volume))
        
    #elif gesture == 'click':
        
    



        





