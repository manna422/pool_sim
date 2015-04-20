from table import Table
from gui import Gui

def main():
    print 'Simulation started.'

    # Test initial table
    # TODO: replace with values from input file scraper
    tbl = Table(2700, (2700*2), 50, 50, 25)
    for i in range (0, 10000):
        tbl.add_ball(i, i, i)

    gui = Gui(tbl, 400, 800)
    gui.start()
    for t_ball in tbl.balls:
        print t_ball.x_pos
    print len(tbl.balls)

if __name__ == '__main__':
    main()
