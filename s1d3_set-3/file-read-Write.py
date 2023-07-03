def countWord(text):
    words=text.split()
    print(words)
    print(type(words))
    return len(words)


input_file_name = "input.txt"
with open(input_file_name, "r") as input_file:
    file_contents = input_file.read()


word_count = countWord(file_contents)

print(word_count)

file_writer_name="worldCount.txt"


with open(file_writer_name, "w") as file_writer:
    file_writer.write("Number of word is "+str(word_count))


print(file_writer)