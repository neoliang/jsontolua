# jsontolua
a python script convert json to lua table

#usage:
git clone https://github.com/neoliang/jsontolua.git

cd jsontolua

python ./setup.py install

## Quick Expamples

#command line

python ./convert_json.py json_file lua_file

#code
```python

#convert string
jsontolua.str_to_lua_table('{"a":"1","b":2,"c":[1,2,3]}')
#return lua code 
'''
{
	a = '1',
	c = {
		1,2,3
	},
	b = 2
}

'''
#convert file
jsontolua.file_to_lua_file('./1.json','./1.lua')

```


