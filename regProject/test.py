# encoding=utf-8
import os
import tqdm


# keygenme1_09_keygen
def keygenme1_09():
    name = 'soundfuture'
    temp1 = 0
    for i in name:
        temp1 -= ord(i) - 0x19
    a = temp1
    print("a={}".format(hex(a & 0xffffffff)))
    temp1 = a ** 2
    temp2 = -a ^ temp1
    temp3 = temp1 * a
    b = temp3
    print("b={}".format(hex(b & 0xffffffff)))
    temp1 = 0x40e0f8
    temp1 = temp1 ** 2
    temp1 -= 0x40e0f8
    c = temp1
    # print(c)
    print("c={}".format(hex(c & 0xffffffff)))
    res = 'Bon-' + str(hex(a & 0xffffffff))[2:].upper() + '-' + str(hex(b & 0xffffffff))[2:].upper() + "-" \
          + str(hex(c & 0xffffffff))[2:].upper()
    print(res)


def crcme1_12():
    keygen = ""
    nlist = [0x168, 0x160, 0x170, 0xec, 0x13c,
             0x1cc, 0x1f8, 0xec, 0x164, 0x1f8,
             0x1a0, 0x1bc]
    for i in nlist:
        keygen += chr(i // 4 ^ 0x1b)
    print('keygen={}'.format(keygen))

    username = "soundfuture"
    eax_add = 0
    for i in username:
        eax_add += ord(i)
    eax_add *= 8
    eax_add ^= 0x515A5
    print("eax_add:{}".format(hex(eax_add)))
    edi_res = 0x797e7 - eax_add
    edi_res ^= 0x87ca
    print("edi_res:{}".format(hex(edi_res)))
    """
    下面这个函数为对输入密码的变换，实际上这个变换的含义是把输入数字从10进制换算成16进制
    因此注册机就可以把上述edi_add的16进制数直接10进制打印即可
    def password_reform(password): 
        edi = 0
        for i in password:
            edi *= 0xa
            edi += ord(i) - 0x30
        return edi
    """
    print("生成密码：{}".format(edi_res))


def acid_burn_13():
    name = "thelastede"
    esi = ord(name[0]) * 7
    esi = ord(name[1]) * 16 + esi
    save1 = esi
    esi = ord(name[3]) * 0xb
    eax = ord(name[2]) * 0xe
    esi += eax
    save2 = esi
    eax = ord(name[0]) * 0x29
    init_number_0x29 = eax * 2
    # print(init_number_0x29)
    res = 'CW-' + str(init_number_0x29) + '-CRACKED'
    print('res:{}'.format(res))


def Splish_14():
    name = "thelastede"
    if len(name) > 0xa:
        name = name[0:0xa]
    ecx = 0xa
    name_res = ''
    for ebx in range(len(name)):
        eax = ord(name[ebx]) // ecx
        edx = ord(name[ebx]) % ecx
        edx ^= ebx
        edx += 2
        if edx >= 0xa:
            edx -= 0xa
        name_res += chr(edx)
    # print(bytes(name_res.encode()))

    """
    这是对输入serials的变换，最后要求输入serials变换后与用户名变换后相等。因此可以写出逆变换
    
    input_serials = '123456'
    input_res = b''
    for ebx in range(len(input_serials)):
        edx = ord(input_serials[ebx]) % ecx
        input_res += bytes(chr(edx).encode())
    print(input_res)
    """
    k = 7  # 由于取余的逆运算结果并不唯一，因此需要乘以系数k，多次尝试k已得到可输入的serials
    input_serials = ""
    for c in name_res:
        input_serials += chr(ord(c) + k * 0xa)
    print(input_serials)


def fty_crkme3_16():
    # ori_func将原汇编的函数用python翻译了过来，实际上是判断该数是否属于广义水仙花数,即输入的序列号的数字形式，是否等于其各位数的7次方之和
    # 例如输入12-456-89,则其数字形式为1245689，此时要判断1^7+2^7+4^7+...+9^7是否等于该数本身
    # 如果是则破解成功
    def ori_func():
        series_input = '12-456-89'
        if len(series_input) != 9:
            print("input error")
            return 0

        for i in series_input:
            if i != '-' and (ord(i) < 0x30 or ord(i) > 0x39):
                print("input error")
                return 0

        if series_input[2] != '-' or series_input[6] != '-':
            print("input error")
            return 0

        """
        以下代码为逆向原始程序时一句一句话翻译得到的结果，然而观察一下，很明显下面是吧循环展开了
        而且由于要求了输入input[2]和input[6]为-，实际上这段代码是将input拼接出一个新的数字
        该数字形式是高位对应原来的高位，最低位为数据长度，因此可以进行简化,简化代码见未被注释的部分
        
        def str_combine(a, b, cl):
            a_length = a & 0xff
            b_length = b & 0xff
            length = a_length + b_length
            ncount = b_length
            if length > cl:
                if cl <= a_length:
                    return a
                else:
                    ncount = cl - a_length
            res = length
            for i in range(a_length):
                res |= a & (0xff << ((i + 1)*8))
            for i in range(ncount):
                res |= (b & (0xff << ((i + 1)*8))) << (a_length * 8)
            return res
    
        buf3 = 1 + (ord(series_input[0]) << 8)
        buf4 = buf3
        buf5 = 1 + (ord(series_input[1]) << 8)
        buf4 = str_combine(buf4,buf5,2)
        buf6 = buf4
        buf5 = (buf5 & 0xffff00ff) | (ord(series_input[3]) << 8)
        buf6 = str_combine(buf6,buf5,3)
        buf8 = buf6
        buf5 = (buf5 & 0xffff00ff) | (ord(series_input[4]) << 8)
        buf8 = str_combine(buf8,buf5,4)
        buf10 = buf8
        buf5 = (buf5 & 0xffff00ff) | (ord(series_input[5]) << 8)
        buf10 = str_combine(buf10,buf5,5)
        buf12 = buf10
        buf5 = (buf5 & 0xffff00ff) | (ord(series_input[7]) << 8)
        buf12 = str_combine(buf12, buf5, 6)
        buf14 = buf12
        buf5 = (buf5 & 0xffff00ff) | (ord(series_input[8]) << 8)
        buf14 = str_combine(buf14, buf5, 7)
        print(hex(buf14))
        """

        # 以下部分代码为上述部分的简化形式
        res = 0
        ncount = 0
        for i in range(len(series_input)):
            if series_input[i] == '-':
                continue
            else:
                res += ord(series_input[i]) << (8 * ncount)
                ncount += 1
        res = (res << 8) + ncount

        # print(hex(res))

        def tranlate_into_str(a):
            nlength = a & 0xff
            res = ''
            for i in range(nlength):
                num = a & (0xff << ((i + 1) * 8))
                num = num >> ((i + 1) * 8)
                res += chr(num)
            return res

        res = tranlate_into_str(res)

        def convert_into_int(a):
            res = int(a)
            return res

        res = convert_into_int(res)

        edi = 0
        for i in range(len(series_input)):
            if series_input[i] == '-':
                continue
            edi += pow(int(series_input[i]), 7)
        print(hex(edi))

        if res == edi:
            print("破解成功")
            return 0

    def find_the_number():
        def get_pow_7(num):
            res = 0
            for i in range(7):
                temp = num % 10
                num //= 10
                res += pow(temp, 7)
            return res

        lres = []
        for i in tqdm.tqdm(range(0000000, 9999999)):
            if i == get_pow_7(i):
                # print("find num {}".format(i))
                lres.append(i)
        return lres

    numbers = find_the_number()
    for i in range(len(numbers)):
        res = str(numbers[i])
        if len(res) != 7:
            res = res.rjust(7, '0')
        res = list(res)
        res.insert(2, '-')
        res.insert(6, '-')
        res = ''.join(res)
        print("answer {}:{}".format(i, res))


def cabeca_17():
    name = 'soundfuture'

    def get_number(c):
        c = ord(c)
        if c == 0x61:
            return 0x427, 0x79
        if c == 0x62:
            return 0x6bc, 0x6f
        if c == 0x63:
            return 0x491, 0x2e2
        if c == 0x64:
            return 0x474d, 0x2fa
        if c == 0x65:
            return 0x400, 0xe
        if c == 0x66:
            return 0x6d0, 0xd
        if c == 0x67:
            return 0x67d, 0xc
        if c == 0x68:
            return 0x750, 0xb
        if c == 0x69:
            return 0x43c, 0x63
        if c == 0x6a:
            return 0x764, 0x378
        if c == 0x6b:
            return 0xc0, 0x4d
        if c == 0x6c:
            return 0x277d, 0x22b
        if c == 0x6d:
            return 0x81e, 0x5a
        if c == 0x6e:
            return 0xe07, 0x62
        if c == 0x6f:
            return 0x8e, 0x1d2c
        if c == 0x70:
            return 0x9a670, 0x8c7f3
        if c == 0x71:
            return 0xd57, 0x288
        if c == 0x72:
            return 0x5feb, 0x21a
        if c == 0x73:
            return 0x8b0, 0x1
        if c == 0x74:
            return 0x4bb, 0x40
        if c == 0x75:
            return 0x8c2, 0x4b
        if c == 0x76:
            return 0x1ca6, 0x4e
        if c == 0x77:
            return 0x251e, 0x5
        if c == 0x78:
            return 0x395, 0x26
        if c == 0x79:
            return 0x2d13, 0x8
        if c == 0x7a:
            return 0x1900, 0x1c8
        if c == 0x41:
            return 0x428, 0x1610
        if c == 0x42:
            return 0xb1630, 0x2
        if c == 0x43:
            return 0xd86, 0x270f
        if c == 0x44:
            return 0x11a4, 0x46ff33c
        if c == 0x45:
            return 0x110a, 0x883c
        if c == 0x46:
            return 0x3cc2, 0x8618
        if c == 0x47:
            return 0x3e1a8, 0x6c81c
        if c == 0x48:
            return 0x91e4, 0x27e945
        if c == 0x49:
            return 0x6b42, 0x2fc7c3
        if c == 0x4a:
            return 0x516a4, 0xb8f47c
        if c == 0x4b:
            return 0x4345a, 0x115c7
        if c == 0x4c:
            return 0x1bfdd9, 0x12b54
        if c == 0x4d:
            return 0x286d, 0xb348c
        if c == 0x4e:
            return 0x401, 0x357ce174
        if c == 0x4f:
            return 0x674, 0x317cd7
        if c == 0x50:
            return 0x9c, 0x7dd834
        if c == 0x51:
            return 0x156, 0x39cd0
        if c == 0x52:
            return 0x8627, 0xbf44a
        if c == 0x53:
            return 0x748190, 0x854686
        if c == 0x54:
            return 0xa568, 0x13220
        if c == 0x55:
            return 0x15592, 0x302e
        if c == 0x56:
            return 0x1dd9, 0x1c43
        if c == 0x57:
            return 0x3cc0, 0x4efc8
        if c == 0x58:
            return 0x266a, 0x2ba96c08
        if c == 0x59:
            return 0x8311, 0x1c46
        if c == 0x5a:
            return 0xce1b, 0xb1664

    key1 = 0
    key2 = 0
    for c in name:
        t1, t2 = get_number(c)
        key1 += t1
        key2 += t2
    print("key1={}".format(key1))
    print("key2={}".format(key2))


def CrackMe_0006_18():
    name = 'soundfuture'
    # 通过GetVolumeInformationA函数获得，pVolumeSerialNumber是返回的硬盘序列号的地址。由于无法用python复现，故直接给出其值
    lpVolumeSerialNumber_c = 0x1F8E031F
    lpVolumeSerialNumber_d = 0x19FCB767

    def rol(num, bit):
        for i in range(bit):
            if num & 0x80000000 == 0:
                num = num * 2
            else:
                num = num * 2 - 0x100000000 + 1
        return num

    def shl(num, bit):
        return (num << bit) & 0xffffffff

    # 下面这段eax计算后面好像没用到
    eax = shl(lpVolumeSerialNumber_c, 5)
    eax = rol(eax, 0xd)
    eax = lpVolumeSerialNumber_c + lpVolumeSerialNumber_d
    eax = shl(eax, 5)
    eax = rol(eax, 0xd)

    # print(hex(eax))

    def float_calcu(a, b):
        st1 = a * a
        st0 = b * b
        st0 = st0 + st1
        st0 = st0 ** 0.5
        return int(st0) if st0 - int(st0) < 0.5 else int(st0) + 1

    sav1 = float_calcu(lpVolumeSerialNumber_c, lpVolumeSerialNumber_d)
    # print(hex(eax))

    eax = 1
    for c in name:
        eax *= ord(c)
        edx = eax >> 32
        eax &= 0xffffffff
        eax += edx
    # print(hex(eax))

    eax = rol(eax, 1)
    eax |= sav1
    eax &= 0xfffffff
    # print(hex(eax))
    magic_str = "071362de9f8ab45c"
    sav2 = eax
    sav3 = ''

    while sav2 != 0:
        eax = eax % 0x10
        eax = ord(magic_str[eax])
        sav3 += chr(eax)
        eax = sav2 // 4
        sav2 = eax
    print("key={}".format(sav3))


def cosh_3_20():
    name = 'abcdedede'
    series = '123456'

    name_2 = ''
    for i in range(len(name)):
        name_2 += chr(ord(name[i]) ^ (i + 1))
    # print(name_2)

    """
    对series的变换函数
    series_2 = ''
    for i in range(len(series)):
        series_2 += chr(ord(series[i]) ^ (i + 0xa))
    print(series_2)
    """

    series = ''
    for i in range(len(name_2)):
        series += chr(ord(name_2[i]) ^ (i + 0xa))
    print("series={}".format(series))


def Creakme_21():
    name = "black"
    if len(name) > 5:
        print("不建议用户名这么长，此时注册机会失效（因为用户名太长在内存中会覆盖掉输入的密码）")
        return 0
    res = ''
    for i in range(len(name)):
        ordi = ord(name[i])
        if ordi == 0x7a or ordi == 0x39 or ordi == 0x5a:
            ordi -= 1
        ordi = ordi + ((i + 0x61) << 8) + 0x1
        res += chr(ordi & 0xff)
        res += chr(ordi >> 8)
    print(res)


def CM_22():
    print("6287-A")


def TraceMe_23():
    name = "soundfuture"
    chars = [0xc, 0xa, 0x13, 0x9, 0xc, 0xb, 0xa, 0x8]
    series = 0
    i = 0
    for idx in range(3, len(name)):
        i = i % 8
        series += chars[i] * ord(name[idx])
        i += 1
    print(series)


def crc32crackme_25():
    data = [0x00, 0x00, 0x00, 0x00, 0x96, 0x30, 0x07, 0x77, 0x2c, 0x61, 0x0e, 0xee, 0xba, 0x51, 0x09, 0x99, 0x19, 0xc4,
            0x6d, 0x07, 0x8f, 0xf4, 0x6a, 0x70, 0x35, 0xa5, 0x63, 0xe9, 0xa3, 0x95, 0x64, 0x9e,
            0x32, 0x88, 0xdb, 0x0e, 0xa4, 0xb8, 0xdc, 0x79, 0x1e, 0xe9, 0xd5, 0xe0, 0x88, 0xd9, 0xd2, 0x97,
            0x2b, 0x4c, 0xb6, 0x09, 0xbd, 0x7c, 0xb1, 0x7e, 0x07, 0x2d, 0xb8, 0xe7, 0x91, 0x1d, 0xbf, 0x90,
            0x64, 0x10, 0xb7, 0x1d, 0xf2, 0x20, 0xb0, 0x6a, 0x48, 0x71, 0xb9, 0xf3, 0xde, 0x41, 0xbe, 0x84,
            0x7d, 0xd4, 0xda, 0x1a, 0xeb, 0xe4, 0xdd, 0x6d, 0x51, 0xb5, 0xd4, 0xf4, 0xc7, 0x85, 0xd3, 0x83,
            0x56, 0x98, 0x6c, 0x13, 0xc0, 0xa8, 0x6b, 0x64, 0x7a, 0xf9, 0x62, 0xfd, 0xec, 0xc9, 0x65, 0x8a,
            0x4f, 0x5c, 0x01, 0x14, 0xd9, 0x6c, 0x06, 0x63, 0x63, 0x3d, 0x0f, 0xfa, 0xf5, 0x0d, 0x08, 0x8d,
            0xc8, 0x20, 0x6e, 0x3b, 0x5e, 0x10, 0x69, 0x4c, 0xe4, 0x41, 0x60, 0xd5, 0x72, 0x71, 0x67, 0xa2,
            0xd1, 0xe4, 0x03, 0x3c, 0x47, 0xd4, 0x04, 0x4b, 0xfd, 0x85, 0x0d, 0xd2, 0x6b, 0xb5, 0x0a, 0xa5,
            0xfa, 0xa8, 0xb5, 0x35, 0x6c, 0x98, 0xb2, 0x42, 0xd6, 0xc9, 0xbb, 0xdb, 0x40, 0xf9, 0xbc, 0xac,
            0xe3, 0x6c, 0xd8, 0x32, 0x75, 0x5c, 0xdf, 0x45, 0xcf, 0x0d, 0xd6, 0xdc, 0x59, 0x3d, 0xd1, 0xab,
            0xac, 0x30, 0xd9, 0x26, 0x3a, 0x00, 0xde, 0x51, 0x80, 0x51, 0xd7, 0xc8, 0x16, 0x61, 0xd0, 0xbf,
            0xb5, 0xf4, 0xb4, 0x21, 0x23, 0xc4, 0xb3, 0x56, 0x99, 0x95, 0xba, 0xcf, 0x0f, 0xa5, 0xbd, 0xb8,
            0x9e, 0xb8, 0x02, 0x28, 0x08, 0x88, 0x05, 0x5f, 0xb2, 0xd9, 0x0c, 0xc6, 0x24, 0xe9, 0x0b, 0xb1,
            0x87, 0x7c, 0x6f, 0x2f, 0x11, 0x4c, 0x68, 0x58, 0xab, 0x1d, 0x61, 0xc1, 0x3d, 0x2d, 0x66, 0xb6,
            0x90, 0x41, 0xdc, 0x76, 0x06, 0x71, 0xdb, 0x01, 0xbc, 0x20, 0xd2, 0x98, 0x2a, 0x10, 0xd5, 0xef,
            0x89, 0x85, 0xb1, 0x71, 0x1f, 0xb5, 0xb6, 0x06, 0xa5, 0xe4, 0xbf, 0x9f, 0x33, 0xd4, 0xb8, 0xe8,
            0xa2, 0xc9, 0x07, 0x78, 0x34, 0xf9, 0x00, 0x0f, 0x8e, 0xa8, 0x09, 0x96, 0x18, 0x98, 0x0e, 0xe1,
            0xbb, 0x0d, 0x6a, 0x7f, 0x2d, 0x3d, 0x6d, 0x08, 0x97, 0x6c, 0x64, 0x91, 0x01, 0x5c, 0x63, 0xe6,
            0xf4, 0x51, 0x6b, 0x6b, 0x62, 0x61, 0x6c, 0x1c, 0xd8, 0x30, 0x65, 0x85, 0x4e, 0x00, 0x62, 0xf2,
            0xed, 0x95, 0x06, 0x6c, 0x7b, 0xa5, 0x01, 0x1b, 0xc1, 0xf4, 0x08, 0x82, 0x57, 0xc4, 0x0f, 0xf5,
            0xc6, 0xd9, 0xb0, 0x65, 0x50, 0xe9, 0xb7, 0x12, 0xea, 0xb8, 0xbe, 0x8b, 0x7c, 0x88, 0xb9, 0xfc,
            0xdf, 0x1d, 0xdd, 0x62, 0x49, 0x2d, 0xda, 0x15, 0xf3, 0x7c, 0xd3, 0x8c, 0x65, 0x4c, 0xd4, 0xfb,
            0x58, 0x61, 0xb2, 0x4d, 0xce, 0x51, 0xb5, 0x3a, 0x74, 0x00, 0xbc, 0xa3, 0xe2, 0x30, 0xbb, 0xd4,
            0x41, 0xa5, 0xdf, 0x4a, 0xd7, 0x95, 0xd8, 0x3d, 0x6d, 0xc4, 0xd1, 0xa4, 0xfb, 0xf4, 0xd6, 0xd3,
            0x6a, 0xe9, 0x69, 0x43, 0xfc, 0xd9, 0x6e, 0x34, 0x46, 0x88, 0x67, 0xad, 0xd0, 0xb8, 0x60, 0xda,
            0x73, 0x2d, 0x04, 0x44, 0xe5, 0x1d, 0x03, 0x33, 0x5f, 0x4c, 0x0a, 0xaa, 0xc9, 0x7c, 0x0d, 0xdd,
            0x3c, 0x71, 0x05, 0x50, 0xaa, 0x41, 0x02, 0x27, 0x10, 0x10, 0x0b, 0xbe, 0x86, 0x20, 0x0c, 0xc9,
            0x25, 0xb5, 0x68, 0x57, 0xb3, 0x85, 0x6f, 0x20, 0x09, 0xd4, 0x66, 0xb9, 0x9f, 0xe4, 0x61, 0xce,
            0x0e, 0xf9, 0xde, 0x5e, 0x98, 0xc9, 0xd9, 0x29, 0x22, 0x98, 0xd0, 0xb0, 0xb4, 0xa8, 0xd7, 0xc7,
            0x17, 0x3d, 0xb3, 0x59, 0x81, 0x0d, 0xb4, 0x2e, 0x3b, 0x5c, 0xbd, 0xb7, 0xad, 0x6c, 0xba, 0xc0,
            0x20, 0x83, 0xb8, 0xed, 0xb6, 0xb3, 0xbf, 0x9a, 0x0c, 0xe2, 0xb6, 0x03, 0x9a, 0xd2, 0xb1, 0x74,
            0x39, 0x47, 0xd5, 0xea, 0xaf, 0x77, 0xd2, 0x9d, 0x15, 0x26, 0xdb, 0x04, 0x83, 0x16, 0xdc, 0x73,
            0x12, 0x0b, 0x63, 0xe3, 0x84, 0x3b, 0x64, 0x94, 0x3e, 0x6a, 0x6d, 0x0d, 0xa8, 0x5a, 0x6a, 0x7a,
            0x0b, 0xcf, 0x0e, 0xe4, 0x9d, 0xff, 0x09, 0x93, 0x27, 0xae, 0x00, 0x0a, 0xb1, 0x9e, 0x07, 0x7d,
            0x44, 0x93, 0x0f, 0xf0, 0xd2, 0xa3, 0x08, 0x87, 0x68, 0xf2, 0x01, 0x1e, 0xfe, 0xc2, 0x06, 0x69,
            0x5d, 0x57, 0x62, 0xf7, 0xcb, 0x67, 0x65, 0x80, 0x71, 0x36, 0x6c, 0x19, 0xe7, 0x06, 0x6b, 0x6e,
            0x76, 0x1b, 0xd4, 0xfe, 0xe0, 0x2b, 0xd3, 0x89, 0x5a, 0x7a, 0xda, 0x10, 0xcc, 0x4a, 0xdd, 0x67,
            0x6f, 0xdf, 0xb9, 0xf9, 0xf9, 0xef, 0xbe, 0x8e, 0x43, 0xbe, 0xb7, 0x17, 0xd5, 0x8e, 0xb0, 0x60,
            0xe8, 0xa3, 0xd6, 0xd6, 0x7e, 0x93, 0xd1, 0xa1, 0xc4, 0xc2, 0xd8, 0x38, 0x52, 0xf2, 0xdf, 0x4f,
            0xf1, 0x67, 0xbb, 0xd1, 0x67, 0x57, 0xbc, 0xa6, 0xdd, 0x06, 0xb5, 0x3f, 0x4b, 0x36, 0xb2, 0x48,
            0xda, 0x2b, 0x0d, 0xd8, 0x4c, 0x1b, 0x0a, 0xaf, 0xf6, 0x4a, 0x03, 0x36, 0x60, 0x7a, 0x04, 0x41,
            0xc3, 0xef, 0x60, 0xdf, 0x55, 0xdf, 0x67, 0xa8, 0xef, 0x8e, 0x6e, 0x31, 0x79, 0xbe, 0x69, 0x46,
            0x8c, 0xb3, 0x61, 0xcb, 0x1a, 0x83, 0x66, 0xbc, 0xa0, 0xd2, 0x6f, 0x25, 0x36, 0xe2, 0x68, 0x52,
            0x95, 0x77, 0x0c, 0xcc, 0x03, 0x47, 0x0b, 0xbb, 0xb9, 0x16, 0x02, 0x22, 0x2f, 0x26, 0x05, 0x55,
            0xbe, 0x3b, 0xba, 0xc5, 0x28, 0x0b, 0xbd, 0xb2, 0x92, 0x5a, 0xb4, 0x2b, 0x04, 0x6a, 0xb3, 0x5c,
            0xa7, 0xff, 0xd7, 0xc2, 0x31, 0xcf, 0xd0, 0xb5, 0x8b, 0x9e, 0xd9, 0x2c, 0x1d, 0xae, 0xde, 0x5b,
            0xb0, 0xc2, 0x64, 0x9b, 0x26, 0xf2, 0x63, 0xec, 0x9c, 0xa3, 0x6a, 0x75, 0x0a, 0x93, 0x6d, 0x02,
            0xa9, 0x06, 0x09, 0x9c, 0x3f, 0x36, 0x0e, 0xeb, 0x85, 0x67, 0x07, 0x72, 0x13, 0x57, 0x00, 0x05,
            0x82, 0x4a, 0xbf, 0x95, 0x14, 0x7a, 0xb8, 0xe2, 0xae, 0x2b, 0xb1, 0x7b, 0x38, 0x1b, 0xb6, 0x0c,
            0x9b, 0x8e, 0xd2, 0x92, 0x0d, 0xbe, 0xd5, 0xe5, 0xb7, 0xef, 0xdc, 0x7c, 0x21, 0xdf, 0xdb, 0x0b,
            0xd4, 0xd2, 0xd3, 0x86, 0x42, 0xe2, 0xd4, 0xf1, 0xf8, 0xb3, 0xdd, 0x68, 0x6e, 0x83, 0xda, 0x1f,
            0xcd, 0x16, 0xbe, 0x81, 0x5b, 0x26, 0xb9, 0xf6, 0xe1, 0x77, 0xb0, 0x6f, 0x77, 0x47, 0xb7, 0x18,
            0xe6, 0x5a, 0x08, 0x88, 0x70, 0x6a, 0x0f, 0xff, 0xca, 0x3b, 0x06, 0x66, 0x5c, 0x0b, 0x01, 0x11,
            0xff, 0x9e, 0x65, 0x8f, 0x69, 0xae, 0x62, 0xf8, 0xd3, 0xff, 0x6b, 0x61, 0x45, 0xcf, 0x6c, 0x16,
            0x78, 0xe2, 0x0a, 0xa0, 0xee, 0xd2, 0x0d, 0xd7, 0x54, 0x83, 0x04, 0x4e, 0xc2, 0xb3, 0x03, 0x39,
            0x61, 0x26, 0x67, 0xa7, 0xf7, 0x16, 0x60, 0xd0, 0x4d, 0x47, 0x69, 0x49, 0xdb, 0x77, 0x6e, 0x3e,
            0x4a, 0x6a, 0xd1, 0xae, 0xdc, 0x5a, 0xd6, 0xd9, 0x66, 0x0b, 0xdf, 0x40, 0xf0, 0x3b, 0xd8, 0x37,
            0x53, 0xae, 0xbc, 0xa9, 0xc5, 0x9e, 0xbb, 0xde, 0x7f, 0xcf, 0xb2, 0x47, 0xe9, 0xff, 0xb5, 0x30,
            0x1c, 0xf2, 0xbd, 0xbd, 0x8a, 0xc2, 0xba, 0xca, 0x30, 0x93, 0xb3, 0x53, 0xa6, 0xa3, 0xb4, 0x24,
            0x05, 0x36, 0xd0, 0xba, 0x93, 0x06, 0xd7, 0xcd, 0x29, 0x57, 0xde, 0x54, 0xbf, 0x67, 0xd9, 0x23,
            0x2e, 0x7a, 0x66, 0xb3, 0xb8, 0x4a, 0x61, 0xc4, 0x02, 0x1b, 0x68, 0x5d, 0x94, 0x2b, 0x6f, 0x2a,
            0x37, 0xbe, 0x0b, 0xb4, 0xa1, 0x8e, 0x0c, 0xc3, 0x1b, 0xdf, 0x05, 0x5a, 0x8d, 0xef, 0x02, 0x2d
            ]
    name = "thelastede"
    name = "DiKeN" + name
    eax = 0 ^ 0xffffffff
    for i in range(len(name)):
        eax ^= ord(name[i])
        sav = eax
        eax &= 0xff
        ebx = data[eax * 4] + (data[eax * 4 + 1] << 8) + (data[eax * 4 + 2] << 16) + (data[eax * 4 + 3] << 24)
        eax = sav // (2 ** 8)
        eax ^= ebx
    eax ^= 0xffffffff

    # series变形算法,循环部分说白了是将输入数字转换成10进制
    # series = "6835985263"
    # series = '0' + series
    # edx = 0
    # for eax in range(1, len(series) + 1):
    #     edx += edx
    #     edx = edx * 5
    #     ebx = ord(series[eax-1])
    #     edx += ebx
    #     edx -= 0x30
    # print(hex(edx))

    series = str(eax)
    print(series)


def KeygenMe_26():
    username = "wanaoa1"

    def calcu(name):
        eax = 1
        esi = 0
        for ecx in range(len(name), 0, -1):
            edx = ord(name[eax - 1])
            ebx = edx
            ebx *= edx
            esi += ebx

            ebx = edx
            ebx //= 2
            ebx += 3
            ebx *= edx
            ebx -= edx

            esi += ebx
            esi += esi
            eax += 1

        series = chr(esi & 0xff) + chr(esi >> 8 & 0xff) + chr(esi >> 16 & 0xff) + chr(esi >> 24 & 0xff)
        for c in series:
            if (ord(c) <= 32 or ord(c) >= 127) and ord(c) != 0:
                print("name {} can not generate a enterable series, please try another one".format(username))
                return ''
        flag = False
        for i in range(len(series) - 1, -1, -1):
            if series[i] == '\x00' and flag is False:
                series = series[:i]
            elif series[i] == '\x00':
                print("name {} can not generate a enterable series, please try another one".format(username))
                return ''
            else:
                flag = True
        return series

    def search():
        clist = []
        for i in range(ord('a'), ord('z') + 1):
            clist.append(chr(i))
        for a in clist:
            for b in clist:
                for c in clist:
                    for d in clist:
                        for e in clist:
                            for f in clist:
                                for g in clist:
                                    print("try {}".format(a + b + c + d + e + f + g))
                                    res = calcu(a + b + c + d + e + f + g)
                                    if len(res) != 0:
                                        print("find username {}".format(a + b + c + d + e + f + g))
                                        print("series:{}".format(res))

    res = calcu(username)
    if len(res) != 0:
        print(res)


def figugegl_1_29():
    name = 'soundfuture'
    series = ''
    for i in range(len(name)):
        series += chr(ord(name[i]) - i)
    print(series)


def CrackMe_4_30():
    username = 'bluethefat'
    if len(username) <= 6:
        print("too short")
        return
    esi = 0
    for i in range(6):
        esi += ord(username[i]) * 2
    # print(hex(esi))
    eax = len(username) * 2 + esi
    print(eax)


def Cruehead_1_31():
    username = "xjh"
    fake_series = '123456'

    username = username.upper()
    if len(username) >= 10:
        username = username[:10]
    edi = 0
    for c in username:
        edi += ord(c)
    edi ^= 0x5678

    """
    密码加密机制，字符串转成十进制后异或
    eax = 0xa
    edi = 0
    for c in fake_series:
        ebx = ord(c) - 0x30
        edi *= eax
        edi += ebx
    print(edi)
    edi ^= 0x1234
    """
    edi ^= 0x1234
    print(edi)


def Crackme2_32():
    username = 'soundfuture'
    esi = 0
    for c in username:
        esi += ord(c) ** 2
        esi += ord(c) // 2
        esi -= ord(c)
    print(esi)


def dccrackme1_33():
    username = 'soundfuture'
    esi = 0
    for c in username:
        esi += (ord(c) - 0x17) * (ord(c) - 0x11)
    print(esi)


def Dope2112_2_35():
    username = 'soundfuture'
    res = 0x37
    for c in username:
        res += ord(c) * (2 ** 9)
    print(res)


def Andrénalin_2_36():
    username = 'soundfuture'
    add = 0
    for c in username:
        add += ord(c)
    # print(hex(add))
    add *= 1234567890
    add = str(add)
    print(add)
    print(add[:3] + '-' + add[4:8] + '-' + add[9:])


def fireworx_2_37():
    username = 'soundfuture'
    print(username + username + '625g72')


def Eternal_Bliss_3_38():
    # username = 'soundfuture'
    username = "Reverse"
    a = 0
    for c in username:
        a += ord(c)
    b = 0x52 + 0x65 + 0x76 + 0x65 + 0x72 + 0x73 + 0x65
    if a != b:
        print("failed")
    print(username)


def eKH_1_39():
    username = 'thelastede'
    a = "LANNYDIBANDINGINANAKEKHYANGNGENTOT"
    b = "LANNY5646521"
    ebx = 0
    for i in range(len(username)):
        ebx += ord(username[i])
        ebx = ebx << 8
        ebx ^= ord(a[i])
        if ebx & 0x80000000 != 0:
            # ebx *= -1，但是有符号乘法，且寄存器为4字节
            ebx ^= 0xffffffff
            ebx += 1
        ebx &= 0xffffffff
    ebx ^= 0x12345678
    # print(ebx)
    res = ''
    for i in range(len(str(ebx))):
        edx = ebx % 0xa
        res += b[edx]
        ebx //= 0xa
    print(res)


def DaNiEl_RJ_1_40():
    username = 'soundfuture'
    sav1 = ''
    for c in username:
        sav1 += chr(ord(c) + 5)
    print(sav1)


def crackme_2_41():
    username = 'soundfuture'
    if len(username) < 5:
        print("username too short")
        return 0
    idx = [0, 2, 3, 4]
    res = []
    for i in idx:
        res.append(ord(username[i]) // 10)
    for i in range(len(res)):
        res[i] //= 10
    for i in res:
        print('{}'.format(i), end=' ')


def crackme_42():
    # initVar = [
    #     0x1e, 0xbf, 0xa2, 0x1a, 0xf3, 0x0b, 0xb7, 0x34, 0x4e, 0x4b, 0x34, 0xc5, 0x0e, 0x38, 0x88, 0x4b,
    #     0x32, 0xc5, 0x06, 0x38, 0x88, 0x0a, 0x35, 0x43, 0xc0, 0x61, 0x42, 0x8d, 0x76, 0x4c, 0x45, 0xbf,
    #     0x0b, 0x47, 0xf2, 0x0e, 0x48, 0x3a, 0xc5, 0x06, 0x38, 0x88, 0x0a, 0x30, 0x52, 0xc0, 0x61, 0x42,
    #     0x8d, 0x76, 0x4b, 0x1f, 0xbf, 0x0b, 0x47, 0xf2, 0x0e, 0x4d, 0x0a, 0xc5, 0x06, 0x38, 0x88, 0x0a,
    #     0x33, 0x68, 0xc0, 0x61, 0x42, 0x8d, 0x76, 0x46, 0x63, 0xbf, 0x0b, 0x47, 0xf2, 0x0e, 0x42, 0x17,
    #     0xc5, 0x06, 0x38, 0x88, 0x0a, 0x3e, 0x33, 0xc0, 0x61, 0x42, 0x8d, 0x76, 0x45, 0x6b, 0xbf, 0x0b,
    #     0x47, 0xf2, 0x0e, 0x47, 0x33, 0xc5, 0x06, 0x38, 0x88, 0x0a, 0x39, 0x1d, 0xc0, 0x61, 0x42, 0x8d,
    #     0x76, 0x40, 0x6b, 0xbf, 0x0b, 0x47, 0xbe, 0x46, 0xcb, 0xc5, 0x1a, 0xc0, 0x61, 0x42, 0xc3, 0x3e,
    #     0xc5, 0x0e, 0x38, 0xc4, 0x03, 0x35, 0xce, 0xba, 0x5c, 0xc5, 0x1e, 0x38, 0xc6, 0x01, 0x35, 0xc5,
    #     0x0e, 0x38, 0xc4, 0x03, 0x36, 0xce, 0xba, 0x5d, 0xc5, 0x1e, 0x38, 0xc6, 0x01, 0x36, 0xc5, 0x0e,
    #     0x38, 0xc4, 0x03, 0x37, 0xce, 0xba, 0x53, 0xc5, 0x1e, 0x38, 0xc6, 0x01, 0x37, 0xc5, 0x0e, 0x38,
    #     0xc4, 0x03, 0x30, 0xce, 0xba, 0x5b, 0xc5, 0x1e, 0x38, 0xc6, 0x01, 0x30, 0xc5, 0x0e, 0x38, 0xc4,
    #     0x03, 0x31, 0xce, 0xba, 0x14, 0xc5, 0x1e, 0x38, 0xc6, 0x01, 0x31, 0xc5, 0x0e, 0x38, 0xc4, 0x03,
    #     0x32, 0xce, 0xba, 0x6f, 0xc5, 0x1e, 0x38, 0xc6, 0x01, 0x32, 0xc5, 0x0e, 0x38, 0xc4, 0x03, 0x33,
    #     0xce, 0xba, 0x60, 0xc5, 0x1e, 0x38, 0xc6, 0x01, 0x33, 0xc5, 0x0e, 0x38, 0xc4, 0x03, 0x3c, 0xce,
    #     0xba, 0x79, 0xc5, 0x1e, 0x38, 0xc6, 0x01, 0x3c, 0xc5, 0x0e, 0x38, 0xc4, 0x03, 0x3d, 0xce, 0xba,
    #     0x73, 0xc5, 0x1e, 0x38, 0xc6, 0x01, 0x3d, 0xc5, 0x0e, 0x38, 0xc4, 0x03, 0x3e, 0xce, 0xba, 0x69,
    #     0xc5, 0x1e, 0x38, 0xc6, 0x01, 0x3e, 0xc5, 0x0e, 0x38, 0xc4, 0x03, 0x3f, 0xce, 0xba, 0x60, 0xc5,
    #     0x1e, 0x38, 0xc6, 0x01, 0x3f, 0xc5, 0x0e, 0x38, 0xc4, 0x03, 0x38, 0xce, 0xba, 0x5c, 0xc5, 0x1e,
    #     0x38, 0xc6, 0x01, 0x38, 0xc5, 0x0e, 0x38, 0xc4, 0x03, 0x39, 0xce, 0xba, 0x5d, 0xc5, 0x1e, 0x38,
    #     0xc6, 0x01, 0x39, 0x89, 0x0e, 0xc8, 0x4e, 0x4b, 0x34, 0x4e, 0xc0, 0x71, 0x42, 0x48, 0x71, 0xb2,
    #     0xc0, 0x79, 0x46, 0x48, 0x79, 0xb2, 0xc1, 0x25, 0xc6, 0x1b, 0x3b, 0xc5, 0x0e, 0xc8, 0xcd, 0x8b,
    #     0x35, 0xc7, 0x0e, 0xc8, 0xc5, 0x06, 0x3c, 0x4d, 0x06, 0xc8, 0x41, 0xf5, 0x25, 0xcb, 0x99, 0x41,
    #     0x97, 0xc0, 0x71, 0x42, 0x48, 0x71, 0xb2, 0x8d, 0x74, 0x41, 0x4b, 0xbf, 0xab, 0x16, 0xf7, 0xff]
    #
    # useful_char_ascii_list = [i for i in range(0x20, 0x7e)]

    # def search(length):
    #     # 下面这段代码是早期不懂程序真实内涵的时候用来暴力搜索的
    #     # 这个程序有个独特的检查机制，会检查输入serial的前三个字符是否合法，下面这个函数给出了所有合法前缀
    #     # 输入参数为你想输入的serial的长度
    #     # for i in useful_char_ascii_list:
    #     #     for j in useful_char_ascii_list:
    #     #         for k in useful_char_ascii_list:
    #     #             temp = []
    #     #             temp.append(i ^ 0x54 ^ length)
    #     #             temp.append(j ^ 0x4d ^ length)
    #     #             temp.append(k ^ 0x47 ^ length)
    #     #             eax = (temp[0] ^ initVar[0]) * (temp[1] ^ initVar[1]) * (temp[2] ^ initVar[2])
    #     #             if eax == 0x2A8BF4:
    #     #                 res.append((i, j, k))
    #     #                 # print(temp)
    #
    #     # 0x55是push ebp的操作码。0x8bec是mov ebp,esp的操作码
    #     return 0x55 ^ 0x54 ^ 0x1e ^ length, 0x8b ^ 0x4d ^ 0xbf ^ length, 0xec ^ 0x47 ^ 0xa2 ^ length
    #
    # useful_prefix = search(6)
    # useful_prefix_char = chr(useful_prefix[0]) + chr(useful_prefix[1]) +chr(useful_prefix[2])
    # useful_prefix_bytes = useful_prefix[0].to_bytes(1,'big') + useful_prefix[1].to_bytes(1,'big')\
    #                 + useful_prefix[2].to_bytes(1,'big')
    # with open(r"F:\逆向学习相关\160 crack me_new\解压后\42\key.dat",'wb') as f:
    #     f.write(useful_prefix_bytes)
    #
    # # search2函数搜索了除了前3个字符以外后面的合法字符
    # # prefix为前三个字符，当然得是合法的。可以用search搜出来
    # # length为预期的serial总长度
    # # remain为待搜索的字符长度，对于最外层，就直接等于length-3即可
    # def search2(prefix, length, remain):
    #     def search2_deep(prefix, length, remain):
    #         res = []
    #         for j in useful_char_ascii_list:
    #             i = j
    #             i ^= length
    #             idx = length - remain
    #             i ^= ord(prefix[idx % 3])
    #             if remain != 1:
    #                 if i != 0x20:
    #                     ret = search2_deep(prefix + chr(i), length, remain - 1)
    #                     for l in ret:
    #                         temp = [j]
    #                         temp.extend(l)
    #                         res.append(temp)
    #                 else:
    #                     temp = []
    #                     for k in range(remain - 1):
    #                         temp.append(-1)
    #                     temp2 = [j]
    #                     temp2.extend(temp)
    #                     res.append(temp2)
    #             elif i == 0x20:
    #                 res.append([j])
    #         return res
    #
    #     # 对prefix进行预处理
    #     prefix = chr(ord(prefix[0]) ^ 0x54 ^ length) + chr(ord(prefix[1]) ^ 0x4d ^ length) \
    #              + chr(ord(prefix[2]) ^ 0x47 ^ length)
    #     return search2_deep(prefix, length, remain)
    #
    # useful_suffix = search2(useful_prefix_char, 6, 6 - 3)
    # useful_suffix_char = []
    # for i in useful_suffix:
    #     temp = ''
    #     for j in i:
    #         if j != -1:
    #             temp += chr(j)
    #         else:
    #             temp += '*'  # 显然这里其实是有问题，因为我试图用*代替任意字符。但*本身就是合法字符的一部分。但我也没想到好的代替方法，就这样了
    #     useful_suffix_char.append(temp)
    #
    # for i in useful_suffix_char:
    #     print(i)

    # serial的前三个字符见useful_prefix
    # serial后面的字符也是有要求的，其搜索方式见search2
    # 下面这段代码是汇编程序逻辑，后面还有一段是吧变形后的序列号用\x20分割，分割的后半段作为用户名显示，这里我就不续写了
    # serial = ':^h-**'
    # temp = ''
    # for i in serial:
    #     temp += chr(ord(i) ^ len(serial))
    # serial = chr(ord(temp[0]) ^ 0x54)
    # serial += chr(ord(temp[1]) ^ 0x4d)
    # serial += chr(ord(temp[2]) ^ 0x47)
    # serial += temp[3:]
    # 序列号长度最好可以整除3，不然下面这段代码会越界
    # temp = serial[:3]
    # for i in range(3, len(serial), 3):
    #     temp += chr(ord(serial[0]) ^ ord(serial[i]))
    #     temp += chr(ord(serial[1]) ^ ord(serial[i + 1]))
    #     temp += chr(ord(serial[2]) ^ ord(serial[i + 2]))
    # serial = temp
    # print(serial)
    #
    # resList = []
    # ncount = 0
    # for i in range(len(initVar) - 1):
    #     resList.append(initVar[i] ^ ord(serial[ncount]))
    #     ncount = (ncount + 1) % 3
    # resList.append(0xff)
    #
    # eax = resList[1] * resList[2] * resList[0]
    # print(hex(eax))
    # if eax != 0x2A8BF4:
    #     print("前三个字符有问题")

    # 上面的代码过于杂乱，下面整理成注册机形式
    def generate():
        # username = input("your name:")
        username = 'soundfuture'
        username_length = len(username)

        program_start_bytes = [0x1e, 0xbf, 0xa2]
        init_bytes = [0x54, 0x4d, 0x47]
        serials = b''
        length = username_length + 6
        prefix = [0x55, 0x8b, 0xec]
        # 获取前三个字节的值
        for i in range(len(program_start_bytes)):
            prefix[i] ^= program_start_bytes[i] ^ init_bytes[i] ^ length
        # 0x20是用来分割字符串的，0x21和0x22纯粹是凑位置数的，因为每3个进行一次轮变换
        threeBytesFollow = [0x21, 0x22, 0x20]
        # 获取4~6个字节的值
        for i in range(len(threeBytesFollow)):
            threeBytesFollow[i] ^= prefix[i] ^ init_bytes[i]
        prefix.extend(threeBytesFollow)
        # 取用户名并对用户名每个字符进行变形，同时与上述字节连接成一个字节字符串
        for i in range(len(username)):
            prefix.append(ord(username[i]) ^ prefix[i % 3] ^ init_bytes[i % 3])
        for i in range(len(prefix)):
            serials += prefix[i].to_bytes(1, 'big')
        print("你的序列号是:{}\n由于是字节流形式，因此直接写入对应文件".format(serials))
        with open(r"F:\逆向学习相关\160 crack me_new\解压后\42\key.dat", 'wb') as f:
            f.write(serials)

    generate()


def tsrh_crackme_44():
    username = 'soundfuture'
    serials = 'tsrh-' + str(len(username) + 0x7d3) + '-'
    sav1 = int.from_bytes(serials[:4].encode(), 'little') + 0x3220
    for c in username:
        eax = ord(c) + 0xc
        edx = eax - 0x11 + eax - len(serials)
        eax ^= edx
        serials += hex(eax)[2:]
    edx = sav1 ^ 0x403321
    # print(serials)
    serials = list(serials)
    for i in range(len(serials)):
        if i >= 0xa:
            serials[i] = serials[i].upper()  # 一个坑点，wsprintfA以%x为参数时写入的是大写字母
        serials[i] = ord(serials[i])

    def memWrite(num, serials_, idx):
        numLen = 0
        for numLen in range(4):
            if num >> (numLen * 8) == 0:
                break
            num = num >> (numLen * 8)
        for i in range(idx, idx + 4):
            if i - idx + 1 >= numLen:
                serials_[i] = num >> ((i - idx) * 8)
            else:
                serials_[i] = 0

    def loop1(serials_):
        for esi in range(1, 0x10):
            if esi > len(username):
                return
            eax = ord(username[esi - 1]) + 1
            edx = serials_[0xb + esi]
            eax ^= edx
            while eax < 0x41:
                eax += 0x8
            while eax > 0x5a:
                eax -= 0x3
            temp_esi = esi + 9
            memWrite(eax, serials_, temp_esi)

    loop1(serials)
    result = ''
    for i in range(len(serials)):
        if serials[i] == 0:
            break
        result += chr(serials[i])
    print(result)


def CrackMe_45():
    username = 'thebluefat'

    """
    serials计算方法,即数字字符串转10进制数
    serials = '123456'
    eax = 0
    for c in serials:
        eax = eax * 10 + int(c)
    sav1 = eax
    """

    eax = 1
    for c in username:
        eax *= ord(c)
    eax &= 0xfffffff
    print(eax)


def mfykm1_46():
    """
    import sys
    按理来说，该程序会获取系统的主版本号，次版本号和构建号，在python中用以下方式获取
    但是不知道为什么，两边获取的数值对不上，源程序用的是GetVersionExA函数。总之下面将直接从内存中提取数据
    major_ver = sys.getwindowsversion().major
    minor = sys.getwindowsversion().minor
    build_num = sys.getwindowsversion().build
    """

    major_ver = 6
    minor_ver = 2
    build_num = 0x23f0
    eax = major_ver * minor_ver + build_num
    edx = eax - minor_ver
    eax = build_num * 0xcdd + edx + build_num
    print(eax)


def surre_47():
    num_chr = [chr(ord('0') + i) for i in range(10)]
    res = 0x20a9
    for i in num_chr:
        a = res // ord(i)
        b = res % ord(i)
        if b >= 0x21:
            serials = a * i + chr(b)
            print("serials = {}".format(serials))
    print("随意挑选一个序列号即可，写进一个txt里然后用软件打开即可")


def monkeycrackme1_48():
    username = 'thebluefat'
    edx_4 = 0xce6d
    edx_8 = 0x58bf
    ebp_12 = 0x4de1
    result = ''
    for c in username:
        eax = ord(c) ^ (ebp_12 >> 8)
        result += hex(eax)[2:].upper()
        eax = eax + ebp_12
        ebp_12 = (eax * edx_4 + edx_8) & 0xffff
    print(result)


def crackme8_49():
    import win32api
    serial = win32api.GetVolumeInformation("C:\\")[1]
    serial *= 2
    serial *= int(str(serial)[3]) * 3
    serial &= 0xffffffff

    def trans_num_to_signed_str(num):
        b = num & 0x80000000
        if b == 0:
            return str(num)
        else:
            res = '-'
            num &= 0x7fffffff
            num ^= 0x7fffffff
            num += 1
            res += str(num)
            return res

    magic_str1 = trans_num_to_signed_str(serial)

    username = 'wa1ex'
    sav1 = ''
    for c in username:
        sav1 += hex(ord(c))[2:]
    sav1 = sav1.upper()
    print(magic_str1 + sav1)


def DaXXoR_50():
    username = 'thebluefat'
    sav1 = ''
    for c in username:
        """
        temp = len(username) + ord(c) - 0x4
        temp = temp - len(username) - 0x2
        temp += 2
        """
        sav1 += chr(ord(c) - 0x4)

    def add_str(ori, idx, string):
        if idx <= len(ori) - 1:
            result = ori[:idx] + string + ori[idx:]
        else:
            result = ori + string
        return result

    sav1 = add_str(sav1, 3, '-')
    sav1 = add_str(sav1, 5, '-')
    sav1 = add_str(sav1, 6, 'axd')
    print(sav1)


def k4n_51():
    username = 'thebluefat'
    ebx = 0
    for ecx in range(len(username)):
        eax = ord(username[ecx]) ^ (ecx + 1)
        ebx += eax
    eax *= 6
    ebx *= 2 ** 7
    eax += ebx
    print(hex(eax)[2:].upper())


def tc_2_52():
    username = 'soundfuture'
    bl = 0
    si = 0
    for i in range(len(username)):
        al = ord(username[i])
        bl = ((bl - al) & 0xff) + 1 + i
        si += bl
    while si < 0x438d:
        si += 0x45e6
    res = str(si)
    print(res[:2] + "-" + res[2] + "-" + res[3:])


def KeyGen_me_3_53():
    username = 'soundfuture'
    temp = ''
    for i in range(len(username) - 1, -1, -1):
        temp += username[i]

    username = temp
    temp = ''
    for c in username:
        temp += chr(ord(c) ^ 0x30)
    username = temp

    serials = ''
    for c in username:
        serials += chr(ord(c) ^ 0x20)
    print(serials)


def vcrkme01_54():
    username = 'thebluefat'
    serials = ''
    serials += username[0]
    serials += '-'
    ebp = 0  # 太会写程序了，还有用ebp来算数的。源程序给我看的一愣
    for c in username:
        ebp += ord(c)
    ebp += 0x6064
    sav1 = str(ebp)
    serials += username[len(username) - 1].upper()
    ebp += 0x6064
    serials += sav1 + '-' + str(ebp)
    print(serials)


def BCG_55():
    key = '123456789'
    temp = ''
    for c in key:
        temp += chr(ord(c) ^ 0x58)
    key += '\x00' + temp + '\x00'
    with open(r"F:\逆向学习相关\160 crack me_new\解压后\55\[BCG].Key", 'w') as f:
        f.write(key)
    print("已经生成key文件,key={}".format(key))


def d2k2_crackme01_56():
    username = 'thebluefat'
    eax = 0x5
    result = ""
    for c in username:
        cl = (ord(c) ^ 0x29) + eax
        if cl < 0x41 or cl > 0x5a:
            cl = 0x52 + eax
        result += chr(cl)
        eax -= 1
        if eax == 0:
            break

    eax = 0x5
    for c in username:
        cl = (ord(c) ^ 0x27) + eax + 1
        if cl < 0x41 or cl > 0x5a:
            cl = 0x4d + eax
        result += chr(cl)
        eax -= 1
        if eax == 0:
            break

    cl = 0
    serials = ''
    for c in result:
        dl = ord(c) + 5
        if dl > 0x5a:
            dl -= 0xd
        dl ^= 0xc
        if dl < 0x41:
            dl = 0x4b + cl
        elif dl > 0x5a:
            dl = 0x4b - cl
        cl += 1
        serials += chr(dl)
    print(serials)


def crackme3_58():
    """
    username = 'soundfuture'
    str1 = 'crackme'
    str2 = '657uthutduehdhdhd,ljhgs4sgf4s5s5gs5sg5g45s4g5dgyshste][gf]fg]f]d]'
    result = ''
    serial_count = 9
    for i in range(0,serial_count):
        edx = ord(str1[i]) & ord(str2[i]) if i <= 6 else 0 & ord(str2[i])
        al = edx & ord(str1[i]) if i <= 6 else 0 & edx
        cl = al ^ ord(str2[i])
        cl += i
        result += chr(cl)
    """
    print(4339744)


def Dope2112_1_59():
    username = 'thebluefat'
    switch = {}
    nlist = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    keys = [0x18, 0x25, 0x42, 0xc, 0xd, 0x6, 0x36, 0x2b, 0x17, 0x2f, 0x13, 0x82, 0x9b, 0x92, 0x3, 0x63, 0x21, 0x42,
            0x5c, 0x29, 0xc7, 0x66, 0x58, 0xa, 0x28, 0x50]
    for i in range(26):
        switch[nlist[i]] = keys[i]

    def get_switch(a):
        if 'a' <= a <= 'z':
            return switch[a]
        else:
            return 0x5d

    bl = 0x5d
    for i in range(5):
        bl += get_switch(username[i])
    bl &= 0xff
    # print(hex(bl))
    eax = len(username) * 0x4a7e
    print(str(bl) + '-' + str(eax))


def keyfileme_61():
    username = 'soundfuture'
    if len(username) > 0x10:
        print("too long")
    result = username.ljust(0x10, ' ')
    res = 0
    for c in username:
        res += (ord(c) + 0xf) ^ 0x20
    res = (res * 0x7a69) & 0xffffffff
    serial = hex(res)[2:].upper()
    print("序列号等于:{}".format(serial))
    result += serial.ljust(0x10, ' ')
    with open(r"F:\逆向学习相关\160 crack me_new\解压后\61\keyfile.dat", 'w') as f:
        f.write(result)
    print("keyfile文件已写入")


def Syllogism_crackme1_62():
    username = 'soundfuture'
    print(" " + username[1:])


def crackme_63():
    username = 'bluefat'
    if len(username) >= 0xa or len(username) <= 0:
        print("not suggest")
        return 0

    magic_str1 = ';;;;;;;;;;;;;**====,,=,,========*=**=*=**=*=**=*=*=* '
    magic_str2 = ''
    for c in magic_str1:
        magic_str2 += chr(ord(c) + 1)
    local4 = len(magic_str2) + 2
    magic_str2 += '\x00' + username

    for c in range(len(magic_str2)):
        if magic_str2[c] == '>':
            local4 += 1
        elif magic_str2[c] == '<':
            local4 -= 1
        elif magic_str2[c] == '+':
            a = chr(ord(magic_str2[local4 - 1]) + 1)
            magic_str2 = magic_str2[:local4 - 1] + a + magic_str2[local4:]
        elif magic_str2[c] == '-':
            a = chr(ord(magic_str2[local4 - 1]) - 1)
            magic_str2 = magic_str2[:local4 - 1] + a + magic_str2[local4:]
        elif magic_str2[c] == '[':
            eax = local4
            a = ord(magic_str2[eax])
            if a == 0:
                while magic_str2[eax] != ']':
                    eax += 1
        elif magic_str2[c] == ']':
            eax = local4
            a = ord(magic_str2[eax])
            if a == 0:
                while magic_str2[eax] != '[':
                    eax -= 1
        elif magic_str2[c] == '!':
            break

    # 注意，虽然网上所有教程都说这是个固定值，但其实这不是个固定值，其来源依然不明。甚至直接打开程序和用ollydbg打开他结果都不一样
    edi = 0x19F430  # ollydbg直接打开得到的值
    edi = 0x19F50C  # 先直接运行程序，后用IDA attach得到的值
    for i in range(len(magic_str1) + 1, len(magic_str2)):
        edi += ord(magic_str2[i])
    print(edi)


def CR_Game0_7_64():
    username = 'soundfuture'
    company = 'thebluefat'

    def stage0():
        print("仅serial有效")
        print("JPL-168-39")

    def stage1():
        print("仅serial有效")
        a = "CR-Game vXO"
        a = a[:10] + chr(ord('O') - 0x1f)
        print(a)

    # stage1()

    def stage2():
        print("仅serial有效")
        a = chr(0x32) + chr(0x6c) + chr(0x65) + chr(0x76) + chr(0x65) + chr(0x4c)
        a += chr(0x6c - 0x3b) + chr(0x47) + chr(0x43)
        print(a)

    # stage2()

    def stage3(username):
        print("未用到company")
        username = username.upper()
        magic_str1 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        serials = ''
        for c in username:
            serials += magic_str1[ord(c) - 0x41]
        print(serials)

    # stage3(username)

    def stage4(username):
        magic_str1 = 'polkiujmnhytgbvfredcxswqaz'
        magic_str2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        serials = ''
        for c in username:
            if ord('a') <= ord(c) <= ord('z'):
                idx = ord(c) - ord('a')
            elif ord('A') <= ord(c) <= ord('Z'):
                idx = ord(c) - ord('A')
            else:
                print("The input is not suggested")
                return 0
            serials += magic_str1[idx]

        for c in username:
            if ord('a') <= ord(c) <= ord('z'):
                idx = ord(c) - ord('a')
            elif ord('A') <= ord(c) <= ord('Z'):
                idx = ord(c) - ord('A')
            else:
                print("The input is not suggested")
                return 0
            serials += magic_str2[idx]
        print(serials)

    # stage4(username)

    def stage5(username):
        magic_str1 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        magic_str2 = 'pOlKiUjmnhytgbVfredCXSwqaZ'
        username = username.upper()
        serials = ''
        for c in username:
            idx = magic_str1.find(c)
            al = magic_str2[idx]
            serials += al
        print(serials)

    # stage5(username)

    def stage6(username, company):
        serials = 'JiP'  # 固定开头
        serials += chr((ord(company[0]) & 6) + ord(username[0]))
        serials += chr((ord(username[0]) & 9) + ord(company[0]))

        def search():
            alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
            alphabet.extend([chr(i) for i in range(ord("A"), ord('Z') + 1)])
            alphabet.extend([chr(i) for i in range(ord("0"), ord("9") + 1)])
            for a in alphabet:
                for b in alphabet:
                    for c in alphabet:
                        for d in alphabet:
                            eax = (ord(a) << 24) + (ord(b) << 16) + (ord(c) << 8) + ord(d)
                            edx = int.from_bytes(username[:4].encode(), 'little')
                            edx ^= eax
                            edx &= 0x9070503
                            edx += int.from_bytes(username[:4].encode(), 'little')
                            flag = 0
                            ret = edx.to_bytes(4, 'little').decode()
                            for i in range(4):
                                temp = edx & 0xff
                                edx = edx >> 8
                                if chr(temp) in alphabet or temp == 0:
                                    continue
                                else:
                                    flag = 1
                                    break

                            if flag == 0:
                                # print("{}{}{}{}{}".format(a,b,c,d,ret))
                                return a + b + c + d + ret

        serials += search()
        magic_str = 'JiP4ZAQWSXCDERFVBGTYHNMJUIKLOP'
        username = username.upper()
        for c in username:
            c = ord(c) - 0x3d
            serials += magic_str[c]
        print(serials)

    # stage6(username,company)

    def stage7(username, company):
        magic_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        username = username + company
        username = username[:0xd]

        """
        serials = '1234567890123456'
        把输入的serials经过下标变换后转为64进制形式
        由于len(magic_str) = 64,所以64进制变换后不同的数之间不会重叠
        res = ''
        for i in range(0,len(serials),4):
            ecx = magic_str.find(serials[i]) << 6
            ecx += magic_str.find(serials[i+1])
            ecx = ecx << 6
            ecx += magic_str.find(serials[i+2])
            ecx = ecx << 6
            ecx += magic_str.find(serials[i + 3])
            print(hex(ecx))
            res += hex(ecx)[2:4] + ' ' + hex(ecx)[4:6] + ' '+ hex(ecx)[6:8] + ' '
        print(res)
        """

        # 当写入内存时，ecx的高位写在低地址，所以是按照大端序存储的，因此username的结果每3字节一取时需要把该3字节按大端序排列
        # 随后我们可以发现，serials的低字节首先被处理，并且会被多次*64，所以低字节写入最终数字的高位
        # 因此对于截取的数字，第一次对64取余的结果应当是序列号的第四位被处理得到的结果，因此每次要逆序
        serials = ''
        for i in range(4):
            a = int.from_bytes(username[i * 3:i * 3 + 3].encode(), 'big')
            # print(hex(a))
            temp = ''
            for j in range(4):
                b = a % 64
                a = a >> 6
                temp += magic_str[b]
            temp = list(reversed(temp))
            serials += ''.join(temp)
        print(serials)

    stage7(username, company)


def Eternal_Bliss_65():
    itype = 'integer'
    itype = itype.lower()
    if itype == 'string':
        print("String")
    elif itype == 'variant':
        print("Empty")
    elif itype == 'long':
        print(0x2C2FAE)
    elif itype == 'currency':
        print(13579.2468)
    elif itype == 'byte':
        print(0xEF)
    elif itype == 'single':
        print("9764317691904")
    elif itype == 'double':
        print("1.47258369789456E17")
    elif itype == 'integer':
        print(0x5BEF)
    else:
        print("type error")


def Andrenalin_3_66():
    magic_str = 'kXy^rO|*yXo*m\kMuOn*+'
    serials = ''
    for c in magic_str:
        serials += chr(ord(c) - 0xa)
    print(serials)


def CarLitoZ_1_67():
    magic_str = "bPe CrackMe   v1.0                                               " \
                "                                                                 " \
                "           This CrackMe it's to trainer your VB cracking ab" \
                "ility                                                            " \
                "                                                               De" \
                "veloped by CarLitoZ"
    serials = ''
    serials += magic_str[5] + magic_str[8] + magic_str[142] + magic_str[15] + magic_str[160] + magic_str[170]
    serials += magic_str[165] + magic_str[167]
    print(serials)


def figugegl_3_68():
    magic_str = '203945709398475029384750293875577934765620110289347563929867122287863095762304984875020398746563'
    username = 'soundfuture'
    serials = ''
    for c in username:
        a = ord(c) - 0x20
        serials += magic_str[a]
    print(serials)


def AD_CM_4_69():
    username = 'soundfuture'
    serials = ''
    for i in range(len(username)):
        eax = ord(username[i]) // 6
        edx = ord(username[i]) // 4
        eax *= edx
        edx = ord(username[i]) // 0xa
        eax //= edx
        serials += str(eax)
    serials = 'ADCM4-' + serials + '-YEAH!'
    print(serials)


def CodeFantasy系列_Crackme_70():
    username = 'soundfuture'
    """
    sav1 = ''
    for c in username:
        sav1 += chr(ord(c) + 1)
    sav2 = ''
    for c in username:
        sav2 += chr(ord(c) + 3)
    sav3 = ''
    for c in username:
        sav3 += chr(ord(c) + 6)
    sav4 = ''
    for c in username:
        sav4 += chr(ord(c) + 10)
    res = ''
    for c in sav4:
        res += hex(ord(c))[2:]
    print(res)
    """
    res = ''
    for c in username:
        res += hex(ord(c) + 10)[2:]
    print(res.upper())


def Rith_1_71():
    magic_str = '31415926535897932384'
    username = 'soundfuture'
    serials = ''
    for i in range(len(username)):
        eax = (ord(username[i]) % ord(magic_str[i])) * 2
        if eax > 0x7b:
            eax -= 0x1a
        if eax < 0x41:
            eax = 0x82 - eax
        if 0x5b < eax < 0x61:
            eax = (eax % 0xa) + 0x30
        serials += chr(eax)
    try:
        print(serials)
    except Exception:
        print("该用户名无法生成可输入的序列号")


def asm_cm01_72():
    username = 'soundfuture'
    """
    骗人的注册码算法，事实上魔改了messagebox，用来跳到真正的算法
    ecx = 0
    sav1 = ''
    for c in username+'\x00':
        ecx += 1
        eax = ((ecx * len(username)) + 0x17) ^ 0xf
        sav1 += str(eax)
    print(sav1)
    """

    eax = int.from_bytes(username[:2].encode(), 'little')
    eax ^= 0xe32f
    eax = (eax * eax) & 0xffff
    eax ^= 0xab6c
    # print(hex(eax))
    ecx = 0
    res = ''
    for i in range(len(username)):
        edx = (ord(username[i]) * (eax & 0xff) * ((eax & 0xff00) >> 8) & 0xffff) ^ 0x45eb
        edx //= 4
        edx += edx
        ecx += 1
        if ecx % 2:
            res += hex(edx)[2:].lower()
        else:
            res += hex(edx)[2:].upper()
    print(res)


def fireworx_9_81():
    magic_num = 0xA595a  # 该值是每次启动程序是通过random随机生成的，所以只能在运行程序后获得并填在此处
    ecx = 0x78c
    eax = (magic_num // ecx) * 0x399 * (2 ** 0x11)
    eax = eax & 0xffffffff
    eax //= 2 ** 9
    eax //= 0xc
    print(eax)


def phox_1_82():
    username = 'soundfuture'
    username = username.upper()
    res = ord(username[0]) * len(username) * (2 ** 0xc) + 0x3930e
    res &= 0xffffffff
    res -= 0x14
    print(res)


def Pusillus_83():
    magic_str = '\x71\x18\x59\x1B\x79\x42\x45\x4C'
    serials = ''

    al = 0
    for c in magic_str:
        al ^= ord(c)
    for c in magic_str:
        serials += chr(al ^ ord(c) ^ 0x32)
    print(serials)
    """
    alphabet = [chr(i) for i in range(ord('0'), ord('9') + 1)]
    alphabet.extend([chr(i) for i in range(ord('a'), ord('z') + 1)])
    alphabet.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    serials = '12345678'

    def algorithm(serials,magic_str):
        # 正向的算法，要求最后serials和magic_str相等才行
        if len(serials) != 8:
            print('not suggested, for there may be errors that are not unpredictable')
        res = ''
        for c in serials:
            res += chr(ord(c) ^ 0x32)
        serials = res
        sav1 = ''
        for i in range(0, len(serials), 2):
            sav1 += chr(ord(serials[i]) ^ ord(serials[i + 1]))
        al = 0
        for c in sav1:
            al ^= ord(c)
        res = ''
        for c in serials:
            res += chr(ord(c) ^ al)
        if res != magic_str:
            return False
        else
            return True
    """

    # 这题的逆向算法很有意思，不需要暴力破解，实际上只需要以下几行即可得到需求字符串
    # 简单说一下原理，首先源程序把serials每个字符异或0x32
    # 随后让sav1为每两个在serials中连续的字符异或，因此得到了4个字符。然而，这等价于直接操作原来的serials，因为0x32在这个过程中或异或8次，会被消掉
    # 随后al是sav1中每个字符异或，由于sav1[0] = serials[0] ^ serials[1](0x32消了)，后面sav1[1,2,3]同理。
    # 所以al等于serials中所有字符异或
    # 所以就res就等于serials中每个字符与serials中全字符异或
    # 那么已知magic_str，想求出al，只需要得到magic_str中所有字符异或的结果即可
    # 后面就不言自明了

    al = 0
    for c in magic_str:
        al ^= ord(c)
    for c in magic_str:
        serials += chr(al ^ ord(c) ^ 0x32)
    print(serials)


def KeyMe1_84():
    import os
    name = os.environ.get("COMPUTERNAME")
    print("想要破解该程序要分为两步，第一步需要修改你的剪切板，第二步才是生成reg.dat")
    print("首先复制下一行冒号右侧的字符，以修改你的剪切板，复制后单击程序的CHECK以通过第一层校验")
    print("请复制:{}".format(name))

    sav1 = 0
    for c in name:
        sav1 += ord(c)
    # print(hex(sav1))

    alphabet = [chr(i) for i in range(ord('0'), ord('9') + 1)]
    alphabet.extend([chr(i) for i in range(ord('a'), ord('z') + 1)])
    alphabet.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    serials = ''

    def calcu(serials):
        return int.from_bytes(serials[:4].encode(), 'little') ^ int.from_bytes(serials[4:].encode(), 'little')

    flag = [0]  # 标志是否找到有效序列号，用列表是因为列表是对象传递而不是值传递，适合当全局变量使
    print("查找有效序列号中...")

    def search(serials, flag):
        if flag[0]:
            return
        if len(serials) == 8:
            if calcu(serials) == sav1:
                print("找到有效序列号{}".format(serials))
                with open(r"F:\逆向学习相关\160 crack me_new\解压后\84\reg.key", 'w') as f:
                    f.write(serials)
                flag[0] = 1  # 终止
            return

        for c in alphabet:
            serials += c
            search(serials, flag)
            serials = serials[:len(serials) - 1]

    search(serials, flag)


def easycrackme_85():
    username = 'soundfuture'
    serials = ''
    magic_data = [
        0x26, 0x11, 0x79, 0x19, 0x07, 0x10, 0x79, 0x19, 0x79, 0x19, 0x26, 0x11, 0x79, 0x19, 0x07, 0x10,
        0x78, 0x56, 0x34, 0x12, 0xf0, 0xde, 0xbc, 0x9a, 0x34, 0x34, 0x12, 0x12, 0x78, 0x78, 0x78, 0x78,
        0xc6, 0xcc, 0xc6, 0xcc, 0x00, 0xcc, 0x00, 0xcc, 0xff, 0xef, 0xef, 0xff, 0x55, 0x55, 0xcc, 0xdd,
        0x89, 0x87, 0x67, 0x67, 0xcc, 0xcb, 0xce, 0xce, 0xab, 0x99, 0x88, 0x77, 0x66, 0x77, 0x33, 0x44
    ]
    esi = 0
    for i in range(len(username)):
        esi += i * ord(username[i])
    ebx = len(username) * 2 + 0x63
    ebx &= 0xffff
    esi &= 0xffff
    ebx *= 2 ** 0x10
    ebx = esi + ebx
    esi = ebx & 0xf
    print(hex(esi))
    ebx = magic_data[4 * esi] + (magic_data[4 * esi + 1] << 8) \
          + (magic_data[4 * esi + 2] << 16) + (magic_data[4 * esi + 3] << 24)
    print(ebx)


def CrackMe_86():
    import random
    username = 'thebluefat'

    """
    serials = '1234567890123456'
    # 原算法，程序写的比较恶心人，虽然实际上只是对serials每一位的合法性判断罢了，但最后那个全通过的标志比较有意思
    # 因为只要全通过，res一定等于0xfff，反之不然
    def algorithm(username, serials):
        magic_str = 'HT-7'
        res = 0
        for i in range(4):
            if serials[i] == magic_str[i]:
                res |= 1 << i
        if ord(serials[4]) + ord(serials[6]) == ord(serials[9]) + ord(serials[10]):
            res |= 0x10
        ascii_sum = sum([ord(c) for c in username])
        if ascii_sum // len(username) == ord(serials[5]):
            res |= 0x20
        if ord(serials[7]) + ord(serials[8]) == ord(username[1]) + ord(username[len(username) - 2]):
            res |= 0x40
        if (ord(serials[9]) + ord(serials[10])) % 2 == 0:
            res |= 0x80
        if (ord(serials[0xb]) - 0x30 == len(username)) % 3:
            res |= 0x100
        if (ord(serials[0xc]) + ord(serials[5])) % 2 == 1:
            res |= 0x200
        if ord(serials[0xc]) + ord(serials[0xd]) + ord(serials[0xe]) + len(username) == 0x10a:
            res |= 0x400
        if ord(serials[0xf]) == ord(username[len(username) - 2]):
            res |= 0x800
        if res == 0xfff:
            return True
        else:
            return False

    algorithm(username, serials)
    """

    def search(username):
        alphabet = [chr(i) for i in range(ord('0'), ord('9') + 1)]
        alphabet.extend([chr(i) for i in range(ord('a'), ord('z') + 1)])
        alphabet.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
        serials = 'HT-7'
        result_dict = {}

        result_dict[4] = result_dict[9] = random.choice(alphabet)
        for b in alphabet:
            if (ord(result_dict[4]) + ord(b)) % 2 == 0:
                result_dict[6] = result_dict[10] = b

        result_dict[5] = sum([ord(c) for c in username]) // len(username)
        if result_dict[5] < 0x20 or result_dict[5] >= 0x7f:
            print("该用户无法生成可输入的密钥")
            return
        result_dict[5] = chr(result_dict[5])

        result_dict[7] = username[1]
        result_dict[8] = username[len(username) - 2]

        result_dict[0xb] = chr(len(username) % 3 + 0x30)

        for c in alphabet:
            if (ord(c) + ord(result_dict[5])) % 2 == 1:
                result_dict[0xc] = c

        flag = False
        for a in alphabet:
            for b in alphabet:
                if ord(a) + ord(b) == 0x10a - len(username) - ord(result_dict[0xc]):
                    result_dict[0xd] = a
                    result_dict[0xe] = b
                    flag = True
        if flag is False:
            print("该用户无法生成可输入的密钥")
            return

        result_dict[0xf] = username[len(username) - 2]

        for i in range(4, 0x10):
            serials += result_dict[i]
        return serials

    res = search(username)
    if res is not None:
        print(res)


def D4ph1_Crackme_2_87():
    username = 'thebluefat'
    serials = ''
    sav1 = ''
    for c in username:
        sav1 += hex(ord(c))[2:].upper()
    sav2 = ''

    def mem_write(input_string, idx, add):
        if idx == len(input_string):
            return input_string + add
        elif idx == len(input_string) - 2:
            return input_string[:-2] + add
        else:
            return input_string[:idx] + add + input_string[idx + 2:]

    esi = ebp = edi = counter = 0
    sav1_t = sav1 + '\x00'
    for i in range(len(sav1)):
        if sav1_t[i + ebp] == sav1_t[i + 1 + ebp]:
            esi += 1
            counter += 1
            ebp += 1
            if counter != 1:
                edi -= 2
                esi += 1
        elif counter > 1:
            edi -= 2
        else:
            counter = 0
            esi = 1
        sav2 = mem_write(sav2, edi, int.to_bytes(esi, 1, 'little').decode() + sav1_t[i + ebp])
        edi += 2
        if sav1_t[i + ebp + 1] == '\x00':
            break

    ecx = esi = 1
    sav3 = ''
    while ecx <= len(username):
        ebx = ord(sav2[esi - 1]) + (ord(sav2[esi]) << 8)
        eax = ord(username[ecx - 1])
        eax = eax + ebx - ecx
        edx = eax % ecx
        eax //= ecx
        eax = eax - len(sav2) + edx
        ebx += ecx
        eax ^= ebx
        sav3 += chr(eax & 0xff)

        esi += 1
        if esi >= len(sav2):
            esi = 1
        ecx += 1

    for c in sav3:
        eax = ((ord(c) // (2 ** 4)) & 0xf) + 0x30
        serials += chr(eax) if eax <= 0x39 else chr(eax + 7)
        eax = (ord(c) & 0xf) + 0x30
        serials += chr(eax) if eax <= 0x39 else chr(eax + 7)
    print(serials)


def CrackMe_88():
    username = 'soundfuture'
    magic_str = 'KEY-KANON'
    esi = 0
    for c in username:
        esi += ord(c)
    edi = 0
    for i in range(9):
        edx = (ord(magic_str[i]) * esi) % 0x1a
        edx = (edx + 0x61) ^ 0xaa
        edi += edx

    serials = ''
    for c in magic_str:
        serials += chr(((ord(c) * esi) % 0x1a) + 0x61)
    print(serials)

    """
    # serials处理程序段
    serials = '123456'
    edi = 0
    for i in range(9):
        if i >= len(serials):
            edx = 0
        else:
            edx = ord(serials[i])
        edi += edx ^ 0xaa
    """

    """
    效率很低的搜索
    alphabet = [chr(i) for i in range(ord("0"), ord('9') + 1)]
    alphabet += "\x00"
    def search(res, sum, level):
        if sum < 0:
            return 1
        if sum == 0:
            print(res)
            return 0
        if level == 9:
            return 1
        if len(res) != 0 and res[-1] == '\x00':
            res += '\x00'
            sum -= 0xaa
            if search(res,sum,level+1) == 0:
                return 0
        else:
            if level == 0:
                for c in tqdm.tqdm(alphabet):
                    res += c
                    sum -= 0xaa ^ ord(c)
                    if search(res,sum,level+1) == 0:
                        return 0
                    res = res[:len(res) - 1]
                    sum += 0xaa ^ ord(c)
            else:
                for c in alphabet:
                    res += c
                    sum -= 0xaa ^ ord(c)
                    if search(res,sum,level+1) == 0:
                        return 0
                    res = res[:len(res) - 1]
                    sum += 0xaa ^ ord(c)
        return 1
    search('', edi, 0)
    """


def fornixcrackme1_89():
    import os
    username = 'soundfuture'
    # lpVolumeNameBuffer = '系统'  # 通过GetVolumeInformation获得
    lpVolumeNameBuffer = os.popen("wmic VOLUME WHERE DriveLetter='c:' GET Label").read().split('\n')
    if '' in lpVolumeNameBuffer:
        lpVolumeNameBuffer.remove('')
    sav1 = lpVolumeNameBuffer[1] + username
    sav1 = sav1.encode('gbk')
    sav3 = ''
    for i in range(4):
        sav3 += chr(((((sav1[i] ^ ord(username[i])) & 0x5f) | 0x40) ^ 9))
    sav3 += chr(0x24)
    for i in range(4):
        sav3 += chr(((((sav1[i] ^ ord(username[i])) & 0x3f) | 0x30) ^ 9))
    serials = ''
    for c in sav3:
        serials += chr(ord(c) ^ 9)
    print(serials)


def tc_12_90():
    magic_str2 = [0x3a, 0xd9, 0xc4, 0xc9, 0xba, 0xbf, 0xde, 0x7d, 0x44, 0xcf, 0xe2, 0xd9, 0xea, 0x49,
                  0xd2, 0xdd, 0xde, 0x8f]
    """
    serials = '123456789012345678'
    magic_str1 = '\x10\x70\x30\x02'
    原汇编算法
    def calcu(serials):
        sav1 = []
        for c in magic_str1:
            sav1.append(c)
        for c in serials:
            sav1.append(c)
            for i in range(3):
                sav1.append(' ')

        for i in range(len(serials)):
            sav1[i*4+4] = (ord(sav1[i*4+4]) ^ 3) * 2
        sav2 = ''
        for i in range(len(serials)):
            sav2 += chr(sav1[i*4+4] + 8 - (i + 1))
        sav3 = ''
        for i in range(len(sav2)-1, 0,-1):
            sav3 += sav2[i]
    """

    temp1 = ''
    for i in range(len(magic_str2) - 1, 0, -1):
        temp1 += chr(magic_str2[i])
    temp2 = ''
    for i in range(len(temp1)):
        temp2 += chr(ord(temp1[i]) - 8 + (i + 1))
    serials = ''
    for i in range(len(temp2)):
        serials += chr((ord(temp2[i]) // 2) ^ 3)

    # calcu(serials)
    print(serials)


def crackme2_91():
    username = 'soundfuture'
    magic_str1 = 'biq2jrxc-ape3*dsynhz8gt5o7f0uml4v19w6+/k'
    magic_str2 = '-apeoiq2jrml4xcsw6ynh7f0uv19+3/k*dbz8gt5'
    magic_str3 = 'h7f0uv19+3/kjrml4xcsw6yn*dbz8gt5-apeoiq2'
    sav1 = ''
    for i in range(len(username)):
        edx = ord(username[i]) * 41 % 0x28
        sav1 += magic_str1[edx]

    for i in range(len(username)):
        edx = ord(username[i]) * (2 ** 5 - 1) % 0x28
        sav1 += magic_str2[edx]
    serials = ''
    for i in range(len(sav1)):
        edx = ord(sav1[i]) * 11 % 0x28
        serials += magic_str3[edx]
    print(serials)


def CRACKME6_92():
    import random
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    alphabet.extend([chr(i) for i in range(ord("A"), ord('Z') + 1)])
    alphabet.extend([chr(i) for i in range(ord("0"), ord("9") + 1)])
    serials = []
    for i in range(10):
        serials.append(random.choice(alphabet))
    serials[5] = chr(0x31)
    serials[8] = chr(0x33)
    serials[9] = 'd'
    serials = ''.join(serials)
    print(serials)

    with open(r"F:\逆向学习相关\160 crack me_new\解压后\92\keyfile.dat", 'w') as f:
        f.write(serials)


def cm_93():
    username = 'soundfuture'
    """
    serials变形过程
    serials = '12345678'
    if len(serials) != 8:
        print("error")
        return 0
    eax = 0
    for i in range(len(serials)):
        eax = eax << 4
        eax += int(serials[i])
    """

    edx = 0x12dfd16
    for c in username:
        edx += (ord(c) ^ 0xca) & 0xff
    edx ^= 0x19840808
    print(hex(edx)[2:].upper())


def TheBigMans_Crackme_6_94():
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    alphabet.extend([chr(i) for i in range(ord("A"), ord('Z') + 1)])
    alphabet.extend([chr(i) for i in range(ord("0"), ord("9") + 1)])

    username = 'theblue'
    serials = ''
    """
    def signed_compare(a, b):
    # 以有符号数的形式比较输入两个4字节数据的大小，a>b返回1，相等返回0.否则为-1
    if a == b:
        return 0
    elif a & 0x80000000 != 0 and b & 0x80000000 == 0:
        return -1
    elif a & 0x80000000 == 0 and b & 0x80000000 != 0:
        return 1
    elif a & 0x80000000 == 0 and b & 0x80000000 == 0:
        return 1 if a > b else -1
    else:
        return -1 if a > b else 1
        
    # 这段代码实际含义是检测username的长度，经过反向计算（遍历）可以知道，username最长为9
    eax = 0x48 // len(username)
    esi = (0x30 - eax) * 5
    edi = (0x2bc - esi) * 0x6b - 0xcf6c & 0xffffffff
    print(hex(edi))

    compare_res = signed_compare(edi,0x2300)
    if compare_res == 0 or compare_res == -1:
        compare_res = signed_compare(edi, 0x190)
        if compare_res == 0 or compare_res == 1:
            print('pass')
    return 0
    """
    if len(username) > 9 or len(username) < 3:
        print("username too long")
        return 0

    for c in alphabet:
        if 0x11cf % ord(c) == 0x17:
            serials += c
            break

    sav1 = 0
    for c in username:
        sav1 += ord(c)

    magic_str1 = '\x00ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for ebx in range(len(username)):
        edi = ord(username[ebx])
        esi = sav1
        ecx = ord(magic_str1[ebx * 3])
        edx = edi ^ ecx
        esi = ((esi * ebx - esi) & 0xffffffff) ^ 0xffffffff
        esi = edx + esi + 0x14d
        ecx = len(username) * (ebx + 3) * edi
        eax = esi + ecx & 0xffffffff
        edi = (eax % 10 + 0x30) ^ 0xadac
        eax = edi * (ebx + 2)
        edx = (eax % 10) + 0x30
        res += chr(edx)
    res = 'T' + res
    edi = ((len(username) * sav1) % 0x64) + 0x30
    res += '-' + str(edi)
    for i in range(1, len(res)):
        serials += chr((ord(res[i]) ^ 0x20) % 0xa + 0x30)
    print(serials)


def crackme1_1_95():
    username = 'sakura'
    serials = ''
    # 这里magic_str实际上代表一个标志位集合，从0~255都用一位来代替。其中，magic_str1标志数字，大写,小写字母的那些位被置1了
    magic_str1 = [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x03, 0xfe, 0xff, 0xff, 0x07, 0xfe, 0xff, 0xff, 0x07,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    # magic_str2中去除了数字的部分，只保留代表大写和小写字母的位
    magic_str2 = [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xfe, 0xff, 0xff, 0x07, 0xfe, 0xff, 0xff, 0x07,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ]

    def bt(a, b):
        target_byte = a[b // 8]
        idx = b % 8
        cover = 1 << idx
        if target_byte & cover != 0:
            return 1
        else:
            return 0

    for c in username:
        if bt(magic_str1, ord(c)) == 0 or bt(magic_str2, ord(c)) == 0:
            print("不是合法的用户名输入,仅可包含大写，小写字母")
            return 0

    for esi in range(len(username)):
        edx = len(username) * 3 - (esi + 1) * 2 - 0x14 + ord(username[esi])
        edx = edx & 0xff
        if bt(magic_str1, edx) == 1:
            serials += chr(edx)

    reve_username = ''
    for i in range(len(username) - 1, -1, -1):
        reve_username += username[i]

    for esi in range(len(reve_username)):
        edx = len(username) * 3 - (esi + 1) * 3 - 0x14 + ord(reve_username[esi])
        edx = edx & 0xff
        if bt(magic_str1, edx) == 1:
            serials += chr(edx)

    sav1 = ['\x00']
    for c in username:
        sav1.append(c)

    flag = 0
    esi = 1
    while flag == 0:
        flag = 1
        for eax in range(1, len(sav1) - esi):
            flag = 0
            if ord(sav1[eax]) <= ord(sav1[eax + 1]):
                continue
            edx = sav1[eax + 1]
            ecx = sav1[eax]
            sav1[eax + 1] = ecx
            sav1[eax] = edx
        esi += 1
    sav1 = ''.join(sav1[1:])

    for esi in range(len(sav1)):
        edx = ((len(username) - 3) ** 2) - ((esi + 1) * 2) - 0x14 + ord(sav1[esi])
        edx &= 0xff
        if bt(magic_str1, edx) == 1:
            serials += chr(edx)
    print(serials)


def xtfK1_96():
    local5 = 0x60ff5c
    local6 = 0x401220
    local7 = 0x401220

    username = 'thebluefat'
    for i in range(len(username)):
        edx = ord(username[i]) * 5 * 16
        local5 += edx
        local6 = (local5 + local6) ^ 0x32
        local7 += local6 * 4
        local8 = local6 + local5 + local7
    print(hex(local8)[2:])


def fireworx_11_97():
    username = 'soundfuture'
    serials = '123456'
    for edi in range(6):
        esi = (edi >> 0xe) ^ edi
        esi += 0x2F21A0 + 0x795CE
        sav1 = str(esi)
        eax = esi // 0x49 - 0xbba
        sav2 = str(eax)
        eax = esi // 0x130 * 4 * 5
        eax = (eax ^ int(sav2)) + 0x10f
        sav3 = str(eax)
        print('VL - -{}..{}.-{}.'.format(sav1,sav2,sav3))


def DueList_4_98():
    magic_str1 = 'A1LSK2DJF4HGP3QWO5EIR6UTYZ8MXN7CBV9'
    magic_str2 = 'SU7CSJKF09NCSDO9SDF09SDRLVK7809S4NF'
    username = 'sound'
    serials = ''
    if 0 == len(username) or len(username) > 8:
        print("username too long or empty")
        return 0
    for i in range(len(username)):
        c = username[i]
        if ord(c) < 0x41 or ord(c) >0x7a:
            print("invalid username")
            return 0
        c = c.upper()
        idx = magic_str1.find(c)
        serials += magic_str2[idx]
    print(serials)


def figugegl_2b_99():
    username = 'thebluefat'
    serials = ''
    for edi in range(len(username)):
        edx = ord(username[edi]) ^ edi
        ecx = len(username) ^ edi
        edx += ecx
        if edx < 0x20:
            serials += chr(edx + 0x20)
        elif edx >= 0x80:
            serials += chr(0x20)
        else:
            serials += chr(edx)
    temp = serials
    serials = ''
    for i in range(len(temp) - 1, -1, -1):
        serials += temp[i]
    print(serials)


def ECRACKME_100():
    serials = ''
    machine_code = 0  # 直接运行程序会显示机器码。但根据评论机器码是可以算出来的，这里我就不深究其算法过程了
    magic_num1 = 0x4B4EB28 ^ machine_code
    magic_num2 = 0x22F16632 ^ machine_code
    magic_num3 = 0x2CF062E0 ^ machine_code
    magic_num4 = 0x6C21D6B ^ machine_code
    serials += str(magic_num1)[1:5] + ' '
    serials += str(magic_num2)[1:5] + ' '
    serials += str(magic_num3)[1:5] + ' '
    serials += str(magic_num4)[1:5]
    print(serials)


def serialme_101():
    import random
    # serials = '123456789012'
    serials = []
    for i in range(0xc):
        serials.append('*')
    serials[5] = '3'
    serials[2] = '-'
    serials[11] = '1'
    serials[3] = '1'
    serials[9] = '0'
    serials[6] = '9'
    serials[7] = '3'
    serials[10] = random.choice([chr(i) for i in range(ord('0'), ord('9')+1)])


    """
    # 后面只会用到ebx的bh部分
    ebx = 0x401115

    def div(a,b):
        ax = a & 0xffff
        eax_high = a & 0xffff0000
        al = ax // b
        ah = ax % b
        a = eax_high + (ah << 8) + al
        return a

    eax = 0
    for c in serials+'\x00':
        eax = (eax & 0xffffff00) + ord(c)
        if ord(c) == 0:
            break
        eax = div(eax,2)
        if eax & 0xff00 == 0:
            ebx += 0x100
    ebx = ebx << 8
    sav1 = eax
    """

    """
    # 用于通过校验的算法
    edx = len(serials)
    eax = 1
    cl = 2
    while True:
        if eax >= len(serials):
            break
        edx += ord(serials[eax])  # eax = 1, 4, 8
        cl += 1
        eax += cl
    """

    target = 0xab - len(serials)
    remain = target % 3
    generate_char = target // 3
    if remain != 0:
        serials[1] = serials[4] = chr(generate_char)
        serials[8] = chr(generate_char + remain)
    else:
        serials[1] = serials[4] = serials[8] = chr(generate_char)
    for i in range(len(serials)):
        if serials[i] == '*':
            serials[i] = random.choice([chr(i) for i in range(ord('0'), ord('9')+1)])
    serials = ''.join(serials)
    print(serials)






if __name__ == '__main__':
    crackme8_49()
