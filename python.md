## os.path

### abspath(path) 

返回绝对路径

```python
    >>> import os
    >>> os.path.abspath("translate.py")
    '/home/dl/PJT/translate.py'
    
    >>> os.path.abspath("./")          
    '/home/dl/PJT'
```

### split(path) 

将path分割成(目录,文件(夹)名)二元组

```python
    >>> os.path.split(os.path.abspath("translate.py"))
    ('/home/dl/PJT', 'translate.py')
```

如果path只是一个文件夹路径，没有精确到文件，则第二个元素返回最后一层文件夹的名字：

```python
    >>> os.path.split(os.path.abspath("./"))  
    ('/home/dl', 'PJT')
```

### dirname(path) 

返回os.path.split(path)的第一个元素

```python
    >>> os.path.dirname(os.path.abspath("translate.py"))
    '/home/dl/PJT'
    
    >>> os.path.dirname(os.path.abspath("./"))  
    '/home/dl'
```

### basename(path) 

返回os.path.split(path)的第二个元素。 

```python
    >>> os.path.basename(os.path.abspath("translate.py"))
    'translate.py'
    
    >>> os.path.basename(os.path.abspath("./"))  
    'PJT'
```

### commonprefix(list)

返回最长公共路径前缀

```python
    >>> cur = os.path.abspath("./")
    >>> mnist = os.path.abspath("mnist")
    >>> mnist
    '/home/dl/PJT/mnist'
    >>> cur
    '/home/dl/PJT'
    >>> os.path.commonprefix([cur,mnist])
    '/home/dl/PJT'
```

### exists(path) 

如果path(当前路径优先)存在，返回True；如果path不存在，返回False

```python
    >>> os.path.exists("test")
    False
    >>> os.path.exists("mnist")
    True
```

### isabs(path)

如果path为绝对路径，返回True；否则，返回False

```python
    >>> os.path.isabs("mnist")
    False
    >>> os.path.isabs(os.path.abspath("mnist"))
    True
```

### isfile(path) 

如果path(当前路径优先)是一个存在的文件，返回True。否则，返回False

```python
    >>> os.path.isfile("translate.py")
    True
    >>> os.path.isfile("mnist")
    False
```

### isdir(path)

如果path是一个存在的目录，则返回True。否则返回False

```python
    >>> os.path.isdir("translate.py")
    False
    >>> os.path.isdir("mnist")
    True    
```


### join(path, *paths)

将多个路径组合后返回，第一个绝对路径之前的参数将被忽略。 

```python
    >>> cur
    '/home/dl/PJT'
    >>> mnist
    '/home/dl/PJT/mnist'
    >>> os.path.join(mnist, cur, "translate.py")
    '/home/dl/PJT/translate.py'
```

### splitext(path) 

分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作

```python
    >>> os.path.splitext("translate.py")
    ('translate', '.py')
    >>> os.path.splitext(mnist)         
    ('/home/dl/PJT/mnist', '')
```

## tmpfile

### tempfile.TemporaryFile()

如何你的应用程序需要一个临时文件来存储数据，但不需要同其他程序共享，那么用TemporaryFile函数创建临时文件是最好的选择。其他的应用程序是无法找到或打开这个文件的，因为它并没有引用文件系统表。用这个函数创建的临时文件，关闭后会自动删除。

```python
    import os
    import tempfile
     
    print 'OriginalFile'
    filename = '/tmp/guess_my_name.%s.txt' % os.getpid()
    temp = open(filename, 'w+b')
    try:
        print 'temp:', temp
        print 'temp.name:', temp.name
    finally:
        temp.close()
        os.remove(filename)     # Clean up the temporary file yourself
     
    print
    print 'TemporaryFile:'
    temp = tempfile.TemporaryFile()
    try:
        print 'temp:', temp
        print 'temp.name:', temp.name
    finally:
        temp.close()    # Automatically cleans up the file
```

输出：
    
    OriginalFile:
    temp: <open file '/tmp/guess_my_name.4807.txt', mode 'w+b' at 0x7f0323cf35d0>
    temp.name: /tmp/guess_my_name.4807.txt
    
    TemporaryFile:
    temp: <open file '<fdopen>', mode 'w+b' at 0x7f0323cf3b70>
    temp.name: <fdopen>

这个例子说明了普通创建文件的方法与TemporaryFile()的不同之处，注意：用TemporaryFile()创建的文件没有文件名。

### tempfile.NamedTemporaryFile()

如果临时文件会被多个进程或主机使用，那么建立一个有名字的文件是最简单的方法。这就是NamedTemporaryFile要做的，可以使用name属性访问它的名字。

```python
    import os
    import tempfile
     
    temp = tempfile.NamedTemporaryFile()
    try:
        print 'temp:', temp
        print 'temp.name:', temp.name
    finally:
        # Automatically cleans up the file
        temp.close()
    print 'Exists after close:', os.path.exists(temp.name)
```

输出：

    temp: <open file '<fdopen>', mode 'w+b' at 0x7f109a4ed660>
    temp.name: /tmp/tmpM3clpn
    Exists after close: False
    
尽管文件带有名字，但它仍然会在close后自动删除。

**更精确地用3个参数生成文件名：**

path = dir + prefix + random + suffix

```python
    import tempfile
     
    temp = tempfile.NamedTemporaryFile(suffix='_suffix', 
                                       prefix='prefix_', 
                                       dir='/tmp',
                                       )
    try:
        print 'temp:', temp
        print 'temp.name:', temp.name
    finally:
        temp.close()
```

输出：

    temp: <open file '<fdopen>', mode 'w+b' at 0x7f9dca0f7b70>
    temp.name: /tmp/prefix_SCJKwE_suffix

### tempfile.mkdtemp()

创建临时目录，目录需要手动删除

```python
    import os
    import tempfile
     
    directory_name = tempfile.mkdtemp()
    print directory_name
    # Clean up the directory 
    os.removedirs(directory_name)
```

输出：

    /tmp/tmp9u8Zw4
    
### tempfile.mkstemp([suffix=''[, prefix='tmp'[, dir=None[, text=False]]]])
    
创建临时文件，调用tempfile.mkstemp函数后，返回包含两个元素的元组，第一个元素指示操作该临时文件的安全级别，第二个元素指示该临时文件的路径。参数suffix和prefix分别表示临时文件名称的后缀和前缀；dir指定了临时文件所在的目录，如果没有指定目录，将根据系统环境变量TMPDIR, TEMP或者TMP的设置来保存临时文件；参数text指定了是否以文本的形式来操作文件，默认为False，表示以二进制的形式来操作文件。

### tempfile.mktemp([suffix=''[, prefix='tmp'[, dir=None]]])

mktemp用于返回一个临时文件的路径，但并不创建该临时文件。

### tempfile.tempdir

该属性用于指定创建的临时文件（夹）所在的默认文件夹。如果没有设置该属性或者将其设为None，Python将返回以下环境变量TMPDIR, TEMP, TEMP指定的目录，如果没有定义这些环境变量，临时文件将被创建在当前工作目录。

### tempfile.gettempdir()

返回保存临时文件的文件夹路径。    
