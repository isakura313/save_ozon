filename = 'data_t.txt'
file_output = "result.html"

#итого, у нас здесь пример того, как читать файл, если у него допустим
# все располагается

file_string = ''

with open(filename) as file_object:
    for line in file_object:
        file_string += line.strip()

file_arr = file_string.split(', ')
print(file_arr)

with open(file_output, 'w') as file_out:
    file_out.write(
    '<!DOCTYPE html>'
 '<html lang="en">'
'<head>'

'</head>'
'<body>'
    '<h1>'+
    file_string+
    '</h1>'
'</body>'
'</html>' )

