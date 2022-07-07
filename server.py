# Importing Flask to be our HTTP server
from flask import Flask

# Importing this view so Flask can delegate to Graphene
from flask_graphql import GraphQLView
from schemas import schema

app=Flask(__name__)

# Adding a single route for /graphql
app.add_url_rule("/graphql", view_func=GraphQLView.as_view( "graphql", schema=schema, graphiql=True),)
