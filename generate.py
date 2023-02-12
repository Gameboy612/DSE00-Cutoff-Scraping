import pyperclip
output = "{"

with open("settings/data.txt", "r") as f:
    raw = f.readlines()
    for i in range(len(raw) - 1):
        raw[i] = raw[i][:-1]
    i = 0
    year = 0
    while i < len(raw):
        line = raw[i]
        if line[0:2] == '20' and len(line) == 4:
            year = line
            output += year + ':{'
            j=3
            score = 7
            while i+j < len(raw) and not (len(raw[i+j]) == 4 and raw[i+j][0:2] == '20'):
                if raw[i+j+1][0] == '(' and raw[i+j+1][-1] == ')':
                    output += f"{score}:{raw[i+j+1][1:-1]},"
                    score -= 1
                j += 2
            output += '},'
            i += j - 1
        i += 1
output += "}"
print(output)
pyperclip.copy(output)