class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be a Integer')
        if score < 0 or score > 100:
            raise ValueError('score must between 0~100!!!')
        self.__score = score


s = Student('张三', 59)
s.score = 60
print(s.score)
