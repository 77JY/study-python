from collections import Counter

def solution(id_list, report, k):
    user_report = Counter(report)
    report_list = {}
    answer = {}

    for i in id_list:
        report_list[i] = []
        answer[i] = 0

    for i in user_report.keys():
        report_name = i.split()
        report_list[report_name[1]].append(report_name[0])

    for i in id_list:
        if k <= len(report_list[i]):
            for j in report_list[i]:
                answer[j] += 1

    return(list(answer.values()))