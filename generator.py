import db_structure
from db_structure import VarianTaskTemplate, db

import parsing_utils
from parsing_utils import *
from random_utils import *


class task():
	def __init__(self, task_descr, answers, correct_answer):
		self.task_descr = task_descr
		self.answers = answers
		self.correct_answer = correct_answer

def generate_tasks(topics, topic_distr, diffs, diff_distr, a_tasks, b_tasks, seed=None):
	task_objects = VarianTaskTemplate.query.all()
	generated_tasks = []
	random_generator = stable_random_generator(seed)

	for i in range(a_tasks):
		tsk, sols, true_s = parse_task_object(random_generator.choice(task_objects), random_generator)
		generated_tasks.append(task(tsk, sols, true_s))
	#for t_a in task_objects:
	#	tsk, sols, true_s = parse_task_object(t_a)
	#	print(tsk)
	#	for i,s in enumerate(sols):
	#		print("{} : {}".format(i+1, s))
	#	print("[{}]".format(true_s))
	#	print("-"*10)
	return generated_tasks

#generate_tasks(["Числа и выражения"],[1],[1],[1])


