# -*- coding: utf-8 -*-
import os


TARGET_FILE = "<Path to ALAR file>"

MAX_FILENAME_LEN = 50
ALAR_CONTENT = None
RESULT_DIR = None


def getFileName(startPos):
    fileName = []
    for c in ALAR_CONTENT[startPos:startPos+MAX_FILENAME_LEN]:
        if c == 0:
            break
        else:
            fileName.append(chr(c))

    return "".join(fileName)


def searchRecordHeader(marker, content, offset):
    result = None

    try:
        result = content[offset:].find(marker)
        result += offset
    except Exception:
        result = -1

    return result


if __name__ == '__main__':

    with open(TARGET_FILE, "br") as f:
        ALAR_CONTENT = f.read()

    fileType = ALAR_CONTENT[0x5]
    fileType2 = ALAR_CONTENT[0x6]
    if 0x41 == fileType or 0x49 == fileType:
        # Event txt
        RESULT_DIR = ".\\Event.txt"
        next_offset = 0x28
        firstRecordHeader = ALAR_CONTENT[0x8:0xC]
        lastRecordHeader = ALAR_CONTENT[0xC:0x10]
        data_addr_offset = 0x4
        data_size_offset = data_addr_offset + 0x4
        file_name_offset = data_size_offset + 0xA
        pass
    elif 0x45 == fileType and 0x03 == fileType2:
        # Harlem ATX
        RESULT_DIR = ".\\Harlem.atx"
        next_offset = 0x28
        firstRecordHeader = ALAR_CONTENT[0x7:0xB]
        lastRecordHeader = ALAR_CONTENT[0xB:0xF]
        data_addr_offset = 0x5
        data_size_offset = data_addr_offset + 0x4
        file_name_offset = data_size_offset + 0xA
        pass
    elif 0x45 == fileType and 0x04 == fileType2:
        # CARD ATX
        RESULT_DIR = ".\\Card.atx"
        next_offset = 0x24
        firstRecordHeader = ALAR_CONTENT[0x7:0xB]
        lastRecordHeader = ALAR_CONTENT[0xB:0xF]
        data_addr_offset = 0x5
        data_size_offset = data_addr_offset + 0x4
        file_name_offset = data_size_offset + 0xA
        pass
    else:
        pass

    os.makedirs(RESULT_DIR, exist_ok=True)

    search_offset = 0x10
    target_addr = searchRecordHeader(firstRecordHeader, ALAR_CONTENT, search_offset)
    while True:
        data_addr = int.from_bytes(ALAR_CONTENT[target_addr+data_addr_offset:target_addr+data_addr_offset+0x4], 'little')
        data_size = int.from_bytes(ALAR_CONTENT[target_addr+data_size_offset:target_addr+data_size_offset+0x4], 'little')
        file_name = getFileName(target_addr+file_name_offset)

        if 0 == len(file_name):
            break
        print("0x{0:x}: {1:s}".format(data_addr, file_name))

        output_file = "{0}/{1:s}".format(RESULT_DIR, file_name)

        # Write file
        if False == os.path.exists(output_file):
            with open(output_file, "wb") as f:
                f.write(ALAR_CONTENT[data_addr:data_addr+data_size])

        # 次の処理へ
        if lastRecordHeader == ALAR_CONTENT[target_addr:target_addr+0x4]:
            break
        else:
            target_addr += next_offset
