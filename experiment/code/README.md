# code

## frame

- 主要的内容在文件 [simple.ipynb](simple.ipynb) 中。
- 一些细节放在 [func](func) 中, 构造一些函数被 [simple.ipynb](simple.ipynb) 调用

## conclusion

1. 调用函数的时候, 使用 temp_xxx 来整理一下参数, 可以方便自己思考需要满足哪些条件
   > 无需考虑这一点优化, 编译器会做的
2. 首先要清晰思路, 最后手动计算一边, 对整个流程有非常明确的认识
3. 约定好表达的符号, 符号混乱, 自己到时候明明有想法,却无法捋清楚, 容易自暴自弃
4. 大胆地模块化, 不断拆分, 结构清晰就好, 比例在类里面定义一个'main'
   > 当前层次展现清楚当前层次的思路
5. 划分好层次, 比如谁属于谁, pos 里面有需要的位置,角度, 加速度里面就是加速度,
   不要层次混乱
6. 简洁处理, 比如用复数表达坐标
