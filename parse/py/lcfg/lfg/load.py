class load():
    def __init__(self):
        pass

    def element():
        def classify(arg):
            from re import * #局部？
            # key:val
            # 压缩后的
            # \\n?
            # 进制 -> 颜色？
            #arg[0]==('"' or ):#or
            
            if match('[+,-]*\d+$',arg): return int(arg)
            elif match('[+,-]*\d*\.\d*',arg):
                if arg=='.': return 0.
                return float(arg)
            # 运算式
            elif arg[0]=='~': return True
            elif arg[0]=='!': return False
            # 但是 !a:1 ,a!1,? a!=1等除外
            elif arg=='': return None
            elif arg=='>>': return float('inf')
            elif arg=='<<': return float('-inf')
            elif arg=='<>' or arg=='><': return float('nan')
            return esc(arg)

        def esc(arg):
            #if arg[0]=='@':pass
            if arg[0]=='"':
                if arg[-1]!='"':
                    raise Exception #!
                return arg[1,-1]#其中有\转义？
            if 
