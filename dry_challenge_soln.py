#create grouping for 1's, 10',, 100;,
ones=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens=['Zero','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
hunnids=[' ','Thousand','Million','Billion','Thrillion']

def sub_thousands(input):
    num = int(input)
    if 0 <= num < 19:
        return ones[num]
    elif 20 <= num <= 99:
        if input[-1] == '0':
            return tens[int(input[0])]
        else:
            return tens[int(input[0])] + " " + ones[int(input[1])]
    elif 100 <= num <= 999:
        remainder = num % 100
        digits = num / 100
        if remainder == 0:
            return ones[digits] + " Hundred"
        else:
            return ones[digits] + ' Hundred ' + sub_thousands(str(remainder))
    
    
# handle thousand digits
def handle_thousands(input):
    num=int(input)
    arr_zer = split_thousand(num)
    len_arr=len(arr_zer)-1
    result_arr=[]
    for x in arr_zer[::-1]:
        word = sub_thousands(str(x)) + " "
        hun = hunnids[len_arr] + ", "
        if word == " ":
            break
        elif word == "Zero ":
            word, hun = "", ""
        result_arr.append(word + hun)
        len_arr-=1
    result_arr = "".join(result_arr).strip()
    if result_arr[-1] == ",": result_arr = result_arr[:-1]
    return result_arr

def split_thousand(input):
    num = int(input)
    arr_thou=[]
    while num != 0:
        arr_thou.append(num % 1000)
        num /= 1000
    return arr_thou

#####################################################################
#import unittest
#
#class TestDry(unittest.TestCase):
#    def test_ones(self):
#        self.assertEqual(sub_thousands(2),"Two")
#    def test_hundreds(self):
#        self.assertEqual(sub_thousands(423),"Four Hundred Twenty Three")
#    def test_thousands(self):
#        self.assertEqual(handle_thousands(1000),"One Thousand")
#        self.assertEqual(handle_thousands(5672),"Five Thousand, Six Hundred Seventy Two  ")
#        self.assertEqual(handle_thousands(45781),"Forty Five Thousand, Seven Hundred Eighty One  ")
#    def test_not_ones(self):
#        self.assertFalse(sub_thousands(101)=="Two")
#    def test_not_hundreds(self):
#        self.assertFalse(sub_thousands(200)=="Three Hundred")
#    def test_not_thousands(self):
#        self.assertFalse(handle_thousands(3)=="Three Thousand")
#
#if __name__ == "__main__":
#    unittest.main()
#main block
strnumeric=raw_input(" Enter a number\n ")
input = int(strnumeric)
if input < 0:
    print "Minus",
    input *= -1
    
    strnumeric=strnumeric[1:]
if (input) < 1000:
    print sub_thousands(strnumeric)
else:
    print handle_thousands(strnumeric)
