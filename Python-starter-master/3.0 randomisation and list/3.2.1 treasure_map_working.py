<<<<<<< HEAD
row1=["🟥", "🟥", "🟥"]
row2=["🟥", "🟥", "🟥"]
row3=["🟥", "🟥", "🟥"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("enter the location you want to mark as visited, for example A1: ")
# extracting letter from input
letter=position[0].upper() # converting entered letter to capital
number=position[1]# extracting number from user input
ABC=['A','B','C']# mapping standard positions as in matrix indexing
letter_index=ABC.index(letter)# setting letter to it's standard index pattern e.g A:0, B:1, C:2
number_index=int(number)
map[letter_index][number_index]="🟩"
print(f"{row1}\n{row2}\n{row3}")
=======
row1=["🟥", "🟥", "🟥"]
row2=["🟥", "🟥", "🟥"]
row3=["🟥", "🟥", "🟥"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("enter the location you want to mark as visited, for example A1: ")
# extracting letter from input
letter=position[0].upper() # converting entered letter to capital
number=position[1]# extracting number from user input
ABC=['A','B','C']# mapping standard positions as in matrix indexing
letter_index=ABC.index(letter)# setting letter to it's standard index pattern e.g A:0, B:1, C:2
number_index=int(number)
map[letter_index][number_index]="🟩"
print(f"{row1}\n{row2}\n{row3}")
>>>>>>> refs/remotes/origin/main
