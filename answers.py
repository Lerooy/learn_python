def get_answer(question):
    answers = {'привет': 'И тебе привет!',
                'как дела': 'Лучше всех!',
                'пока': 'Увидимся'}
    print (answers.get(question.lower(), 'Я не понимаю!'))

if __name__ == '__main__':
    get_answer(input('Поговори со мной =) '))