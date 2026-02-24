import CSP_6_02_reading_files as HW

def test_to_string():
    assert HW.toString("newFile.txt") == \
           "Here is the text in file\nAnother line"

def test_longest_line():
    assert HW.longestLine("newFile.txt") == \
               "Here is the text in file\n"

def test_to_binary():
    assert HW.toBinary("binaryText.txt") == \
           ['10011001', '10011001', '']