import os

# # Let us print the files in the directory in which you are running this script
# print (os.listdir("."))
#
# # Let us check if this file is indeed a file!
# print (os.path.isfile("./ex.py"))
#
# # Does the file end with .py?
# print ("./ex.py".endswith(".py"))


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    output = []
    try:
        file_list = os.listdir(path)
    except FileNotFoundError:
        return []
    for item in file_list:
        # First see if the item is a file, if it's a file then we don't have to go deeper inside to see if there's any subdir
        if os.path.isfile(os.path.join(path, item)):
            if item.endswith(suffix):
                output.append(os.path.join(path, item))
        else:  # It means the item is a directory instead of a file, we need to recursively get the files
            # Here extend is used to merge two lists
            output.extend(find_files(suffix, os.path.join(path, item)))
    return output

# Test functions

print("found files: \n", find_files('.c', 'testdir'))
# Expected result: ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']

print("found files: \n", find_files('.c', 'testdir2'))
# Expected result: ['testdir2/subdir1/subsubdir1/test.c', 'testdir2/subdir1/test.c']

print("found files: \n", find_files('.c', 'non_existent_dir'))
# Expected result []