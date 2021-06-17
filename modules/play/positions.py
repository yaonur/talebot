import pyautogui


def personel_warehouse_coords(filename=None, x=1620, y=620, ):
    if filename:
        x, y = get_position_from_file(filename)
    coords = []
    tempY = y
    x = x - 48
    for i in range(6):
        x = x + 48
        y = tempY - 37
        for i in range(4):
            y = y + 37
            coords.append((x, y))
    return coords


# for coord in personel_warehouse_coords():
#     x,y=coord
#     pyautogui.moveTo(x, y)

def personel_inventory_coords(x=1141, y=944):
    '''
    :arg:takes position to look for in personal
    inventory
    '''

    coords = []
    tempY = y
    x = x - 66
    for i in range(3):
        x += 66
        y = tempY - 47
        print(f'{y} outside')
        for i in range(2):
            y += 47
            print(f'{y} inside')
            coords.append((x, y))
    return coords


def treasure_coords(coord):
    '''
    j
    :param coords:is the coord of the img we looking for
    :return:coords to loop in treasure screen
    '''
    coords = []
    x, y = coord
    x = x - 295

    for i in range(3):
        x += 295
        coords.append(x, y)
    return coords


def get_position_from_file(filename):
    x = int(filename.rsplit('X')[1].rsplit('Y')[0])
    y = int(filename.rsplit('Y')[1].rsplit('.')[0])
    return x, y


def loop_coords(coords, duration):
    for coord in coords:
        pyautogui.moveTo(coord, duration=duration)


def calculate_offset(filename, areaname, confidence, areaW=12, areaH=12):
    '''
    :arg: takes a file name,area for offset to be calulated
    :return:create an array for looping image
    in inventory   slots
    '''
    coords = []
    if areaname == 'personal_inv':
        x, y = get_position_from_file(filename)
        print(x,y)
        x_offset = ( x - 1141 ) % 66
        y_offset = ( y - 944 ) % 47
        print(x_offset,y_offset)
        offset_helper_loop(1141,944,66,47,x_offset,y_offset,confidence,areaW,areaH,3,2,filename)


def offset_helper_loop(x_start, y_start, x_incerement, y_incerement, x_offset, y_offset, confidence, areaW, areaH,rows,colums,filename):
    coords =[]
    x_start=x_start+x_offset-x_incerement
    for i in range(rows):
        x_start+=x_incerement
        temp_y=y_start
        y_start=temp_y+y_offset-y_incerement
        for i in range(colums):
            y_start+=y_incerement
            region = (x_start, y_start, areaW, areaH)
            coords.append([ filename,confidence,areaW,areaH,region ])
    print(coords)
    return coords
