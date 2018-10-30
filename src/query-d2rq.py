# -*- coding: UTF-8 -*-
'''
Created on 20181025
 
@author: Hansen
'''

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:2020/sparql")
sparql.setQuery("""
    PREFIX : <http://www.neohope.com/hansen/ontologies/2018/movies#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?title WHERE {
        ?aPerson rdf:type :Person.
        ?aPerson  :personName '巩俐'.
        ?aPerson  :hasActedIn ?aMovie.
        ?aMovie :movieTitle ?title.
        ?aMovie :movieRating ?rating.
        FILTER (?rating>=7)
    }
    LIMIT 10
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["title"]["value"])

