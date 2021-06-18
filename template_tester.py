import parsing_utils
from parsing_utils import *




from db_structure import VarianTaskTemplate

def test_task(task):
	tsk, sols, true_s = parse_task_object(task)
	print(tsk)
	print(sols)
	print(true_s)



# task = VarianTaskTemplate()
# task.topic = "Числа и вычисления"
# task.diff = 1
# task.variables = """[constant_param("A",random.randint(-20,20)),constant_param("B",random.randint(-20,20)),
# 				variable_param("P_1", "", ["-1*",""]), variable_param("P_2",random.choice([\"+\",\"-\",\"*\"]),[\"+\",\"-\",\"*\"]),
# 				variable_param("P_3", "", ["-1*",""]), constant_param("RR", "(lambda : random.randint(-100,100))()")]"""
# task.is_graph = False
# task.grahp_template = None
# task.task_template = "Посчитайте результат вычисления выражения $A$ $P_2$ $B$"
# task.sol_template = "(lambda A, B : !P_1! A !P_2! !P_3! B)($A$, $B$)"
# task.is_variant = True
# task.num_solutions = 5


# task = VarianTaskTemplate()
# task.topic = "Числа и вычисления"
# task.diff = 1
# task.variables = """[constant_param("A",random.randint(1,20)),
# 					constant_param("B",random.randint(1,20)),
# 					constant_param("C",random.randint(1,20)),
# 					constant_param("D",random.randint(1,20)),
# 					constant_param("D1", random.choice(["огурцов", "гвоздей", "мячей", "кошачьего корма", "помидоров"])),
# 					constant_param("D2", random.choice(["томатов", "шурупов", "шариковых ручек", "конфет", "сахара"])),
# 					constant_param("D3", random.choice(["носков", "гаек", "ниток", "перцев", "изоленты"])),
# 					constant_param("D4", random.choice(["угля", "мыла", "авокадо", "собачьего корма", "макулатуры"])),	
# 				variable_param("P_1", "A", ["B","C","D"]),
# 				variable_param("P_2", "B", ["A","C","D"]),
# 				variable_param("P_3", "C", ["A","B","D"]),
# 				variable_param("P_4", "D", ["A","B","C"]),
# 				constant_param("RR", "(lambda : random.randint(1,100))()")]"""
# task.is_graph = False
# task.grahp_template = None
# task.task_template = "$A$ кг $D1$ стоят столько же, сколько $B$ кг $D2$. А $C$ кг $D2$ стоят столько же, сколько $D$ кг $D3$. Сколько процентов цена килограма $D3$ составляет от цены килограмма $D1$"
# task.sol_template = "(lambda A, B, C, D :  int((((!P_1!/!P_2!)*!P_3!)/!P_4!)*100))($A$, $B$, $C$, $D$)"
# task.is_variant = True
# task.num_solutions = 5




# task = VarianTaskTemplate()
# task.topic = "Числа и вычисления"
# task.diff = 1
# task.variables = """[constant_param("N",random.randint(3,7)),
# 					\"constant_param(\'Numbers\', [Fraction(random.randint(1,20), random.randint(2,20)) for i in range($N$)])\",
# 					constant_param("R", random.choice([True, False])),
# 					\"constant_param(\'OD\', \'убывания\' if $R$==True else \'возрастания\')\",
# 				\"variable_param(\'P_1\', [i for i in range($N$)], list(itertools.permutations([i for i in range($N$)])))\",
# 				\"constant_param(\'NL\', \', \'.join([str(x) for x in $Numbers$]))\",
# 				constant_param("RR", "(lambda : random.randint(1,100))()")]"""
# task.is_graph = False
# task.grahp_template = None
# task.task_template = "Расположите числа в порядке $OD$ : $NL$"
# task.sol_template = "(lambda Numbers : \", \".join(tuple(str((sorted(Numbers, reverse=$R$))[i]) for i in !P_1!)))($Numbers$)"
# task.is_variant = True
# task.num_solutions = 5

# test_task(task)

# task = VarianTaskTemplate()
# task.topic = "Числа и вычисления"
# task.diff = 1
# task.variables = """[constant_param("A0",Fraction(random.choice([x for x in range(-20,20) if x!=0]), random.choice([x for x in range(-20,20) if x!=0]))),
# 					 constant_param("D",Fraction(random.choice([x for x in range(-20,20) if x!=0]), random.choice([x for x in range(-20,20) if x!=0]))),
# 					 constant_param("IL", random.randint(3,5)),
# 					 constant_param("TL", random.randint(7,9)),
# 					 \"constant_param(\'SEQ\', \' \'.join([str(@A0@+@D@*x) for x in range($IL$)]))\",
# 					 \"constant_param(\'FSEQ\', [str(@A0@+@D@*x) for x in range($TL$)])\",
# 					 \"variable_param(\'P_1\', \'-1\', [i for i in range($TL$-1)])\",
# 					 variable_param("P_2", "+", ["-","*","/"]),
# 					 variable_param("P_3", "/2", ["/1","/4"]),
# 					 \"variable_param(\'P_4\', \'$TL$\', [i for i in range(1,$TL$-1)])\",
# 				constant_param("RR", "(lambda : random.randint(1,100))()")]"""
# task.is_graph = False
# task.grahp_template = None
# task.task_template = "Найдите сумму первых $TL$ членов арифметической прогрессии $SEQ$"
# task.sol_template = "(lambda A, TL, SEQ : str(((A!P_2!Fraction(SEQ[!P_1!]))!P_3!)*!P_4!))(@A0@, $TL$, $FSEQ$)"
# task.is_variant = True
# task.num_solutions = 5


#test_task(task)


#S - Solution
#R - Random
#L - From list