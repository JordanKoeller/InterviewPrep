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
import scala.collection.immutable

object Result {

    /*
     * Complete the 'reverseShuffleMerge' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    def reverseShuffleMerge(s: String): String = {
    // Write your code here
    val charReps = Array.fill(26)(0)
    s.foreach(c => charReps(c-'a') += 1)
    val extraChars = charReps.map(e => e / 2)
    val charsToConsume = charReps.map(e => e / 2)
    var consumingBucket = 0
    var ret = ""
    for (c <- s.reverseIterator) {
      val index = c - 'a'
      while (consumingBucket < 26 && charsToConsume(consumingBucket) == 0) {
        consumingBucket += 1
      }
      if (consumingBucket < 26) {
        if (index == consumingBucket) {
          ret = ret + c
          charsToConsume(index) -= 1
          println("Finished consuming" + c + " with count " + charsToConsume(index))
        } else {
          if (extraChars(index) > 0) {
            extraChars(index) -= 1
          } else {
            ret = ret + c
            charsToConsume(index) -= 1
          }
        }
      } else {
        return ret
      }
    }
    ret
  }

}

object Solution {
    def main(args: Array[String]) {
        val printWriter = new PrintWriter(sys.env("OUTPUT_PATH"))

        val s = StdIn.readLine

        val result = Result.reverseShuffleMerge(s)

        printWriter.println(result)

        printWriter.close()
    }
}
