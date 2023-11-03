
height = int(input("피라미드의 높이를 입력하세요: "))

# 피라미드를 출력합니다.
for i in range(1, height + 1):
    
    print(" " * (height - i), end="")
    
   
    print("*" * (2 * i - 1))
