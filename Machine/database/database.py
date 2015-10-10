import ast

# {objectname : {last_posX : int, last_postY : int, should_take : bool}}
#
#
# getObject(name)                                  Get an object based on name. (str -> dict)
# getListShouldTake()                              Get a dict of objects that should take (None -> dict)
# getObjectsInArea(min_x, max_x, min_y, max_y)     Get a dict of objects in range (int, int, int, int -> dict)
# getEntireDatabase()                              Get the entire database in all of its glory (None -> dict)
# storeObject(name, x, y, should_take)             Store an object into the database (str, int, int, bool -> None)
# generateNewDatabase()                            Generates a new database


def getObject(name):  # Get an object based on name. (str -> dict)
    name_lower = name.lower()
    database = populateVariable()
    
    if name_lower in database:
        return database[name_lower]
    else:
        return {"error": "error"}

def getListShouldTake(): # Get a dict of objects that should take (None -> dict)
    database = populateVariable()
    to_return = {}
    for item in database:
        if database[item]['should_take'] == True:
            to_return[item]=(database[item])
    return to_return

def getObjectsInArea(min_x, max_x, min_y, max_y): # Get a dict of objects in range (int, int, int, int -> dict)
    database = populateVariable()
    to_return = {}
    for item in database:
        if (database[item]['last_posX'] >= min_x) and (database[item]['last_posX'] <= max_x) and (database[item]['last_posY'] >= min_y) and (database[item]['last_posY'] <= max_y): 
            to_return[item]=(database[item])
    return to_return

def getEntirDatabase(): # Get the entire database in all of its glory (None -> dict)
    return (populateVariable())

def storeObject(name, x, y, should_take): # Store an object into the database (str, int, int, bool -> None)
    database = populateVariable()
    database[name.lower()] = {'last_posX': x, 'last_posY': y, 'should_take': should_take}
    writeChanges(database)

def generateNewDatabase(): # Generates a new database
    file_object = open('database.dat', 'w')
    file_object.write({})
    file_object.close()

def populateVariable(): # Populates the temp database required for operation.
    try:
        file_object = open('database.dat', 'r')
    except:
        print (["ERROR"])
    database = file_object.read()
    file_object.close()
    return ast.literal_eval(database)

def writeChanges(data): # Writes changes to database file
    file_object = open('database.dat', 'w')
    file_object.write(str(data))
    file_object.close()

print getObject("Tim")
