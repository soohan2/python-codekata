# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 우수한
# 작성일: 2026. 01. 20. 13:47:57

def solution(n, k):
    drink = n // 10
    price = (n*12000) + (k*2000) - (drink*2000)
    
    return price