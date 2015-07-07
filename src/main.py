from table import Table
from gui import Gui
from gevent import spawn

def read_datasheet(filename):
    data = {}
    data['balls'] = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('#'):
                continue
            elif line.startswith('['):
                ball_pos = line[1:-2].split(',')
                data['balls'].append((int(ball_pos[0]),
                                      int(ball_pos[1]),
                                      int(ball_pos[2])))
            elif '=' in line:
                entry = line.split('=')
                try:
                    data[entry[0]] = float(entry[1])
                except Exception, e:
                    print 'invalid datasheet: %s' % e
    return data


def read_player_data(filename):
    # TODO: validation checking
    return [ (0, -20000, 1200, 5000)]

def main():
    print 'Simulation started.'

    # Test initial table
    table_data = read_datasheet('../mdata/sample_table.data')
    shot_sequence = read_player_data('../mdata/shots.data')
    tbl = Table(table_data, shot_sequence)

    spawn(tbl.loop)

    gui = Gui(tbl, 350, 700)
    gui.start()

if __name__ == '__main__':
    main()
