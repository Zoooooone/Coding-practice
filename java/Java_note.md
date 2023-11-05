# Java学习笔记

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

### 常量
- 常量在程序运行时不能被修改
- 使用`final`关键字来修饰常量，声明方式如下：
    ```java
    final double PI = 3.1415926
    ```
- 通常使用**大写字母**表示常量

### 自动类型转换
整型、实型（常量）、字符型数据可以混合运算。不同的数据类型会转化为同一数据类型，转化优先级如下：
```java
byte, short, char -> int -> long -> float -> double
```
规则：
- 不能对`boolean`类型进行类型转换
- 容量大的类型转换为容量小的类型时必须使用[**强制类型转换**](#强制类型转换)
- 转换过程中可能导致溢出或损失精度
- 浮点数转换到整数时会**舍弃小数部分**，而不是四舍五入
- 字符转换为整数类型时的值为对应的**ASCII编号**

### 强制类型转换
规则：
- 转换的数据类型必须相互兼容
- 转换格式：`(type) value`

细节：
- 整数的默认类型是`int`
- 小数的默认类型是`double`，在定义`float`类型时须在数字后跟上`F`或`f`


## 变量类型
Java语言支持四种变量类型，分别为：**局部变量(Local Variables)**、**成员变量(Instance Variables)**、**静态变量(Class Variables)**、**参数变量(Parameters)**。

### 局部变量
- 作用范围：只在定义它们的代码块内部可见
- 生命周期：超出代码块该变量就会被销毁
- 作用: 用于存储代码块中临时的变量
- 例子：
    ```java
    public class variables {
        public static void cal_sum(){
            int x = 10;
            int y = 15;
            System.out.println("sum: " + (x + y));
        }

        public static void main(String[] args){
            for (int i = 0; i < 5; i++){
                System.out.print(i + " ");
            }
            // System.out.println(i);  i will not be stored after for loop
            // System.out.println(x);  x will not be stored out of the cal_sum block
            System.out.print("\n");
            cal_sum();
        }
    }
    ```
    1. 位于for循环中的循环变量`i`在离开循环代码块后就不再被保存，也无法被访问
    2. 位于静态方法`cal_sum`中的局部变量`x`在离开该方法的代码块后也无法被访问

### 成员变量
- 作用范围：类的**对象中**
- 生命周期：与类的**对象**的生命周期相同
- 作用：用于存储类的对象的特定状态与数据
- 例子：
    ```java
    public class variables {
        String instance_num = "instance variable";

        public static void main(String[] args){
            /* instance variable */
            // System.out.println(instance_num); instance_num can not be accessed without a object
            variables obj = new variables();
            System.out.println(obj.instance_num); 
        }
    }
    ```
    成员变量在对象实例被创造之前无法被访问，其完全依赖于对象的状态

### 静态变量
- 作用范围：类中
- 生命周期：与类的生命周期相同
- 作用：用于存储与整个类相关的信息，如常量或共享的状态
- 例子：
    ```java
    public class variables {
        static final double PI = 3.14;

        public static void main(String[] args){
            /* class variable */
            System.out.println(PI);
        }
    }
    ```
    其可以在类的静态方法中直接被访问

### 参数变量
- 作用范围：参数变量是方法的输入值，只在方法内部生效
- 生命周期：方法被执行期间
- 作用: 向方法传递数据
- 例子：
    ```java
    public class variables {
        public static void cal_sum_2(int p, int q){
            System.out.println("p + q = " + (p + q));
        }

        public static void main(String[] args){
            /* parameters */
            cal_sum_2(1, 2);
            // System.out.println(p); p can not be accessed out of the method
        }
    }
    ```
    对于方法`cal_sum_2`，`p`和`q`都是参数变量，只在执行这个方法期间存在，无法从外部被访问


## 修饰符
Java语言的修饰符分为两类：
- 访问修饰符
- 非访问修饰符

### 访问修饰符
用来保护对类、变量、方法和构造方法的访问。支持四种权限：
- **default**：什么也不写。
  - 可见范围：同一包内
  
- **private**
  - 可见范围：同一类内

- **public**
  - 可见范围：所有类

- **protected**
  - 可见范围：同一包内的类和所有子类

### 非访问修饰符
- **static**
  - 静态变量：**独立于类的对象的变量**。无论一个类实例化多少对象，静态变量都只有一份拷贝
  - 静态方法：**独立于对象的方法**，不能使用类的非静态变量

- **final**
  - final变量：一旦被赋值后就**不能被重新赋值**。通常用来和static一起用来创建类常量
  - final方法：父类中的final方法可以被子类继承，但**不能被子类重写**
  - final类：final类**不能被继承**


## 运算符
Java中的运算符主要可以分为以下几种：
- 算术运算符
- 关系运算符
- 位运算符
- 逻辑运算符
- 赋值运算符
- 其他运算符

### 算术运算符
|| 描述 |
|---|---|
| `+` | 加 |
| `-` | 减 |
| `*` | 乘 |
| `/` | 除 |
| `++` | 自增 |
| `--` | 自减 |

**注意**：自增和自减符号的顺序会影响结果。
- 前缀自增自减法（`++a`, `--a`）：
- 后缀自增自减法（`a++`, `a--`）

**区别**：前者先进行自增减运算，再进行表达式计算；后者先进行表达式计算，再进行自增减运算。示例：
```java
public class increment_decrement {
    public static void main(String[] args){
        int x = 20;
        System.out.println(++x);  // ++ first, then print x, 21
        System.out.println(x++);  // print x first, then ++, 21
        System.out.println(x);  // 22
    }
}
```

### 关系运算符
|| 描述 |
|---|---|
| `==` | 判断是否相等 |
| `!=` | 判断是否不等 |
| `>` | 判断是否左大于右 |
| `<` | 判断是否左小于右 |
| `>=` | 判断是否左大于等于右 |
| `<=` | 判断是否左小于等于右 |

### 位运算符
|| 描述 |
|---|---|
| `&` | 按位与 |
| `\|` | 按位或 |
| `^` | 按位异或 |
| `~` | 按位取反（一元运算符） |
| `<<` | 左移 |
| `>>` | 右移 |
| `>>>` | 右移，空位补零 |

### 逻辑运算符
|| 描述 |
|---|---|
| `&&` | and |
| `\|\|` | or |
| `!` | not |

### 赋值运算符
与python基本一致，略

### 条件运算符
三元运算符，主要**决定哪个值应该赋值给变量**
```java
variable x = expression ? value1 : value2
// variable x = value1 if expression == True else value2
```


## 循环结构
### while
与python一致，例：
```java
public class loops {
    public static void main(String[] args){
        /* while loop */
        System.out.println("while loop:");
        int x = 5;
        while (x < 7){
            System.out.print(x + " ");
            x++;
        }
    }
}
```
输出：
```
while loop:
5 6 
```

### do ... while
**与while的区别**：最开始的时候若`while`后的布尔表达式结果为`false`，仍会执行一次`do`代码块中的内容。其余时候与普通的`while`没有区别。例：
```java
public class loops {
    public static void main(String[] args){
        /* do while loop */
        System.out.println("\ndo while loop:");
        int x = 10;
        do{
            System.out.print(x + " ");
            x++;
        } while (x < 7);
    }
}
```
输出:
```
do while loop:
10 
```

### for
与python一致，例：
```java
public class loops {
    public static void main(String[] args){
        /* for loop */
        System.out.println("\nfor loop:");
        int x = 5;
        for(; x < 7; x++){
            System.out.print(x + " ");
        }
    }
}
```
输出:
```
for loop:
5 6 
```

### for each（作用于数组）
Java5新特性，主要用于数组的循环。循环变量的类型与数组元素的类型匹配。例:
```java
public class loops {
    public static void main(String[] args){
        /* for each */
        System.out.println("\nfor each loop:");
        int [] nums = {1, 2, 3, 4 ,5};
        for (int num: nums){
            System.out.print(num + " ");
        }
        System.out.println();
        char [] alphabet = {'a', 'b', 'c'};
        for (char s: alphabet){
            System.out.print(s + " ");
        }
    }
}
```
输出
```
for each loop:
1 2 3 4 5 
a b c 
```