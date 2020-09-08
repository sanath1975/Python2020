
# Dictionary -- Sequence of key:value pairs seperated with comma(,) delcared inside { }...
    # Ex: a= {'username':'sanjeeva','password':'sanjeeva','mobile':6472777828}

a= {'username':'sanjeeva','password':['sanjeeva','sanjeeva123'],('mobile',):6472777828,1:45}

# print(a)
# print(type(a))

# In dictionay all the keys should be immutable only....(string,number,tuple)
# In Dictionary values can be of any datatype.....


# ****** Dictionary are unique..*******
# When ever there is the duplicate keys is declared it will by default takes the last key:value pair into consideration...

# a={'username':'sanjeeva','password':['sanjay',"reddy123"],'username':'ramesh123'}

# print(a)

# Dictionaries will not have any indexing for accessing the elements as dictionary is not only the values it combination of key:values.......

# Dictionaries Accsessing is done based on key-name....

# [] -- is the symbol for accessing the values inside the dictionary...

a= {'username':'sanjeeva','password':['sanjeeva','sanjeeva123'],('mobile',):6472777828,1:45}

# print(a['password'])

# print(a['username'])

# print(a[1])
# print(a[('mobile',)])

# print(a['email'])

# print(a)
# Dictionaries are also mutubale datatypes...

# a['email'] = 'gsanjeev@gmail.com' # This is for adding a single key:value pair at a time...

# a['address'] = "hyderabad"
# print(a)

# del a[1]

# print(a)

# a['password'] = 'sanjay123'

# print(a)

# a['address'] = "chennai"
# print(a)

# If the key is already existed in the dictonary it will update the key with new values.. 
# If the key is not existed it will be add it as a new key:value pair into the dictionary..

# nested dictionaries

a = {
    "India":{"Telangana":"Hyderabad","Andhrapradesh":{"captial1":"Amaravathi","captial2":"Kurnool"},"Tamilnadu":"Chennai"},
    "USA":{'Newyork':"Newyork123","California":"California123"}

}

# # print(a)

# print(a['India'])

# print(a['USA'])

# print(a['India']['Andhrapradesh']['captial2'])
# print(a['USA']['Newyork'])


# Dictionary Methods:-

# print(dir(dict))

# get,update,,pop,popitem,clear,copy,keys,values,items,fromkeys,setdefault


# get -- It for getting the values associated with the key...

print(a['India'])

print(a.get('India'))


# print(a['Africa'])

# print(a.get('Africa'))

# if a['Africa']:
#     print("Key present")
# else:
#     print("Key Not present")


# if a.get('Africa'):
#     print("Key present")
# else:
#     print("Key Not present")
# print("Hello")
# print(2+4)