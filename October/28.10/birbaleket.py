import csv

with open(r'C:\Users\User\Desktop\GIT AIT Akbar\October\28.10\exam_final.csv') as fid:
    exams = list(csv.reader(fid))

header = exams[0]
mid = exams[61]
midterm_index = mid.index('midterm')



student_index = header.index('names')
id_index = header.index('id')

def get_studs_average():
    dict = {}
    for i in exams[1:61]:  

        if i[student_index] not in dict:
            dict[i[student_index]] = [[], None]  

        row = i[:midterm_index]
        for j in row:
            if j == 'absent':
                dict[i[student_index]][0].append(0)
            else:
                try:
                    dict[i[student_index]][0].append(int(j))
                except ValueError:
                    pass

        for j in i[midterm_index + 1:]:
            if j == 'absent':
                dict[i[student_index]][0].append(0)
            else:
                try:
                    dict[i[student_index]][0].append(int(j))
                except ValueError:
                    pass

        if i[midterm_index] == 'absent':
            dict[i[student_index]][1] = 0
        else:
            dict[i[student_index]][1] = int(i[midterm_index])

    average = {}
    for name, arr in dict.items():
        average[name] = round(((sum(sorted(arr[0])[-6:]) / 6) * 0.7) + (arr[1] * 0.075))

    return average

print(get_studs_average())
