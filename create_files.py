import os

# Create a directory 
def create_directory(directory):

    # If directory not available, then create a new dir
    if not os.path.exists(directory):
	print "Creating a directory...\n"
        os.makedirs(directory)
	print "Directory is created \n"

# Write data to text file 
def write_file(path,data):

    print "Writing the data into files...\n"
    f = open(path , 'w')
    f.write(data)
    f.close()


