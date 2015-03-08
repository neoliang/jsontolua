# jsontolua
a python script convert json to lua table

usage:

#convert string

print jsontolua.str_to_lua_table('{"a":"1","b":2,"c":[1,2,3]}')

'''
lua code:

{
	a = '1',
	c = {
		1,2,3
	},
	b = 2
}

'''

print jsontolua.str_to_lua_table('[]')
'''
lua code 

{
	
}
'''

print jsontolua.str_to_lua_table('[1,2,3]')

'''
lua code

{
	1,2,3
}

'''

#convert file

jsontolua.file_to_lua_file('./1.json','./1.lua')


