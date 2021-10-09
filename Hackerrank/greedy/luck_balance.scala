import java.io._
import java.math._
import java.security._
import java.text._
import java.util._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._
import scala.collection.immutable._
import scala.collection.mutable._
import scala.collection.concurrent._
import scala.concurrent._
import scala.io._
import scala.math._
import scala.sys._
import scala.util.matching._
import scala.reflect._

object Result {

    /*
     * Complete the 'luckBalance' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER k
     *  2. 2D_INTEGER_ARRAY contests
     */

    def luckBalance(k: Int, contests: Array[Array[Int]]): Int = {
    // Write your code here
      val sorted = contests.sortBy(subArr => -subArr(0))
      var remainingSkips = k
      var luck = 0
      for (i <- sorted.indices) {
        if (sorted(i)(1) == 1) {
          if (remainingSkips > 0) {
            remainingSkips -= 1
            luck += sorted(i)(0)
          } else {
            luck -= sorted(i)(0)
          }
        } else {
          luck += sorted(i)(0)
        }
      }
      luck
    }
}

object Solution {
    def main(args: Array[String]) {
        val printWriter = new PrintWriter(sys.env("OUTPUT_PATH"))

        val firstMultipleInput = StdIn.readLine.replaceAll("\\s+$", "").split(" ")

        val n = firstMultipleInput(0).toInt

        val k = firstMultipleInput(1).toInt

        val contests = Array.ofDim[Int](n, 2)

        for (i <- 0 until n) {
            contests(i) = StdIn.readLine.replaceAll("\\s+$", "").split(" ").map(_.trim.toInt)
        }

        val result = Result.luckBalance(k, contests)

        printWriter.println(result)

        printWriter.close()
    }
}
