# squish-object-map-reducer

**CURRENTLY UNDER DEVELOPMENT**

Small app helping to remove duplicated and not used entries from [object map](https://doc.froglogic.com/squish/latest/rg-objectmap.html)
of GUI Test Automation Tool called [Squish](https://www.froglogic.com/)

# Ultimate question of life, the universe and everything
After some time spent with this nice GUI automation tool I realized I miss something which would clean the last dirty 
(hahaha) part of the code - the object map. Squish does not provide this feature out of the box and also cleaning the map 
manually is laborious and boring.  

## The input
python squish-map-reducer.py -o object.map -t c:/workspace/test_suites/foo

## The output
object.map.reduced in current working directory

### The object.map structure
- Consists of several entries
- Each valid entry is in format:
  -  :NAME {ATTR1='VALUE' ATTR2='VALUE' ...}
- The number of attributes is not limited
- The 'NAME':
  - Can contain spaces, dots, underscores ... basically anything
- The 'ATTR':
  - One lower-case word (from a set), only letters allowed
- The '=':
  - Can be one of: '=', '?=', '~='
- The 'VALUE'
  - Can contain spaces, dots, underscores ... basically anything