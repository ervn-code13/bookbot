def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n")

    output = process_text(text)
    print_output(output)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def process_text(text):
    dict = {}

    for c in text:
      if c.isalpha():
        lowered_c = c.lower()
        if lowered_c in dict:
          dict[lowered_c] += 1
        else:
          dict[lowered_c] = 1

    lists = dict_to_list(dict)
    lists.sort(reverse=True, key=sort_on)

    return lists 

def dict_to_list(dict):
  list = []
  for d in dict:
    list.append({"char": d, "count": dict[d]})

  return list
   
def sort_on(dict):
  return dict["count"]

def print_output(output):
   for o in output:
      print(f"The '{o['char']}' character was found {o['count']} times")
main()