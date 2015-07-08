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


def read_player_data(filename, datasheet):
    shots = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('['):
                shot_data = line[1:-2].split(',')

                shot = [int(shot_data[0]),
                        int(shot_data[1]),
                        int(shot_data[2]),
                        int(shot_data[3])]
                '''
                indicies
                0 - x_vel
                1 - y_vel
                2 - x_reset_pos
                3 - y_reset_pos
                '''
                # cap velocities
                if shot[0] > datasheet['max_x_vel']:
                    shot[0] = datasheet['max_x_vel']
                    print 'capping x vel'

                if shot[0] < -1*datasheet['max_x_vel']:
                    shot[0] = -1*datasheet['max_x_vel']
                    print 'capping x vel'

                if shot[1] > datasheet['max_y_vel']:
                    shot[1] = datasheet['max_y_vel']
                    print 'capping y vel'

                if shot[1] < -1*datasheet['max_y_vel']:
                    shot[1] = -1*datasheet['max_y_vel']
                    print 'capping y vel'

                # cap ball placement
                if shot[2] < (datasheet['pocket_offset'] +
                              datasheet['pocket_radius'] +
                              datasheet['b_radius']):
                    shot[2] = (datasheet['pocket_offset'] +
                               datasheet['pocket_radius'] +
                               datasheet['b_radius'])
                    print 'capping x reset position'

                if shot[2] > (datasheet['width'] - datasheet['pocket_offset'] -
                              datasheet['pocket_radius'] - datasheet['b_radius']):
                    shot[2] = (datasheet['width'] - datasheet['pocket_offset'] -
                               datasheet['pocket_radius'] - datasheet['b_radius'])
                    print 'capping x reset position'

                if shot[3] < (datasheet['length']/2 +
                              datasheet['pocket_radius'] +
                              datasheet['b_radius']):
                    shot[3] = (datasheet['length']/2 +
                               datasheet['pocket_radius'] +
                               datasheet['b_radius'])
                    print 'capping y reset position'

                if shot[3] > (datasheet['length'] - datasheet['pocket_offset'] -
                              datasheet['pocket_radius'] - datasheet['b_radius']):
                    shot[3] = (datasheet['length'] - datasheet['pocket_offset'] -
                               datasheet['pocket_radius'] - datasheet['b_radius'])
                    print 'capping y reset position'

                shots.append(shot)

    return shots

def main():
    print 'Simulation started.'

    # Test initial table
    table_data = read_datasheet('../mdata/sample_table.data')
    shot_sequence = read_player_data('../mdata/shots.data', table_data)
    tbl = Table(table_data, shot_sequence)

    spawn(tbl.loop)

    gui = Gui(tbl, 350, 700)
    gui.start()

if __name__ == '__main__':
    main()
