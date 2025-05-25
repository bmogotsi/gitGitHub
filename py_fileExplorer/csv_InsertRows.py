#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file.

# Import writer class from csv module
from csv import writer


try:
    # List that we want to add as a new row
    ListAll = []
    ListAll.append([6, 'William', 5532, 1, 'UAE'])
    ListAll.append([7, 'William', 5532, 1, 'ZAR'])
    ListAll.append([8, 'Bewn', 5532, 1, 'ZAR'])
    
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('event.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        for List in ListAll:
            writer_object.writerow(List)

        # Close the file object
        f_object.close()

    exit 
    
except Exception as e:
    print("Exception.....:    " + str(e))