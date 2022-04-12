c = input("Enter the language you want to find: ")
language=["Java","Python","HTML","CSS","C++","Shell"]
try:
    assert c in language
except:
    print("Language not being taught we will be adding it to our courses")
    language.append(c)
else:
    print("Languages that are being taught are: ")
    for i in range(len(language)):
        print(language[i])
print(language)