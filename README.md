# lldb-scripts

Collection of Python script for lldb, simplifying debugging.

## QString printer

Prints readable QStrings for Qt 5.x inspired by http://codelite.org/LiteEditor/DebugWithLLD

### How to use

* Copy qstring.py into ~/.lldb/

* Invoke following command in lldb:

```
command script import ~/.lldb/qstring.py
```

* Enjoy readable QStrings in lldb or Xcode


![Xcode and QString](https://github.com/tgebarowski/lldb-scripts/blob/master/docs/lldb-qstring-xcode.png "Xcode and QString")