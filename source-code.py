#Importing Stuff
from ctypes import Structure, c_long, byref, windll
import math
import time
import os


#Variables
slp = 0.5 #Time Between Choosing Charcters(Higher: More Secured, Lower: Faster)
n = 1 #For While Loop To Make Codes As Long As The Message
key = [] #Key For Decryptin The Message
used = [] #Charcters Choosen By Cursor Move For Encryption
final = {} #Final Dic For Main Message & Encrypted Message

print("""\n\n=-=-=-=-=-=-=-=-=-=-=-=-= HEELO! =-=-=-=-=-=-=-=-=-=-=-=-=\n""")


message = input('Enter Your Message For Encryption: \n>>') #Main Message


print('\nEncrypting... Wait')


#Cursor Position Class
class Point(Structure):
    _fields_ = [('x', c_long), ('y', c_long)]


def Get():
    ps = Point()
    windll.user32.GetCursorPos(byref(ps))
    
    final_pos = math.sqrt((ps.x)**2 + (ps.y)**2)
    return final_pos


#A Functoin To Overwrite Textes ( 0<r<10)
def Overwrite(r):
    #Overwrite Per Second
    r = int(r)
    
    for i in range(r):
        print(r, end='\r')
        time.sleep(1)
        print(r-1, end = '\r')
        r -= 1



#Encryption By Cursor Position
while (len(message) >= n):
    temp = int(Get())
    n += 1

    
    if (temp <  16.6  and temp >=  0.0 ):

        let = '!'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  16.6  and temp >=  0.0 ):

        used.append('!')


    if (temp <  33.2  and temp >=  16.6 ):

        let = '"'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  33.2  and temp >=  16.6 ):

        used.append('"')


    if (temp <  49.800000000000004  and temp >=  33.2 ):

        let = '#'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  49.800000000000004  and temp >=  33.2 ):

        used.append('#')


    if (temp <  66.4  and temp >=  49.800000000000004 ):

        let = '$'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  66.4  and temp >=  49.800000000000004 ):

        used.append('$')


    if (temp <  83.0  and temp >=  66.4 ):

        let = '%'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  83.0  and temp >=  66.4 ):

        used.append('%')


    if (temp <  99.60000000000001  and temp >=  83.0 ):

        let = '&'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  99.60000000000001  and temp >=  83.0 ):

        used.append('&')


    if (temp <  116.20000000000002  and temp >=  99.60000000000001 ):

        let = "'"
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  116.20000000000002  and temp >=  99.60000000000001 ):

        used.append("'")


    if (temp <  132.8  and temp >=  116.20000000000002 ):

        let = '('
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  132.8  and temp >=  116.20000000000002 ):

        used.append('(')


    if (temp <  149.4  and temp >=  132.8 ):

        let = ')'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  149.4  and temp >=  132.8 ):

        used.append(')')


    if (temp <  166.0  and temp >=  149.4 ):

        let = '*'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  166.0  and temp >=  149.4 ):

        used.append('*')


    if (temp <  182.60000000000002  and temp >=  166.0 ):

        let = '+'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  182.60000000000002  and temp >=  166.0 ):

        used.append('+')


    if (temp <  199.20000000000002  and temp >=  182.60000000000002 ):

        let = ','
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  199.20000000000002  and temp >=  182.60000000000002 ):

        used.append(',')


    if (temp <  215.8  and temp >=  199.20000000000002 ):

        let = '-'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  215.8  and temp >=  199.20000000000002 ):

        used.append('-')


    if (temp <  232.40000000000003  and temp >=  215.8 ):

        let = '.'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  232.40000000000003  and temp >=  215.8 ):

        used.append('.')


    if (temp <  249.00000000000003  and temp >=  232.40000000000003 ):

        let = '//'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  249.00000000000003  and temp >=  232.40000000000003 ):

        used.append('//')


    if (temp <  265.6  and temp >=  249.00000000000003 ):

        let = '0'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  265.6  and temp >=  249.00000000000003 ):

        used.append('0')


    if (temp <  282.20000000000005  and temp >=  265.6 ):

        let = '1'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  282.20000000000005  and temp >=  265.6 ):

        used.append('1')


    if (temp <  298.8  and temp >=  282.20000000000005 ):

        let = '2'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  298.8  and temp >=  282.20000000000005 ):

        used.append('2')


    if (temp <  315.40000000000003  and temp >=  298.8 ):

        let = '3'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  315.40000000000003  and temp >=  298.8 ):

        used.append('3')


    if (temp <  332.0  and temp >=  315.40000000000003 ):

        let = '4'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  332.0  and temp >=  315.40000000000003 ):

        used.append('4')


    if (temp <  348.6  and temp >=  332.0 ):

        let = '5'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  348.6  and temp >=  332.0 ):

        used.append('5')


    if (temp <  365.20000000000005  and temp >=  348.6 ):

        let = '6'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  365.20000000000005  and temp >=  348.6 ):

        used.append('6')


    if (temp <  381.8  and temp >=  365.20000000000005 ):

        let = '7'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  381.8  and temp >=  365.20000000000005 ):

        used.append('7')


    if (temp <  398.40000000000003  and temp >=  381.8 ):

        let = '8'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  398.40000000000003  and temp >=  381.8 ):

        used.append('8')


    if (temp <  415.00000000000006  and temp >=  398.40000000000003 ):

        let = '9'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  415.00000000000006  and temp >=  398.40000000000003 ):

        used.append('9')


    if (temp <  431.6  and temp >=  415.00000000000006 ):

        let = ':'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  431.6  and temp >=  415.00000000000006 ):

        used.append(':')


    if (temp <  448.20000000000005  and temp >=  431.6 ):

        let = ';'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  448.20000000000005  and temp >=  431.6 ):

        used.append(';')


    if (temp <  464.80000000000007  and temp >=  448.20000000000005 ):

        let = '<'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  464.80000000000007  and temp >=  448.20000000000005 ):

        used.append('<')


    if (temp <  481.40000000000003  and temp >=  464.80000000000007 ):

        let = '='
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  481.40000000000003  and temp >=  464.80000000000007 ):

        used.append('=')


    if (temp <  498.00000000000006  and temp >=  481.40000000000003 ):

        let = '>'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  498.00000000000006  and temp >=  481.40000000000003 ):

        used.append('>')


    if (temp <  514.6  and temp >=  498.00000000000006 ):

        let = '?'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  514.6  and temp >=  498.00000000000006 ):

        used.append('?')


    if (temp <  531.2  and temp >=  514.6 ):

        let = '@'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  531.2  and temp >=  514.6 ):

        used.append('@')


    if (temp <  547.8000000000001  and temp >=  531.2 ):

        let = 'A'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  547.8000000000001  and temp >=  531.2 ):

        used.append('A')


    if (temp <  564.4000000000001  and temp >=  547.8000000000001 ):

        let = 'B'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  564.4000000000001  and temp >=  547.8000000000001 ):

        used.append('B')


    if (temp <  581.0  and temp >=  564.4000000000001 ):

        let = 'C'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  581.0  and temp >=  564.4000000000001 ):

        used.append('C')


    if (temp <  597.6  and temp >=  581.0 ):

        let = 'D'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  597.6  and temp >=  581.0 ):

        used.append('D')


    if (temp <  614.2  and temp >=  597.6 ):

        let = 'E'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  614.2  and temp >=  597.6 ):

        used.append('E')


    if (temp <  630.8000000000001  and temp >=  614.2 ):

        let = 'F'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  630.8000000000001  and temp >=  614.2 ):

        used.append('F')


    if (temp <  647.4000000000001  and temp >=  630.8000000000001 ):

        let = 'G'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  647.4000000000001  and temp >=  630.8000000000001 ):

        used.append('G')


    if (temp <  664.0  and temp >=  647.4000000000001 ):

        let = 'H'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  664.0  and temp >=  647.4000000000001 ):

        used.append('H')


    if (temp <  680.6  and temp >=  664.0 ):

        let = 'I'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  680.6  and temp >=  664.0 ):

        used.append('I')


    if (temp <  697.2  and temp >=  680.6 ):

        let = 'J'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  697.2  and temp >=  680.6 ):

        used.append('J')


    if (temp <  713.8000000000001  and temp >=  697.2 ):

        let = 'K'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  713.8000000000001  and temp >=  697.2 ):

        used.append('K')


    if (temp <  730.4000000000001  and temp >=  713.8000000000001 ):

        let = 'L'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  730.4000000000001  and temp >=  713.8000000000001 ):

        used.append('L')


    if (temp <  747.0000000000001  and temp >=  730.4000000000001 ):

        let = 'M'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  747.0000000000001  and temp >=  730.4000000000001 ):

        used.append('M')


    if (temp <  763.6  and temp >=  747.0000000000001 ):

        let = 'N'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  763.6  and temp >=  747.0000000000001 ):

        used.append('N')


    if (temp <  780.2  and temp >=  763.6 ):

        let = 'O'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  780.2  and temp >=  763.6 ):

        used.append('O')


    if (temp <  796.8000000000001  and temp >=  780.2 ):

        let = 'P'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  796.8000000000001  and temp >=  780.2 ):

        used.append('P')


    if (temp <  813.4000000000001  and temp >=  796.8000000000001 ):

        let = 'Q'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  813.4000000000001  and temp >=  796.8000000000001 ):

        used.append('Q')


    if (temp <  830.0000000000001  and temp >=  813.4000000000001 ):

        let = 'R'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  830.0000000000001  and temp >=  813.4000000000001 ):

        used.append('R')


    if (temp <  846.6  and temp >=  830.0000000000001 ):

        let = 'S'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  846.6  and temp >=  830.0000000000001 ):

        used.append('S')


    if (temp <  863.2  and temp >=  846.6 ):

        let = 'T'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  863.2  and temp >=  846.6 ):

        used.append('T')


    if (temp <  879.8000000000001  and temp >=  863.2 ):

        let = 'U'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  879.8000000000001  and temp >=  863.2 ):

        used.append('U')


    if (temp <  896.4000000000001  and temp >=  879.8000000000001 ):

        let = 'V'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  896.4000000000001  and temp >=  879.8000000000001 ):

        used.append('V')


    if (temp <  913.0000000000001  and temp >=  896.4000000000001 ):

        let = 'W'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  913.0000000000001  and temp >=  896.4000000000001 ):

        used.append('W')


    if (temp <  929.6000000000001  and temp >=  913.0000000000001 ):

        let = 'X'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  929.6000000000001  and temp >=  913.0000000000001 ):

        used.append('X')


    if (temp <  946.2  and temp >=  929.6000000000001 ):

        let = 'Y'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  946.2  and temp >=  929.6000000000001 ):

        used.append('Y')


    if (temp <  962.8000000000001  and temp >=  946.2 ):

        let = 'Z'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  962.8000000000001  and temp >=  946.2 ):

        used.append('Z')


    if (temp <  979.4000000000001  and temp >=  962.8000000000001 ):

        let = '['
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  979.4000000000001  and temp >=  962.8000000000001 ):

        used.append('[')


    if (temp <  996.0000000000001  and temp >=  979.4000000000001 ):

        let = '\\'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  996.0000000000001  and temp >=  979.4000000000001 ):

        used.append('\\')


    if (temp <  1012.6000000000001  and temp >=  996.0000000000001 ):

        let = ']'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1012.6000000000001  and temp >=  996.0000000000001 ):

        used.append(']')


    if (temp <  1029.2  and temp >=  1012.6000000000001 ):

        let = '^'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1029.2  and temp >=  1012.6000000000001 ):

        used.append('^')
        

    if (temp <  1045.8000000000002  and temp >=  1029.2 ):

        let = '_'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1045.8000000000002  and temp >=  1029.2 ):

        used.append('_')


    if (temp <  1062.4  and temp >=  1045.8000000000002 ):

        let = '`'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1062.4  and temp >=  1045.8000000000002 ):

        used.append('`')


    if (temp <  1079.0  and temp >=  1062.4 ):

        let = 'a'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1079.0  and temp >=  1062.4 ):

        used.append('a')


    if (temp <  1095.6000000000001  and temp >=  1079.0 ):

        let = '{b'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1095.6000000000001  and temp >=  1079.0 ):

        used.append('b')


    if (temp <  1112.2  and temp >=  1095.6000000000001 ):

        let = 'c'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1112.2  and temp >=  1095.6000000000001 ):

        used.append('c')


    if (temp <  1128.8000000000002  and temp >=  1112.2 ):

        let = 'd'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1128.8000000000002  and temp >=  1112.2 ):

        used.append('d')


    if (temp <  1145.4  and temp >=  1128.8000000000002 ):

        let = 'e'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1145.4  and temp >=  1128.8000000000002 ):

        used.append('e')


    if (temp <  1162.0  and temp >=  1145.4 ):

        let = 'f'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1162.0  and temp >=  1145.4 ):

        used.append('f')


    if (temp <  1178.6000000000001  and temp >=  1162.0 ):

        let = 'g'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1178.6000000000001  and temp >=  1162.0 ):

        used.append('g')


    if (temp <  1195.2  and temp >=  1178.6000000000001 ):

        let = 'h'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1195.2  and temp >=  1178.6000000000001 ):

        used.append('h')


    if (temp <  1211.8000000000002  and temp >=  1195.2 ):

        let = 'i'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1211.8000000000002  and temp >=  1195.2 ):

        used.append('i')


    if (temp <  1228.4  and temp >=  1211.8000000000002 ):

        let = 'j'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1228.4  and temp >=  1211.8000000000002 ):

        used.append('j')


    if (temp <  1245.0  and temp >=  1228.4 ):

        let = 'k'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1245.0  and temp >=  1228.4 ):

        used.append('k')


    if (temp <  1261.6000000000001  and temp >=  1245.0 ):

        let = 'l'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1261.6000000000001  and temp >=  1245.0 ):

        used.append('l')


    if (temp <  1278.2  and temp >=  1261.6000000000001 ):

        let = 'm'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1278.2  and temp >=  1261.6000000000001 ):

        used.append('m')


    if (temp <  1294.8000000000002  and temp >=  1278.2 ):

        let = 'n'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1294.8000000000002  and temp >=  1278.2 ):

        used.append('n')


    if (temp <  1311.4  and temp >=  1294.8000000000002 ):

        let = 'o'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1311.4  and temp >=  1294.8000000000002 ):

        used.append('o')


    if (temp <  1328.0  and temp >=  1311.4 ):

        let = 'p'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1328.0  and temp >=  1311.4 ):

        used.append('p')


    if (temp <  1344.6000000000001  and temp >=  1328.0 ):

        let = 'q'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1344.6000000000001  and temp >=  1328.0 ):

        used.append('q')


    if (temp <  1361.2  and temp >=  1344.6000000000001 ):

        let = 'r'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1361.2  and temp >=  1344.6000000000001 ):

        used.append('r')


    if (temp <  1377.8000000000002  and temp >=  1361.2 ):

        let = 's'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1377.8000000000002  and temp >=  1361.2 ):

        used.append('s')


    if (temp <  1394.4  and temp >=  1377.8000000000002 ):

        let = 't'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1394.4  and temp >=  1377.8000000000002 ):

        used.append('t')


    if (temp <  1411.0000000000002  and temp >=  1394.4 ):

        let = 'u'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1411.0000000000002  and temp >=  1394.4 ):

        used.append('u')


    if (temp <  1427.6000000000001  and temp >=  1411.0000000000002 ):

        let = 'v'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1427.6000000000001  and temp >=  1411.0000000000002 ):

        used.append('v')


    if (temp <  1444.2  and temp >=  1427.6000000000001 ):

        let = 'w'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1444.2  and temp >=  1427.6000000000001 ):

        used.append('w')


    if (temp <  1460.8000000000002  and temp >=  1444.2 ):

        let = 'x'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1460.8000000000002  and temp >=  1444.2 ):

        used.append('x')


    if (temp <  1477.4  and temp >=  1460.8000000000002 ):

        let = 'y'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1477.4  and temp >=  1460.8000000000002 ):

        used.append('y')


    if (temp <  1494.0000000000002  and temp >=  1477.4 ):

        let = 'z'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1494.0000000000002  and temp >=  1477.4 ):

        used.append('z')


    if (temp <  1510.6000000000001  and temp >=  1494.0000000000002 ):

        let = '{'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1510.6000000000001  and temp >=  1494.0000000000002 ):

        used.append('{')


    if (temp <  1527.2  and temp >=  1510.6000000000001 ):

        let = '|'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1527.2  and temp >=  1510.6000000000001 ):

        used.append('|')


    if (temp <  1543.8000000000002  and temp >=  1527.2 ):

        let = '}'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1543.8000000000002  and temp >=  1527.2 ):

        used.append('}')


    if (temp <  1560.4  and temp >=  1543.8000000000002 ):

        let = '~'
        if let in used:
            temp += 16.6
        else:
            pass
        
        
    if (temp <  1560.4  and temp >=  1543.8000000000002 ):

        used.append('~')



    time.sleep(slp) 


print("""\n
=-=-=-=-=-=-=-=-=-=-=-=-= FINISHED =-=-=-=-=-=-=-=-=-=-=-=-=""")
print('Your Encrypted Message Is Ready!')
print("""\n=-=-=-=-=-=-=-=-=-=-=-=-= KEY =-=-=-=-=-=-=-=-=-=-=-=-=""")



time.sleep(0.3) 


#Showing Resault
ti = len(message)

for i in range(ti): #This Loop Make The Fianl Dic(Message:Encrypted Message)

    if message[i] in final:
        
        let_mes = message[i]
        val = final.get(let_mes)
        final.update({let_mes:val})

    else:

        final.update({message[i]:used[i]})


for i in range(ti): #Showing Message --> Encrypted Message
    m_to_k = message[i] + '-->' + final.get(message[i])
    print(m_to_k)
    key.append(m_to_k)
    time.sleep(0.1)


print('\n\nYour Message:\n',message) #Showing Message 
print()
print()
print('Encrypted Message:')
print(' ',end= '')

for i in range(ti): #Showing Encrypted Message
    kk = message[i]
    print(final.get(kk), end ='')

time.sleep(1)

print('\n\nDo you want to save the Key in a txt file? (Y for Yes and N for No)\n')



while True: #This Loop Is For Saving The Key File
    y_n = input('>>')
    y_n = y_n.upper()

    if y_n == 'Y':

        print('Wait...')
        cd = os.getcwd()+'\\key.txt' #Get Current Directory & Prepering It
        
        key_file = open(cd, 'w') #Create File
        key_file.write(str(key)) #Write File
        key_file.close() #Close The Key File
        
        time.sleep(1.5)
        print(f'Saved in {cd}')
        time.sleep(1)
        print('\nBYE. Window will be closed in:')
        Overwrite(8)
        break
        
    elif y_n == 'N':
        print('\nBYE. Window will be closed in:')
        Overwrite(8)
        break
    
    else:
        print('Error! Wrong input:-(')
        
