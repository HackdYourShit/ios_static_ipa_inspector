# Inspect an iOS app
This set of Python scripts was designed to speed up basic static analysis of an iOS IPA.

#### Python and 3rd party APIs
```
radare2
os.path
OptionParser
```
#### Invoke the console output
```
c = Thing2("warcraft","world","hello")
YDConsole.single_list(c.yd_list)
```


#### Message in a bottle
````
In the first python scripts, it was obvious it was going to get messy., main called the Console log functions.  That proved messy.

To make to code simple to read and maintain, I tried to use Object-Orientated features.
 
Inheritance, overrides and Classes that encapsulated the ability to return strings and lists. 

To minimise sprinkings of print statements, that is all inside the console output.
```