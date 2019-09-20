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
    source = urllib.request.urlopen('https://chercher.tech/aws-certification/aws-certification-practice-question-answers').read()
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
        rawanswer = ''
        for x in temp:
            if '(Correct)' in x:
                rawanswer = rawanswer + '|' + x.strip('\n(Correct)')
        answer.append(rawanswer.strip('|'))
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
    filecsv = open(soup.title.string + '.csv', mode='w', newline='', encoding='utf-8')
    fields = ['Question', 'Choice1', 'Choice2', 'Choice3', 'Choice4', 'Choice5', 'Answer']
    writer = csv.DictWriter(filecsv, fieldnames=fields)
    writer.writeheader()
    for i in range(0, len(question)):
        writer.writerow({'Question': question[i].strip(), 'Choice1': choice0[i].strip(), 'Choice2': choice1[i].strip(), 'Choice3': choice2[i].strip(), 'Choice4': choice3[i].strip(), 'Choice5': choice4[i].strip(), 'Answer': answer[i].strip()})


if __name__ == '__main__':
    make_content()
