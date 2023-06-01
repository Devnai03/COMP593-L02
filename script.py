"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        
        # TODO: Put full name into data structure
        'full_name' : 'Devendra Nai',
        
         # TODO: Put student ID into data structure
        'student_id' : '10291266',
        
         # TODO: Put list of 3 pizza toppings into data structure
        'pizza_toppings' : [
            'PEPERONI',
            'JALAPENO',
            'RED CHILLI'
        ],
        
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'Hera Pheri',
                'genre': 'Comedy',
            },
            # TODO: Add one more movie
            {
                'title': 'Spider-man: No way home',
                'genre': 'Fantasy'
            }
            
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['olives', 'spinach'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'the nun', 'horror')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(about_me):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    full_name = about_me['full_name']
    first_name = about_me['full_name'].split(' ')[0]
    student_id = about_me['student_id']
    
    # Print sentence containing name
    print(f'My name is {full_name}, but you can call me Mr. {first_name}.')
    
    # Print sentence containing student ID
    print(f'My student ID is {student_id}.')

def print_pizza_toppings(about_me):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    print(f'My favourite pizza toppings are:')
    
    # Print bullet list of favourite pizza toppings
    for pt in about_me['pizza_toppings']:
            print(f'- {pt} ')
            
    return

def add_pizza_toppings(about_me, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    about_me['pizza_toppings'].extend(toppings)
    
    # Convert all pizza toppings to lowercase
    for ptl, nt in enumerate(about_me['pizza_toppings']):
        about_me['pizza_toppings'][ptl] = nt.lower()
        
    # Sort toppings list alphabetically
    about_me['pizza_toppings'].sort()
    
    return

def add_movie(about_me, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    add_movie = {
        'title' : 'Jab we met',
        'genre' : 'Romantic'
    }
    
    about_me['movies'].append(add_movie)
    return

def print_movie_genres(about_me):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    print("I like to watch ", end="")
    movie_list = [g['genre'] for g in about_me['movies']]
    print(", ".join(movie_list), end=".\n")
    return

def print_movie_titles(about_me):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    print("Some of my favourite movies are  ", end="")
    movie_title = [t['title'] for t in about_me['movies']]
    print(", ".join(movie_title), end="!\n")
    return

if __name__ == '__main__':
    main()