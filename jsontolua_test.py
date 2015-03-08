import jsontolua
import os
import os.path

print jsontolua.str_to_lua_table('{"a":"1","b":2,"c":[1,2,3]}')
print jsontolua.str_to_lua_table('[]')
print jsontolua.str_to_lua_table('[1,2,3]')
jsontolua.file_to_lua_file('./1.json','./1.lua')