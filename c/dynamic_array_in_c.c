// HackerRank
// dynamic_array_in_c.c

#include <stdio.h>
#include <stdlib.h>

/*
Sample Input 0

5
5
1 0 15
1 0 20
1 2 78
2 2 0
3 0

Sample Output 0

78
2

*/

/*
 * This stores the total number of books in each shelf.
 */
int* total_number_of_books;

/*
 * This stores the total number of pages in each book of each shelf.
 * The rows represent the shelves and the columns represent the books.
 */
int** total_number_of_pages;

int main()
{
    int total_number_of_shelves;
    scanf("%d", &total_number_of_shelves);
    
    int total_number_of_queries;
    scanf("%d", &total_number_of_queries);
    
    while (total_number_of_queries--) {
        int type_of_query;
        scanf("%d", &type_of_query);
        
        if (type_of_query == 1) {
            int x, y;
            scanf("%d %d", &x, &y);

            // Allocate memory for total_number_of_books if not already done
            if (total_number_of_books == NULL) {
                total_number_of_books = (int*)calloc(total_number_of_shelves, sizeof(int));
            }

            // Allocate memory for total_number_of_pages if not already done
            if (total_number_of_pages == NULL) {
                total_number_of_pages = (int**)calloc(total_number_of_shelves, sizeof(int*));
            }

            // Ensure the shelf is initialized
            if (*(total_number_of_pages + x) == NULL) {
                *(total_number_of_pages + x) = NULL; // Set to NULL for safety
            }

            // Current number of books on shelf x
            int booksInShelf = *(total_number_of_books + x);

            // Allocate or reallocate memory to add a new book
            *(total_number_of_pages + x) = (int*)realloc(*(total_number_of_pages + x), sizeof(int) * (booksInShelf + 1));

            // Add the new book's page count
            *(*(total_number_of_pages + x) + booksInShelf) = y;

            // Increment the book count for shelf x
            *(total_number_of_books + x) += 1;

        } else if (type_of_query == 2) {
            int x, y;
            scanf("%d %d", &x, &y);
            printf("%d\n", *(*(total_number_of_pages + x) + y));
        } else {
            int x;
            scanf("%d", &x);
            printf("%d\n", *(total_number_of_books + x));
        }
    }

    if (total_number_of_books) {
        free(total_number_of_books);
    }
    
    for (int i = 0; i < total_number_of_shelves; i++) {
        if (*(total_number_of_pages + i)) {
            free(*(total_number_of_pages + i));
        }
    }
    
    if (total_number_of_pages) {
        free(total_number_of_pages);
    }
    
    return 0;
}
