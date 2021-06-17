import globalfunctions as gf
import time
import os
def main():
    os.chdir(r'F:/python/talebot')
    if gf.check_image('modules/openshop/personalcheckX1762Y783.png',.95):
        print('personel open')
        pass
    else:
        gf.click(( 1650,1050 ))
        print('personel closed')
        time.sleep(.8)
        pass
    if gf.check_image('modules/openshop/shopcheckX1631Y266.png',.99):
        print('shop open')
        pass
    else:
        gf.click(( 1850,1050 ))
        print('shop close')
        pass

if __name__ == '__main__':
    main()