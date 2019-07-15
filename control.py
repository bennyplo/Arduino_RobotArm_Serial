import serial

def initialize():
    import serial.tools.list_ports
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if p.description.startswith('Arduino 101 Serial Monitor'):
            break
        
    ser = serial.Serial(p.device, 9600, timeout=1)
    return ser

def command_check(command):
    token_list = command.split()
    if command == 'HELP':
        return 'HELP'
    if command == 'QUIT':
        return 'QUIT'
    elif command == 'SHOW DEGREE':
        return 'SHOW DEGREE'
    elif len(token_list) == 3:
        if token_list[0] not in ['SET', 'ADD', 'MINUS']:
            return 'Command ERROR'
        if token_list[1] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            return 'Command ERROR'
        try:
            int(token_list[2])
        except:
            return 'Command ERROR'
    else:
        return 'Command ERROR'
    return 'VALUE'

def execute(command=None):
    print('Initialising...')
    try:
        ser = initialize()
        print('Initialising Success')
    except:
        print('Initialising Fail')
        ser.close()
        return 
    while True:
        try:
            if command == None:
                command = input('BRobot@genuino101: ')
            else:
                pass
            res = command_check(command)
            if res == 'Command ERROR':
                print('\t' + res)
                print('Try type "HELP"')
                command = None
                continue
            elif res == 'HELP':
                print('\t'+'Available Commands:')
                print('\t'*2+'SHOW DEGREE          : RETURN VALUES OF EACH SERVO')
                print('\t'*2+'HELP                 : HELP LIST')
                print('\t'*2+'QUIT                 : QUIT SCRIPT' )
                print('\t'*2+'SET %SETVO %DEGREE   : SET DEGREE OF A SERVO DIRECTLY; e.g. SET F 45 ')
                print('\t'*2+'ADD %SETVO %DEGREE   : ADD DEGREE OF A SERVO; e.g. ADD F 10 ')
                print('\t'*2+'MINUS %SETVO %DEGREE : MINUS DEGREE OF A SERVO; e.g. MINUS F 10 ')
            elif res == 'QUIT':
                break
            else:
                ser.write(command.encode())    
                s = ser.readlines(40)
                if type(s) == str:
                    print('\t'+s.decode('utf-8'))
                else:
                    for i in range(len(s)):
                        print('\t'+s[i].decode('utf-8'), end='')
                    print()
        except:
            print('ERROR!')
            ser.close()
        command = None
    ser.close()



if __name__ == '__main__':
    execute()
    