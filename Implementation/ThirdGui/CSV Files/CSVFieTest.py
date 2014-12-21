import csv

def ManagePostcode():
    address_list = []
    with open("CumbriaPostcodes.csv", "r")as postcode_file:
        postcodes = csv.reader(postcode_file)
        for item in postcodes:
            address_list.append(item)

        #Dispalying Postcodes Postcode List
        #for count in range(0, len(address_list)):
            #print(address_list[count][0])

            
        postcode_input = input("Enter Postcode Here:")
        print("")
        
        Present = False
        for count in range(0, len(address_list)):
            if postcode_input in address_list[count]:
                Present = True
                for item in address_list[count]:
                    print(item)
        print(Present)


def main():
    ManagePostcode()

if __name__ == '__main__':
    main()
    
    
        
