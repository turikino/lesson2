import random

school_classes = ['1a', '1b', '1c', '2a', '2b', '2c']
school_all_classes_score = []
for school_class in school_classes:
    scores = [random.randrange(1, 5, 1) for score in range(5)]
    school_class_dict = {'school_class' : school_class, 'scores' : scores}
    school_all_classes_score.append(school_class_dict)

for school_class in school_all_classes_score:
    sum_score = sum(school_class["scores"])
    print("В классе {} срединий балл: {}.".format(school_class["school_class"], sum_score))

