# 笔记
## 数据类型
### 基本数据类型 (Primitive types)

1. byte
   
    `Byte.SIZE = 8`, `Byte.MIN_VALUE = -2 ^ 7 = -128`, `Byte.MAX_VALUE = 2 ^ 7 - 1 = 127` 

2. short
   
    `Short.SIZE = 16`, `Short.MIN_VALUE = -2 ^ 15 = -32768`, `Short.MAX_VALUE = 2 ^ 15 - 1 = 32767`

3. int 
   
    `Int.SIZE = 32`, `Int.MIN_VALUE = -2 ^ 31 = -2147483648`, `Int.MAX_VALUE = 2 ^ 31 - 1 = 2147483647`

4. long
   
    `Long.SIZE = 64`, `Long.MIN_VALUE = -2 ^ 63 = -9223372036854775808`, `Long.MAX_VALUE = 2 ^ 63 - 1 = 9223372036854775807`

5. float
    
    单精度，32位

6. double
    
    双精度，64位， 浮点数的默认类型

7. boolean
    
    `true` or `false`, 默认值为`false`

8. char
    
    单一的16位Unicode字符

### 引用数据类型 (Reference types)

引用数据类型指向一个对象，指向对象的变量就是**引用变量**，该变量存储了对象在内存中的**地址**。引用变量在被声明时被指定为一个特殊的数据类型，如某一个特定的类。