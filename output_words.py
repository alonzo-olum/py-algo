def output_words(num):
    ones=['zero','one', 'two', 'three', 'four','five','six','seven','eight',
            'nine','ten','eleven','twelve','thirtheen','fourteen','fifteen',
            'sixteen','seventeen','eighteen','nineteen']
    tens=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    thousands={100:'hundred',1000:'thousand',1000000:'million'}
    if num<20:
        return ones[num]
    if num<100:
        return tens[num/10-2] + ( '' if num%10 == 0 else ' ' + ones[num%10] )
    #finding the largest key in num subset
    maximumKey=max([key for key in thousands.keys() if key<=num])
    return output_words(num/maximumKey) +' '+ thousands[maximumKey] + ('' if num%maximumKey==0 else ' '+ output_words(num%maximumKey))

#main block
input=raw_input("Enter an integer\n")
print output_words(int(input))
