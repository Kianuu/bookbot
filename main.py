def main():
    with open("books/frankenstein.txt") as f:
        files_contents = f.read()
        alist = files_contents.split()
        char_dict = {}
        for item in alist:
            x = item.lower()
            for i in x:
                if i.isalpha():    
                    if i in char_dict:
                        char_dict[i] += 1
                    else:
                        char_dict[i] = 1
    print(f"{len(alist)} words found in the document\n")
    while char_dict != {}:
        x = max(char_dict, key=char_dict.get)
        y = char_dict[x]
        print(f"The '{x}' character was found {y} times")
        del char_dict[x]

    print("--- End report ---")

main()
