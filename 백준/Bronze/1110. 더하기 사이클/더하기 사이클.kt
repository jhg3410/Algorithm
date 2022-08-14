fun main() {
    var num = readln()
    if (num.length == 1) num = "0$num"
    var sum = ""
    var cnt = 0
    var a = num.first()
    var b = num.last()
    while (sum != num){
        sum = b.plus((a.digitToInt()+b.digitToInt()).toString().last().toString())
        cnt ++
        a = b
        b = sum.last()
    }

    println(cnt)
}