import pandas as pd

df = pd.read_csv('books.csv')

df['Price'] = df['Price'].str.replace('£', '').astype(float)

# How many books are there in total?
total_books = df.shape[0]
print(f"Total number of books: {total_books}")

# What is the average price of the books?
average_price = df['Price'].mean()
print(f"Average price of the books: £{average_price:.2f}")

# What are the 5 most expensive books and their prices?
most_expensive_books = df.nlargest(5, 'Price')
for _, book in most_expensive_books.iterrows():
    print(f"Top 5 most expensive book: {book['Title']} at £{book['Price']:.2f}")

# What are the 5 least expensive books and their prices?
least_expensive_books = df.nsmallest(5, 'Price')
for _, book in least_expensive_books.iterrows():
    print(f"Bottom 5 least expensive book: {book['Title']} at £{book['Price']:.2f}")

df.to_csv('cleaned_books.csv', index=False)    


with open('summary.txt', 'w', encoding='utf-8') as f:
    f.write(f"Total number of books: {total_books}\n")
    f.write(f"Average price of the books: £{average_price:.2f}\n")
    f.write("Top 5 most expensive books:\n")
    for _, book in most_expensive_books.iterrows():
        f.write(f"{book['Title']} at £{book['Price']:.2f}\n")
    f.write("Bottom 5 least expensive books:\n")
    for _, book in least_expensive_books.iterrows():
        f.write(f"{book['Title']} at £{book['Price']:.2f}\n")



