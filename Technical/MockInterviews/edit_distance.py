"""
Edit distance string comparison

Dynamic Programming:

say I have substring ss1, ss2 (both begin at the origin of their respective strings)
 I make a matrix distance[i][j] == edit distance between strings up to indices i, j

 distance[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + 1)

"""

def edit_distance(s1, s2):
  if len(s1) == 0 or len(s2) == 0:
    return max(len(s1), len(s2))
  distance = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
  for i in range(len(s1)):
    distance[i][0] = i
  for i in range(len(s2)):
    distance[0][i] = i
  for i in range(1, len(s1)):
    for j in range(1, len(s2)):
      if s1[i] == s2[j]:
        distance[i][j] = distance[i-1][j-1]
      else:
        distance[i][j] = min(
          distance[i-1][j],
          distance[i][j-1],
          distance[i-1][j-1]) + 1
  for row in distance:
    print(row)
  return distance[-1][-1]

def test_edits(s1, s2):
  print(f"{s1}, {s2} => {edit_distance(s1, s2)}")

test_edits('abccc', 'abBccS')