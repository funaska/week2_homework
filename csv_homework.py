from lesson_one import answers_dict
import csv

if __name__ == '__main__':
    with open('conversation.csv', 'w', encoding = 'utf-8') as csv_file:
        fields = ['question', 'answer']
        writer = csv.DictWriter(csv_file, fields, delimiter=';')
        # writer.writeheader()
        # print('\n', 'answers_dict', answers_dict, '\n')
        dict_items = answers_dict.items()
        # print('\n','dict_items:', dict_items,'\n')
        for conversation in dict_items:
            print('\n','current_item:',conversation,'\n')
            # print('answers_dict[conversation]:', answers_dict[conversation])
            writer.writerow(conversation)
