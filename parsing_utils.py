import re

from fractions import Fraction
import itertools
from random_utils import *




class param():
	def __init__(self, name, value, optional_param=None):
		self.name=name
		self.value=value
		if optional_param!=None:
			self.optional_param=optional_param
	def get_value(self, *args):
		return str(self.value)
	def get_raw(self, *args):
		return self.value.__repr__()
	def __repr__(self):
		return "{} : {}".format(self.name, self.value)

class variable_param(param):
	def __init__(self, name, value, options_list, optional_param=None):
		super().__init__(name, value)
		self.options_list = options_list
	def get_value(self, is_optional, generator, *args):
		val = self.value if not is_optional else generator.choice(self.options_list)
		return str(val)
	def get_raw(self, is_optional, generator, *args):  # FUNCTION FOR SPECIAL REPRESENTATION
		val = self.value if not is_optional else generator.choice(self.options_list)
		return val.__repr__()

class constant_param(param):
	def __init__(self, name, value, optional_param=None):
		super().__init__(name, value, optional_param)



def parse_line(line, var_dict, is_optional, generator):
	line = re.sub(r'[$]{1}(.*?)[$]{1}', lambda x : var_dict[x.group()[1:-1]].get_value(is_optional, generator), line)
	line = re.sub(r'[!]{1}(.*?)[!]{1}', lambda x : var_dict[x.group()[1:-1]].get_value(is_optional, generator), line)
	line = re.sub(r'[@]{1}(.*?)[@]{1}', lambda x : var_dict[x.group()[1:-1]].get_raw(is_optional, generator), line)
	return line


# def parse_vars_dependencies()



def parse_task(test_template, sol_template, variables, is_variant, num_variants, generator):
	vars_list = eval(variables,globals(), {"random":generator})
	unresolved_vars = list(filter(lambda x : isinstance(x, str),vars_list))

	var_dict = {v.name:v for v in vars_list if v not in unresolved_vars}

	print("*"*50)
	for u_v in unresolved_vars:
		r = parse_line(u_v, var_dict, False, generator)
		#print(r)
		resolved_var = eval(parse_line(u_v, var_dict, False, generator),globals(), {"random":generator})
		var_dict[resolved_var.name]=resolved_var


	task_line = parse_line(test_template, var_dict, False, generator)
	sols = set()
	true_solution = parse_line(sol_template, var_dict, False, generator)
	sols.add(true_solution)

	tries, tolerance = 0,30
	while len(sols)!=num_variants and tries<tolerance:
		sols.add(parse_line(sol_template, var_dict, True, generator))


	#for s in sols:
	#	print(s)

	sols = set(map(lambda x :eval(x), sols))
	if(len(sols)<num_variants):
		while(len(sols))<num_variants:
			sols.add(eval(var_dict["RR"].get_value(),globals(), {"random":generator}))

	sols = list(sols)
	random.shuffle(sols)

	#print(task_line)
	#for i,s in enumerate(sols):
	#	print("{} : {}".format(i+1, s))
	return task_line, sols, eval(true_solution,globals(), {"random":generator})

def parse_task_object(task, generator):
	return parse_task(task.task_template, task.sol_template, task.variables, task.is_variant, task.num_solutions, generator)