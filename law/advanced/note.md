# Note

语法：`# Notes #`

注意，注释在收缩文本中效果较差，即使是格式化后

注释前后必须都要有 `#` ，不可省略。这样你可以使用单行或多行注释with一个字符

Example:
```lcfg
# This is ...
... (多行注释中允许空行(任意白空格))


Have fun!
#

author = Cure-X # Declare the author's name #
copyright = CopyRight(c) @author
```

注意：sharp 的优先级低于 `""`，单个 sharp 低于 `$` 和 `\` 。
```lcfg
key_1=$#
key_2=\#
key_3="##"
```
上述示例中中的 val 分别为 `"#","#"` 和 `##` 。