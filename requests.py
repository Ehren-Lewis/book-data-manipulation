import requests
import main
import json


def tree_to_json(tree):
    root_value = tree.value
    for i in tree.children:
        pass

if __name__ == "__main__":
    main.set_pandas_options()
    df = main.create_dataframe(r'./books_new.csv')
    new_df = df.sort_values(by=['Genre', 'SubGenre'])
    grouped = new_df.groupby(['Genre'])
    list_of_grouped_books = list(grouped)
    genre_information = new_df.Genre.unique()
    current_tree = main.create_tree(genre_information, list_of_grouped_books)

    print(current_tree.value)

# print(main.current_tree.children)


#
#
# for i in main.current_tree.children:
#     for j in i.children:
#         print(type(j.children))

# tree_to_json(main.current_tree)