# Importing Graphene so we can define a simple GraphQL schema
import graphene

class Query(graphene.ObjectType):
    # defining a field "who" in the schema with the argument "name"`
    who = graphene.String(name=String(default_value="Ms Marvel"))

    # This returns the GraphQL context (root, info) and adds the argument
    def resolve_who(root, info, name):
        return f'Hi {name}!'

schema = graphene.Schema(query=Query)
