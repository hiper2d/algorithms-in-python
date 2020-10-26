import java.nio.charset.Charset
import kotlin.random.Random
import kotlin.random.nextUBytes

@ExperimentalUnsignedTypes
private fun generateRandomKey(length: Int): Int {
    val randomBytes = Random.Default.nextUBytes(length)
    return convertBytesToInt(randomBytes)
}

@ExperimentalUnsignedTypes
private fun convertBytesToInt(randomBytes: UByteArray): Int {
    var shift = 0
    var resultInt = 0
    for (byte in randomBytes) {
        resultInt = resultInt or byte.toInt() shl shift
        shift += 8
    }
    return resultInt
}

private fun convertIntToBytes(a: Int) {
    val digit = a and 0xF
    println(digit)
    println(a shr 1)
}

@ExperimentalUnsignedTypes
private fun encrypt(original: String): EncryptionResult {
    val dummyKey = generateRandomKey(original.length)
    val originalKey = convertBytesToInt(original.toByteArray(Charset.defaultCharset()).toUByteArray())
    return EncryptionResult(dummyKey, originalKey xor dummyKey)
}

private fun decrypt(dummyKey: Int, encryptedKey: Int): String {
    return ""
}

fun main() {
    println(generateRandomKey(2))
    println(encrypt("AA"))
    convertIntToBytes(8)
}

private data class EncryptionResult(val randomKey: Int, val encryptedKey: Int)
