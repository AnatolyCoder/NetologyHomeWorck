first_file = open('1.txt', 'r', encoding='utf-8')
second_file = open('2.txt', 'r', encoding='utf-8')
third_file = open('3.txt', 'r', encoding='utf-8')

class File_Item:
    def __init__(self, file_name, file_content):
        self.file_name = file_name
        self.file_content = file_content
    def __str__(self):
        return self.file_name + '\n' + str(len(self.file_content))

item_to_sort_first = File_Item('1.txt', first_file.readlines())
item_to_sort_second = File_Item('2.txt', second_file.readlines())
item_to_sort_third = File_Item('3.txt', third_file.readlines())

list_file = [item_to_sort_third, item_to_sort_second, item_to_sort_first]
sorted_list_file = sorted(list_file, key=lambda x: len(x.file_content), reverse=True)

for i in sorted_list_file:
    print(i)
    for n in i.file_content:
        print(n)

first_file.close()
second_file.close()
third_file.close()



