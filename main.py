from Models import *

def main():
    sim = Simulation("omaha", 100)
    sim.warmup()
    sim.run_simulation()

            
if __name__ == '__main__':
    main()
