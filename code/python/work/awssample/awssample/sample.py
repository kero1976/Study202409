from typing import List
import random
import math

def g_rand() -> List[int]:
  num_list = []
  for i in range(5):
      num_list.append(random.randint(1, 100))
  return num_list

def g_sums(numbers: List[int]) -> int:
  total = 0
  for n in numbers:
      total += n
  return total

def p_res(prt_numbers: int, prt_total: List[int]) -> None:
    print("The random numbers are:", prt_numbers)
    print("The sum is:", prt_total)

if __name__ == "__main__":
    numbers = g_rand()
    total = g_sums(numbers)
    p_res(numbers, total)