import re


def remove_non_executable_code(code_string):
    """
    Removes single-line comments and multi-line strings (docstrings) from a
    string of Python code.

    Args:
        code_string (str): The string containing Python code.

    Returns:
        str: The code with non-executable parts removed.

    NOTE: This approach uses regular expressions and may not be fully
    robust for all edge cases, such as comments inside a string literal.
    For a more advanced and reliable solution, consider using Python's `ast`
    (Abstract Syntax Tree) module.
    """
    # First, remove multi-line strings (docstrings)
    # This regex looks for triple single quotes or triple double quotes
    # and everything in between, including newlines (re.DOTALL flag).
    # The `?` makes the match non-greedy, so it stops at the first closing quote.
    docstring_pattern = r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''
    code_without_docstrings = re.sub(docstring_pattern, '', code_string, flags=re.DOTALL)

    # Next, remove single-line comments
    # This regex handles comments at the start of a line or inline comments.
    # It looks for a '#' and everything that follows until a newline.
    comment_pattern = re.compile(r'#.*$')
    lines = code_without_docstrings.splitlines()
    clean_lines = [re.sub(comment_pattern, '', line).rstrip() for line in lines]

    # Re-join the lines and remove any blank lines that resulted from
    # removing the comments or docstrings.
    clean_code = '\n'.join(line for line in clean_lines if line)

    return clean_code


# --- Example Usage ---

if __name__ == "__main__":
    example_code = """
import os  # Import the os module

# This is a full-line comment
def my_function(x):
    '''
    This is a docstring for the function.
    It explains what the function does.
    '''
    # Another comment inside the function
    result = x * 2  # Inline comment
    return result

"""

    print("--- Original Code ---")
    print(example_code)

    cleaned_code = remove_non_executable_code(example_code)

    print("\n--- Cleaned Code ---")
    print(cleaned_code)