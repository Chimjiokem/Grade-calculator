a ='Welcome to LearnFactory!'
student_name = input('Enter your name: ')
print(f'Hello {student_name}! {a}')
exam_score = float(input('Enter your exam score: '))

if exam_score <= 0 or exam_score > 100:
    print(f'Hi, {student_name}.\n{exam_score} is an invalid score!')
else:
    if exam_score >= 90 or exam_score == 100:
        print(f'Hi, {student_name}. Your exam score is {exam_score}.\nCongratulations, you passed. You made an A! ')
    elif exam_score >= 80 or exam_score == 89:
        print(f'Hi, {student_name}. Your exam score is {exam_score}.\nYou passed. You made a B! ')
    elif exam_score >= 70 or exam_score == 79:
        print(f'Hi, {student_name}. Your exam score is {exam_score}.\nYou passed. You made a C! ')
    elif exam_score >= 60 or exam_score == 69:
        print(f'Hi, {student_name}. Your exam score is {exam_score}.\nYou passed. You made a D! ')
    elif exam_score < 60:
        print(f'Hi, {student_name}. Your exam score is {exam_score}.\nYou failed. You made an F! ')
