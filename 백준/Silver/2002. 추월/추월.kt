package heejik.`17week`

/*
* 앞에 있는 차 중에 원래 앞에 있던 애들이 아니고 이미 추월한 애가 아닌
애의 숫자들의 합
*
* 나왔더니 원래 앞에 있던 차들 중 하나라도 없으면 난 추월했어~
*
*/
class 추월 {

    fun solve() {

        val n = readln().toInt()
        val carsWithFrontCars = mutableMapOf<String, List<String>>()
        val inFrontCars = mutableListOf<String>()
        val outFrontCars = mutableListOf<String>()
        var cnt = 0

        repeat(n) {
            val inCar = readln()
            carsWithFrontCars[inCar] = inFrontCars.toMutableList()
            inFrontCars.add(inCar)
        }

        repeat(n) {
            val outCar = readln()
            carsWithFrontCars[outCar]!!.forEach {
                if (outFrontCars.contains(it).not()) {
                    cnt++
                    outFrontCars.add(outCar)
                    return@repeat
                }
            }
            outFrontCars.add(outCar)
        }

        println(cnt)
    }
}

fun main() {
    추월().solve()
}
