# Boolean

只有 true 和 false 两种类型

true 用符号 `~` 表示，false 用符号 `!` 表示  
`~` `!` 只能写在键名前。

Example:  
`~key_1` -> `key_1 = true`  
`!key_2` -> `key_2 = false`

如果想要以 `~` 或 `!` 开头作为键名的一部分：

- 如果是 Boolean  
  `~!key` -> `"!key" = true`

- 如果不是 Boolean  
  `~key=val` -> `"~key" = val`  
  这样可以有效避免布尔类型与其他类型的冲突。

___

你也可以通过逻辑运算得到 Boolean

key== -> key = "="

key=== -> key = null == null -> key = true

更多？



分号键名转义

