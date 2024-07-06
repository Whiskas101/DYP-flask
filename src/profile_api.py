import cProfile
import pstats
from api import app

def run_profiler():
    profiler = cProfile.Profile()
    profiler.enable()

    
    try: 
        app.run(debug=True, host="0.0.0.0", port=5000)
    
    finally:
        profiler.disable()
        
        with open('profile stats.prof', "w") as f:
            ps = pstats.Stats(profiler, stream=f)
            ps.strip_dirs().sort_stats('cumulative').print_stats()
            
run_profiler()
        