# Write a function
# Input: an integer n, 0 <= n <= 1000
# Output: a Am. English natural language expression of the integer value

# Example: 0 => "Zero"
# Example: 817 => "Eight-Hundred Seventeen"

def solution(N):
    NumToWord0 = {'0': '', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
    '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
    NumToWord1 = {'0': 'Ten', '1': 'Eleven', '2': 'Twelve', '3': 'Thirtheen', '4': 'Fourteen',
    '5': 'Fifteen', '6': 'Sixteen', '7': 'Seventeen', '8': 'Eighteen', '9': 'Nineteen'}
    NumToWord2 = {'0': '', '1': 'Ten', '2': 'Twenty', '3': 'Thirty', '4': 'Fourty', '5': 'Fifty',
    '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'}
    
    if N==0:
        return "Zero"
    elif N==1000:
        return "One-Thousand"
    elif N<0 or N>1000:
        return "Error: the number is out of bound"
    strN = str(N)
    length = len(strN)

    out = ''
    Pos = 0

    for i in reversed(str(N)):
        Pos += 1
        if length > 1 and strN[-2] == '1' and Pos == 1:
            out = NumToWord1[i]
            continue
        elif length > 1 and strN[-2] == '1' and Pos == 2:
            continue

        if Pos == 1:
            out = NumToWord0[i]
        elif Pos == 2:
            out = NumToWord2[i] + " " + out
        elif Pos == 3:
            out = NumToWord0[i] + "-Hundred " + out
    return out