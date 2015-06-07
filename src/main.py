from table import Table
from gui import Gui
from gevent import spawn

def main():
    print 'Simulation started.'

    # Test initial table
    # TODO: replace with values from input file scraper
    tbl = Table(2700, (2700*2), 50, 100, 25)
    # for i in range (0, 10000):
    #     tbl.add_ball(i, i, i)

    tbl.add_ball(1000, 1000, 1)

    spawn(tbl.loop)

    gui = Gui(tbl, 400, 800)
    gui.start()
    for t_ball in tbl.balls:
        print t_ball.x_pos
    print len(tbl.balls)

if __name__ == '__main__':
    main()
