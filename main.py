import json

# map json class to python 

class Question():

    def __init__(self, question):
        self.question = question
        self.answers = []

if __name__ == '__main__':
    with open('questions.json') as json_file:
        data = json.load(json_file)
        questions = []
        for p in data['questions']:
            question = Question(p['question'])
            questions.append(question)

    print(question.question)
    print(question.answers)

   