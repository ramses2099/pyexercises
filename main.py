from typing import List

type Array = List[int]
type Output = tuple[int, int]

def sumTwo(arr: Array, target: int) -> Output:
    left: int = 0
    rigth: int = len(arr) - 1

    while(left < rigth):
        sum = arr[left] + arr[rigth]
        if(sum == target):
            return (left+1, rigth+1)
        elif(sum<target):
            left = left + 1
        else:
            rigth = rigth - 1
    return (0,0)
    

def main() -> None:
    inArr = [2,7,11,15]
    target = 9
    res = sumTwo(inArr, target)
    print(*res)

if __name__ == "__main__":
    main()