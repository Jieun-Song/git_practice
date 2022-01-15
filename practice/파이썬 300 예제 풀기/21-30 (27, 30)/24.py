string = "PYTHON"

string_len = len(string)
string_back = ""

for i in range(string_len):
    string_back = string_back + string[string_len - i - 1]

print(string_back)
