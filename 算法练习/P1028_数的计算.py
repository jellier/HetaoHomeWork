# 先输入一个正整数 n(n≤1000),然后对此正整数按照如下方法进行处理：
# 不作任何处理；
# 在它的左边加上一个正整数,但该正整数不能超过原数的一半；
# 加上数后,继续按此规则进行处理,直到不能再加正整数为止。
# 输出满足该性质数的个数
# 如输入：6，满足条件的为6，16，26，126，36，136；输出：6

# 思路分析
# 1、假设已知 f(499)的答案，求f (500)的答案。 很显然，将 n=499 的所有解中的 499 由 500 替代之后，可以得出绝大多数 n=500 的解，
# 下面分析缺少的部分。由于 n=499 第一次添加的数从 1 到 249，而 n=500 第一次添加的数从 1 到 250，因此缺少的部分是 f(250)
#
# 2、假设已知 f(500)的答案，求 f(501)的答案。将 n=500 的所有解中的 500 由 501 替代之后，可以得出绝大多数 n=501 的解，
# 下面分析缺少的部分。由于 n=500 第一次添加的数从 1 到 250，而 n=501 第一次添加的数也是从 1 到 250，因此不缺少。
#
# 3、递推公式：偶数 f(2n) = f(2n-1) + f(n) , 奇数 f(2n+1) = f(2n)


n = int(input())
l = [1]*1001

def f(n):
    if n == 1:
        l[1] = 1
    else:
        for i in range(2, n+1):
            l[i] = l[i - 1]
            if i % 2 == 0:
                l[i] += l[i//2]

    return l[n]
print(f(n))


