from test_framework import generic_test

"""
Write a program which takes a pathname, and returns the shortest directory paths.
Logic: Ignore /., and handle /.. by popping the stack, if string starts with / then you 
can go up, record it in a stack. Insert everything else in the stack
We may encounter a .. when stack is empty, this shows a path begining with an ancestor name
 we will then need to record that ..
Final result is the state of the stack after loop finishes
"""
def shortest_equivalent_path(path: str) -> str:

    if not path:
        raise ValueError('Empty string is not a valid path.')

    path_names = []  # Uses list as a stack.
    # Special case: starts with '/', which is an absolute path.
    if path[0] == '/':
        path_names.append('/')

    for token in [token for token in path.split('/')
                  if token not in ['.', '']]: # clever way of ignoring token which are blank or just .
        if token == '..':
            #if path list is empty or last element in path is .. then store ..
            if not path_names or path_names[-1] == '..': # example: ../../local
                path_names.append(token)
            else: #if path list not empty then pop the last element
                if path_names[-1] == '/':#edge cases
                    raise ValueError('Path error')
                path_names.pop()
        else:  # Must be a name.
            path_names.append(token)

    result = '/'.join(path_names)#return overall shortest path
    return result[result.startswith('//'):]  # Avoid starting '//'. #another edge cases, double slash, because first
    # slash will be join by slash. Or remove the unwanted slash from line 34, example "/foo/../foo/./../"

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('8-04-directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
