
def tree(rows):

    if rows < 0 or rows % 2 == 0:
        print("Liczba rzędów powinna być wieksza od zera i nieparzysta.")
        return None

    n = rows
    for i in range(rows):

        for j in range(n):
            print(" ", end = "")
        
        for k in range(2*(rows - n)-1):
            print("*", end = "")
        
        print(" ")

        n = n-1

    for j in range((rows//7)+1):
        for i in range((rows)//2):
            print(" ", end = " ")
        
        print("*")

tree(9)