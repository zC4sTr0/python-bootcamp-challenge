def titlecase(fname, lname):
    formatted_fname = fname.title()
    formatted_lname = lname.title()
    return f"{formatted_fname} {formatted_lname}"


print(titlecase("gabriel", "castro"))
