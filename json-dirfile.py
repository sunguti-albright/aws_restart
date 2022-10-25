import json

data_sample = '''
{
    "users":
    
    [
    { "name": "Albright",
      "age" : 24,
      "phone" : 0799745661,
      "student" : False,
    },
    { "name": "Ruth",
      "age" : 44,
      "phone" : 0799745661,
      "student" : False,
    },
    { "name": "Linda",
      "age" : 44,
      "phone" : 0799745661,
      "student" : True,
    },
    { "name": "Zuri",
      "age" : 50,
      "phone" : 0799745661,
      "student" : False,
    }
    ]

'''
data = json.loads(data_sample)
print(data)
