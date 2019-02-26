import random

school_classes = ['1a', '1b', '1c', '2a', '2b', '2c']
school_all_classes_score = []
for school_class in school_classes:
    scores = [random.randrange(1, 6, 1) for score in range(5)]
    school_class_dict = {'school_class' : school_class, 'scores' : scores}
    school_all_classes_score.append(school_class_dict)

all_class_score = []
for school_class in school_all_classes_score:
    class_sum_score = sum(school_class["scores"])/len(school_class["scores"])
    all_class_score.append(class_sum_score)
    print("В классе {} срединий балл: {}.".format(school_class["school_class"], int(class_sum_score)))

all_classes_sum_score = sum(all_class_score)/len(school_classes)
print("Во всей школе средний балл: {}.".format(int(all_classes_sum_score)))
