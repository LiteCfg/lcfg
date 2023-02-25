# null

你可以这样表达 null

    key=

这并不是没写完的代码。此处的 val 会被解析为 null 。

等价与（易读的lcfg?）这条语句

    key = null

如果在结构体中使用：

    a,,b, // 这是一个数组

等价于JSON
```json
["a",null,"b",null]
```

特别的
a===
a==
a=
a==========...
a==b

a=1>null? node -> true
a=1>

空不会解析成null 的：
a=<>
a=><
a=>>
a=<<

a:(null)
,(null),