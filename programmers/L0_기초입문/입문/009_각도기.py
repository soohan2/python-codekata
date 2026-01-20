# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 우수한
# 작성일: 2026. 01. 20. 13:26:45

def solution(angle):
    if angle == 180:
        return 4
    elif angle > 90 and angle < 180:
        return 3
    elif angle == 90:
        return 2
    else:
        return 1