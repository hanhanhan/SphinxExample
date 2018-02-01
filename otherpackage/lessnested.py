"""
Less nested example functions
"""

def less_nested_example_undocumented():
    return


def less_nested_example_vanilla():
    """
    I'm an example vanilla docstring.
    """
    return


def less_nested_example_googlestyle(a):
    """
    I'm an example numpy/google guide style docstring.
    
    Args:
        a (int): Description of arg1

    Returns:
        bool: Description of return value
    """
    return a


def less_nested_example_rst():
    """
    This is a docstring

    :param path: The path of the file to wrap
    :type path: str
    :param field_storage: The :class:`FileStorage` instance to wrap
    :type field_storage: FileStorage
    :param temporary: Whether or not to delete the file when the File
    :type temporary: bool
    :returns: A buffered writable file descriptor
    :rtype: BufferedFileStorage
    """

    return