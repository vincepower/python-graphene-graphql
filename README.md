# python-graphene-graphql

Sample app for making a GraphQL API using Graphene in a Django server

## What is here

| Files | Purpose |
|---|---|
| LICENSE | Everything needs a license, this uses APL 2.0 |
| README.md | This file |
| .gitignore | What files git should ignore during operations |
| requirements.txt | All the defined packages which this uses (on Rocky 8.5) |
| server.py | Flask based server that accepts requests and routes |
| schema.py | The actual GraphQL code using Graphene  |
| schema.gql | Schema that the code generates and responds to |

# Using this


```
python3 -m venv python-graphene-graphql-ve
source python-graphene-graphql/bin/activate
python server.py
```

