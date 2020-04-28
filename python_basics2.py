def make_dir(dirname, clean=False):
    # Make a directory if it does not exist.
    # Use clean=True to clobber the existing directory.
    import os, shutil # separate modules with a comma
    if clean == True:
        # remove the directory and any sub-directories
        shutil.rmtree(dirname, ignore_errors=True)
        # then create the new empty directory
        os.mkdir(dirname)
    else:
        try:
            # try to create the directory if it does not exist
            os.mkdir(dirname)
        except OSError:
            pass # assume OSError was raised because directory already exists
