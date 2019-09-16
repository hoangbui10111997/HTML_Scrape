import bs4 as bs
import urllib.request
import csv


def make_content():
    question = []
    choice0 = []
    choice1 = []
    choice2 = []
    choice3 = []
    choice4 = []
    answer = []
    choiceraw = []
    source = urllib.request.urlopen('https://chercher.tech/aws-certification/aws-dva-c00-certified-developer-associate-practice-exam-set-1').read()
    soup = bs.BeautifulSoup(source, 'lxml')
    content_raw = soup.find_all('div', class_='card mb-3')
    content = content_raw[0]
    questions = content.find_all('h5')
    for item in questions:
        question.append(item.string)
    choices = content.find_all('ul', class_='diamond')
    for items in choices:
        raw = ''
        for item in items.find_all('li'):
            raw += item.string + '|'
        choiceraw.append(raw.strip('|'))
    for i in range(0, len(question)):
        temp = choiceraw[i].split('|')
        for x in temp:
            if '(Correct)' in x:
                answer.append(x.strip('\n(Correct)'))
                break
        condition = len(temp)
        if condition == 2:
            choice0.append(temp[0].strip('\n(Correct)'))
            choice1.append(temp[1].strip('\n(Correct)'))
            choice2.append('')
            choice3.append('')
            choice4.append('')
        elif condition == 3:
            choice0.append(temp[0].strip('\n(Correct)'))
            choice1.append(temp[1].strip('\n(Correct)'))
            choice2.append(temp[2].strip('\n(Correct)'))
            choice3.append('')
            choice4.append('')
        elif condition == 4:
            choice0.append(temp[0].strip('\n(Correct)'))
            choice1.append(temp[1].strip('\n(Correct)'))
            choice2.append(temp[2].strip('\n(Correct)'))
            choice3.append(temp[3].strip('\n(Correct)'))
            choice4.append('')
        else:
            choice0.append(temp[0].strip('\n(Correct)'))
            choice1.append(temp[1].strip('\n(Correct)'))
            choice2.append(temp[2].strip('\n(Correct)'))
            choice3.append(temp[3].strip('\n(Correct)'))
            choice4.append(temp[4].strip('\n(Correct)'))
    filecsv = open('AWS.csv', mode='w', newline='')
    fields = ['Question', 'Choice1', 'Choice2', 'Choice3', 'Choice4', 'Choice5', 'Answer']
    writer = csv.DictWriter(filecsv, fieldnames=fields)
    writer.writeheader()
    for i in range(0, len(question)):
        writer.writerow({'Question': question[i], 'Choice1': choice0[i], 'Choice2': choice1[i], 'Choice3': choice2[i], 'Choice4': choice3[i], 'Choice5': choice4[i], 'Answer': answer[i]})


if __name__ == '__main__':
    make_content()