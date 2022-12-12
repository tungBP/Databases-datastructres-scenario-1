User_choice = int(input("Enter number of doors on truck 1 or 2:" ))

Destination_list = []
Item_list = []
Destination_dictionary = {}

Num_destination = int(input("Enter number of destination : "))

    
for i in range(0,Num_destination):
    des = str(input("Enter destination name:"))
    Destination_list.append(des)

Num_item = int(input("Enter number of elements : "))
for x in Destination_list:
    Destination_dictionary[str(x)]=[]
    
for i in range(0, Num_item):
    Item_des=str(input("Enter item destination :"))
    Item_name=input("Enter the item name:")
    Item_list.append([Item_des,Item_name])
    for k in Destination_list:
        if Item_des==k:
            Destination_dictionary[k].append(Item_name)

if User_choice == 1:
    print (Destination_dictionary)
if User_choice == 2:
    Door1 = dict(list(Destination_dictionary.items())[len(Destination_dictionary)//2:])
    Door2 = dict(list(Destination_dictionary.items())[:len(Destination_dictionary)//2])
    print(Door1)
    print(Door2)

  
            
    
