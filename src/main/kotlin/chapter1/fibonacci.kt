package chapter1

private fun simpleFibonacci(a: Int): Long = if (a <= 1) 1 else simpleFibonacci(a - 1) + simpleFibonacci(a - 2)

private val memo = mutableMapOf(0 to 1L, 1 to 1L)
private fun memoFibonacci(a: Int): Long {
    if (!memo.containsKey(a)) {
        memo[a] = memoFibonacci(a - 1) + memoFibonacci(a - 2)
    }
    return memo[a]!!
}

private fun iterativeFibonacci(a: Int): Long {
    if (a == 0 || a == 1) return 1
    var prev = 0L
    var curr = 1L
    repeat(a) {
        curr += prev
        prev = curr - prev
    }
    return curr
}

private fun fibonacciGenerator() = sequence {
    var prev = 0L
    var curr = 1L
    while (true) {
        prev = curr - prev
        curr += prev
        yield(prev)
    }
}

fun main() {
    println("Fibonacci (2): ${simpleFibonacci(2)}")
    println("Fibonacci with Memo (50): ${memoFibonacci(50)}")
    println("Fibonacci iterative (50): ${iterativeFibonacci(50)}")
    println("Fibonacci generator (5): ${fibonacciGenerator().take(5).toList()}")
}
