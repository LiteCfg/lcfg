# String

一切非数字的元素都是字符串。(not inf nan)  
如果你认为一个元素为 String ，请使用 `$` 字符串标识符在字符串开头（由于美元符号比较像S），但如果使用在不必要的地方，`$` 会被认作字符串的一部分。

Example:  
`key=val // val is String`  
`key=123 // val is Number`  
`key=$123 // val is String`  
`key=$val // val = "$val"`

key总是字符串，所以即使$123也是 "$123"
如果key中使用了`"`，`;`，`=`，`:`,{},[]等字符？



如果你使用了`;`等字符？
转义？
暂定：`\` 转义单个字符？或者用$开头？（更优先，因为只花费了1字节）
`""`中转义一切字符(不能使用`''`)，`"` 本身用 `\'` 转义。


如果想要在字符串开头结尾中间加入空格（不支持space以为的白空格？），
请在编辑中使用 `""` 。

像这样
```lcfg
" key 1 " = " String with many spaces     "
```
...

但是我 **非常不推荐** 你这样做，因为这样不仅增加了存储空间，更大大增加了人调用它们的难度--精准敲出正确的空格数量并非一件简单的事

在压缩格式的解析中，不需要用引号保留。因为出色的压缩语法把空格的作用发挥到了极致

例如上述压缩后...

不过里面有东西需要""转义除外

