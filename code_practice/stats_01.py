# importing libraries to check the performance of the code.

import cProfile
import pstats
from code01 import pasar_a_romanos_01 as f01
from code01 import otra_de_romanos as f02
from code01 import otra_de_romanos_02 as f03


# define variables to check the performance of the code.

ejemplo = 2721


# with cProfile.Profile() as pr:
#     pasar_a_romanos_01(ejemplo)

# stats = pstats.Stats(pr)
# stats.sort_stats(pstats.SortKey.TIME)
# stats.print_stats()
# stats.dump_stats('pasar_a_romanos_01.prof')    


num_runs = 10000  # Number of times to run the application
print(f'Running {num_runs} times')
profiler = cProfile.Profile()

for _ in range(num_runs):
    
    profiler.enable()
    
    # Your code here
    f03(ejemplo)

    profiler.disable()
profiler.print_stats()
stats = pstats.Stats(profiler)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()


if __name__ == '__main__':
    pass