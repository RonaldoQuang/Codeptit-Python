"""
Thang điểm IELTS được tính từ 1.0 - 9.0 IELTS (Overall điểm thi IELTS được tính trung bình cộng điểm 4 kỹ năng Reading, Listening, Speaking và Writing).
4 kỹ năng của IELTS cũng tính từ 1.0-9.0 để sau đó tính điểm thi IELTS Overall.
Cả 2 phần thi nghe (Listening) và đọc (Reading) đều có 40 câu hỏi thí sinh cần trả lời. 
Với một câu trả lời đúng sẽ được 1 điểm, tối đa là 40 điểm và quy đổi sang thang điểm 1.0 - 9.0 dựa trên tổng số câu trả lời đúng.
Dưới đây là bảng điểm quy đổi sẽ giúp cho các bạn hiểu hơn về cách chuyển đổi điểm cho từng phần thi Reading và Listening.

Correct answers
Band score
 39 - 40
 9.0
 37- 38
 8.5
 35 - 36
 8.0
 33 - 34
 7.5
 30 - 32
 7.0
 27 - 29
 6.5
 23 - 26
 6.0
 20 - 22
 5.5
 16 - 19
 5.0
 13 - 15
 4.5
 10 - 12
 4.0
 7- 9
 3.5
 5 - 6
 3.0
 3 - 4
 2.5
Thang điểm IELTS trên bảng kết quả của thí sinh sẽ thể hiện điểm của từng kỹ năng thi cùng với điểm overall. 
Phần điểm tổng sẽ được tính dựa trên điểm trung bình cộng của 4 kỹ năng.
Điểm tổng của 4 kỹ năng sẽ được làm tròn số theo quy ước chung như sau: 
Nếu điểm trung bình cộng của 4 kỹ năng có số lẻ là .25, thì sẽ được làm tròn lên thành .5, còn nếu là .75 sẽ được làm tròn thành 1.0.
Một trung tâm tổ chức thi thử Tiếng Anh cho các học viên. Hãy giúp trung tâm tính điểm overall dựa trên kết quả bài làm của thí sinh nhé.
Input:
Dòng đầu cho số T là số lượng thí sinh
T dòng tiếp theo mỗi dòng cho 4 số là số câu đúng lần lượt của kỹ năng Reading, Listening, điểm kỹ năng speaking, và điểm kỹ năng writing.
Output:
In ra kết quả theo từng dòng.
Input
DATA.in
2
15 25 5.0 5.5
22 32 6.0 6.0
Output
5.5
6.0
"""

from math import *

def ielts_band(n):
    if n >= 39 and n <= 40:
        return 9.0
    if n >= 37 and n <= 38:
        return 8.5
    if n >= 35 and n <= 36:
        return 8.0
    if n >= 33 and n <= 34:
        return 7.5
    if n >= 30 and n <= 32:
        return 7.0
    if n >= 27 and n <= 29:
        return 6.5
    if n >= 23 and n <= 26:
        return 6.0
    if n >= 20 and n <= 22:
        return 5.5
    if n >= 16 and n <= 19:
        return 5.0
    if n >= 13 and n <= 15:
        return 4.5
    if n >= 10 and n <= 12:
        return 4.0
    if n >= 7 and n <= 9:
        return 3.5
    if n >= 5 and n <= 6:
        return 3.0
    if n >= 3 and n <= 4:
        return 2.5
    return 0.0  

def lam_tron(n):
    x=int(n)
    y=n-x
    if y<0.25:
        return float(x)
    elif y<0.75:
        return float(x)+0.5
    else:
        return float(x)+1.0

if __name__ == '__main__':
    for _ in range (int(input())):
        r, l, s, w=map(float,input().split())
        r=ielts_band(r)
        l=ielts_band(l)
        tb=(r+l+s+w)/4.0
        print("{:.1f}".format(lam_tron(tb)))

        