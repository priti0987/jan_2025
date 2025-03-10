row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
#print matrixx
print(f"{row1}\n{row2}\n{row3}")
# print(row1)
# print(row2)
# print(row3)
matrix= [row1,row2,row3]
position=input("Enter position where money need to hide : ")
x_position = int(position[0])
y_position = int(position[1])
row_selected = matrix[x_position-1]
row_selected[y_position-1]="X"
print(f"{row1}\n{row2}\n{row3}")
