

class Vector[T](private var capacity: Int = 32) {
  private var data: Array[Option[T]] = Array.fill(capacity)(None)
  private var size = 0
  println("Vector initialized")

}

object Vector extends App  {
  def test() {
    val vector = new Vector()

  }

  test()
}