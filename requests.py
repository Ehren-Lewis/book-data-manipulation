import requests
import main
import json
from collections import defaultdict

def tree_to_json(tree):
    root_value = tree.value
    test_dict = {}

	
    #  list of genres   
    everything_dict = []
    for i in tree.children:
        # print(f"\ncurrent genre: {i.value}")
        
        genre_value = i.value

        # genre_dict = {}

     
        all_books_in_subgenre = []

    #  list of subgenres
        for j in i.children:
            # print(f"\ncurrent subgenre: {j.value}")
            subgenre_value = j.value

            #  all books in a subgenre
            books = [k.value for k in j.children]
            all_books_in_subgenre.append({subgenre_value: books})
        genre_dict = {genre_value: all_books_in_subgenre}

        everything_dict.append(genre_dict)

    
    # print({root_value: everything_dict})
    return {root_value: everything_dict}
    

if __name__ == "__main__":
    main.set_pandas_options()
    df = main.create_dataframe(r'./books_new.csv')
    new_df = df.sort_values(by=['Genre', 'SubGenre'])
    grouped = new_df.groupby(['Genre'])
    list_of_grouped_books = list(grouped)
    genre_information = new_df.Genre.unique()
    current_tree = main.create_tree(genre_information, list_of_grouped_books)

    final_dict = tree_to_json(current_tree)
    
    # for (key, value) in final_dict.items():

    #     for i in value:
    #         for (second_key, second_value) in i.items():
    #             print(second_key)
    #             # print(second_value, end="\n")

    #             for k in second_value:
    #                 for (third_key, third_value) in k.items():
    #                     print(third_key)
    #                     print(third_value)


# print(main.current_tree.children)


#
#
# for i in main.current_tree.children:
#     for j in i.children:
#         print(type(j.children))

# tree_to_json(main.current_tree)