dataTypes = {"integer": "All whole numbers",
             "string": "A set of alphanumeric characters",
             "char": "An alphanumeric character",
             "boolean": "True or false value",
             "list": "Ordered collection of data"}

del dataTypes["integer"]
print (dataTypes.get("integer","not found"))

#for key, value in dataTypes.items():
#    print (key)
#    print (value)