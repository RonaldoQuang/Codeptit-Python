"""
Cho danh  sách chủ đề và bộ câu hỏi đi kèm theo chủ đề đó trong một bộ đề bài Tiếng Anh.
Mỗi bộ câu hỏi theo chủ đề sẽ cách nhau một dòng trống. Mỗi câu hỏi được viết trên một dòng.
Ghi ra thống kê số lượng câu hỏi theo từng chủ đề. Thứ tự của chủ đề ở kết quả được giữ nguyên với thứ tự xuất hiện trong dữ liệu vào.
Input:
Dòng đầu cho tổng số dòng dữ liệu
Các dòng tiếp theo là danh sách các chủ đề, câu hỏi.
Output:
In ra kết quả theo yêu cầu
Input
9
Home/accommodation
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?
 
Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?
Output
Home/accommodation: 3
Study: 3
"""
from math import *

if __name__ == '__main__':
    mp={}
    a=[]
    a.append("")
    b=[]
    for _ in range (int(input())):
        s=input()
        a.append(s)
    a.append("")
    for i in range (len(a)):
        if a[i]=="":
            b.append(i)
    for i in range (len(b)-1):
        mp[a[b[i]+1]]=b[i+1]-b[i]-2
    for x, y in mp.items():
        print(x,": ",y,sep="")


        
        
        
        

                