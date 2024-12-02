from Turing_Pattern_Simulator import simulator
from Turing_Pattern_Simulator import sweeper_1d
from Turing_Pattern_Simulator import sweeper_2d

#examples for simulator

simulator(k=0.057,F=0.029,output_type="gif",filename="maze",time_steps= 3000 ,add_noise=False)

simulator(k=0.054,F=0.014,output_type="gif",filename="moving spots",time_steps= 10000,add_noise=False)

simulator(k=0.057,F=0.029,output_type="gif",filename="maze w noise",time_steps= 3000 ,add_noise=True)

simulator(k=0.054,F=0.014,output_type="gif",filename="moving spots w noise",time_steps= 10000,add_noise=True)

#examples for sweeper

sweeper_1d(param_name='F', param_range=(0.02, 0.07, 0.01), simulator_args={'k': 0.06,'D_u': 0.16,'D_v': 0.08},output_dir="1d_F_sweep")
sweeper_2d(param1_name='F', param1_range=(0.02, 0.06, 0.01),param2_name='k',param2_range=(0.02, 0.06, 0.01), simulator_args={'D_u': 0.16,'D_v': 0.08,'time_steps': 3000},output_dir="2d_F_k_sweep")
