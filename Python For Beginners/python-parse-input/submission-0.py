from typing import List

def read_integers() -> List[int]:
    input_list = input().split(",")
    ans = []
    for iyem in input_list:
        ans.append(int(iyem))
    return ans

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
