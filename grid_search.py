import os
# import torch
import subprocess

lambda_A = [1, 2, 3, 4, 5]
lambda_idt = [0.1, 1, 2, 5]
lambda_ctx = [0.1, 1, 2, 5]
list_options = []
# CHEN
dict_option1 = {"lambda_A": 2,
                "lambda_idt": 0.1,
                "lambda_ctx": 1
                }
# EDEN
dict_option2 = {"lambda_A": 2,
                "lambda_idt": 0.1,
                "lambda_ctx": 2
                }
# EDEN
dict_option3 = {"lambda_A": 2,
                "lambda_idt": 1,
                "lambda_ctx": 2
                }
# EDEN
dict_option4 = {"lambda_A": 2,
                "lambda_idt": 1,
                "lambda_ctx": 3
                }
# ITAY
dict_option5 = {"lambda_A": 2,
                "lambda_idt": 0.1,
                "lambda_ctx": 4
                }
# SHAY
dict_option6 = {"lambda_A": 5,
                "lambda_idt": 0.1,
                "lambda_ctx": 2
                }
# CHEN
dict_option7 = {"lambda_A": 1,
                "lambda_idt": 1,
                "lambda_ctx": 1
                }
# ITAY
dict_option8 = {"lambda_A": 10,
                "lambda_idt": 1.2,
                "lambda_ctx": 1.5
                }
# EDEN
dict_option9 = {"lambda_A": 5,
                "lambda_idt": 3,
                "lambda_ctx": 9
                }
# SHAY
dict_option10 = {"lambda_A": 5,
                 "lambda_idt": 1,
                 "lambda_ctx": 2
                 }
# SHAY
dict_option11 = {"lambda_A": 0.5,
                 "lambda_idt": 0.5,
                 "lambda_ctx": 5
                 }
# CHEN
dict_option12 = {"lambda_A": 1,
                 "lambda_idt": 0,
                 "lambda_ctx": 1
                 }

# CHEN
dict_option13 = {"lambda_A": 2,
                 "lambda_idt": 0,
                 "lambda_ctx": 1
                 }

# CHEN
dict_option14 = {"lambda_A": 0.5,
                 "lambda_idt": 0,
                 "lambda_ctx": 1
                 }
# CHEN
dict_option15 = {"lambda_A": 2,
                 "lambda_idt": 0.1,
                 "lambda_ctx": 0.5
                 }
# CHEN
dict_option16 = {"lambda_A": 1,
                 "lambda_idt": 0.1,
                 "lambda_ctx": 1
                 }
# CHEN
dict_option17 = {"lambda_A": 1.5,
                 "lambda_idt": 0.1,
                 "lambda_ctx": 1
                 }

# CHEN
dict_option18 = {"lambda_A": 0.1,
                 "lambda_idt": 0.1,
                 "lambda_ctx": 1
                 }
# CHEN
dict_option19 = {"lambda_A": 1.5,
                 "lambda_idt": 0.1,
                 "lambda_ctx": 2
                 }

# CHEN
dict_option20 = {"lambda_A": 0.1,
                 "lambda_idt": 0,
                 "lambda_ctx": 0.1
                 }

# CHEN
dict_option21 = {"lambda_A": 0.1,
                 "lambda_idt": 0.1,
                 "lambda_ctx": 0.1
                 }
# list_options.append(dict_option1)
# list_options.append(dict_option2)
# list_options.append(dict_option3)
# list_options.append(dict_option4)
# list_options.append(dict_option5)
# list_options.append(dict_option6)
# list_options.append(dict_option7)
# list_options.append(dict_option8)
# list_options.append(dict_option9)
# list_options.append(dict_option10)
# list_options.append(dict_option11)
# list_options.append(dict_option12)
# list_options.append(dict_option13)
# list_options.append(dict_option14)
# list_options.append(dict_option15)
# list_options.append(dict_option16)
list_options.append(dict_option17)
list_options.append(dict_option18)
list_options.append(dict_option19)
list_options.append(dict_option20)
list_options.append(dict_option21)
