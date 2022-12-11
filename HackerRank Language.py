import re

lan = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC"

lang = lan.split(':')

N = int(input())
regex_pattern = r'^[1-9]{1}\d{4}'
for _ in range(N):
    S = input()
    if(re.search(regex_pattern,S)):
        x = re.search(r'\b[A-Z]+',S)
        if x.group() in lang:
            print("VALID")
        else:
            print("INVALID")
    else:
        print("INVALID")
