# def fuc(num: int) ->int:
#     if num == 0:
#         return 1
#     else:
#         result = 1
#         for x in range(1, num + 1):
#             result *= 1
#     return result

# print(fuc(5))

# def fac(n: int) -> int:
    # if n == 0 or n == 1:
        # return 1
    # return n * fac(n-1)
# print(fac(5))

# def rev_str(a: str) ->str:
#     if len(a) <= 1:
#         return a
#     return rev_str(a[1:]) + a[0]

# print(rev_str("Hello"))

# def fibonachi(n: int) -> int:
    # if n == 0:
        # return 0
    # if n == 1:
        # return 1
    # return fibonachi(n-1) + fibonachi(n -2)
# print(fibonachi(7))

from typing import Dict, Tuple, List
import json

Order = Tuple[int, str, float]
with open("data.json", "r", encoding="UTF-8") as f:
    orders:Dict[str, Order] = json.load(f)
def list_sum(orders: Dict[str,Order]) -> List[float]:
    price = lambda v:v[2]
    return list(map(price, orders.values()))
total_sum = sum(list_sum(orders))

print(total_sum)