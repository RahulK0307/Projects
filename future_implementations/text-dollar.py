
Digits = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
          'Seven', 'Eight', 'Nine', 'Ten']

Tens_digits = { 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen',
               16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}

Tens_text = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty',
             7:'Seventy', 8:'Eighty', 9:'Ninety'}

Hundreds_Text = ['Hundred', 'Thousands', 'Lakhs']


def values_below_hundres(val):
    temp = val % 10
    teens = val//10
    for i in range(10):
        if temp == 0:
            temp = ""
        elif temp == i:
            temp = Digits[i]
    for k in Tens_text.keys():
        if teens == k:
            final =  Tens_text[k] + " " + temp + ' dollar'
            return final

def values_below_ten(val):
    for i in range(11):
            if val == i:
                return Digits[i] + ' dollar'

def values_below_twenty(val):
    try:
        for k in Tens_digits.keys():
            if val == k:
                return Tens_digits[k] + ' dollar'
    except:
        return "Please enter the value below to get values in Tens digits."

def text_with_dollar(digi):
    if digi <= 10:
        print values_below_ten(digi)

    elif digi < 20:
        print values_below_twenty(digi)

    elif digi < 100:
        print values_below_hundres(digi)
        
    elif digi >= 100 and digi < 1000:
        if (digi % 100) == 0:
            for i in range(10):
                if (digi // 100) == i:
                    print Digits[i] + ' hundreds dollar'
        else:
            m = digi % 100
            n = values_below_hundres(m)
            h = digi // 100
            for i in range(10):
                if h == i:
                    print Digits[i] + ' hundreds ' + n

try:
    digi = input("Enter your digit : ")
except:
    print "please enter the positive interger value ."


text_with_dollar(digi)
