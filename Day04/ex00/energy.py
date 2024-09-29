import itertools

def fix_wiring(cables, sockets, plugs):
    filtered_cables = list(filter(lambda x: isinstance(x, str), cables))
    filtered_sockets = list(filter(lambda x: isinstance(x, str), sockets))
    filtered_plugs = list(filter(lambda x: isinstance(x, str), plugs))

    part1 = (
        f"plug {cable} into {socket} using {plug}" 
        for cable, socket, plug in zip(filtered_cables, filtered_sockets, filtered_plugs)
    )

    part2 = (
        f"weld {cable} to {socket} without plug" 
        for cable, socket in zip(filtered_cables[len(filtered_plugs):], filtered_sockets[len(filtered_plugs):])
    )
    
    return itertools.chain(part1, part2)

def main():
    print("FIRST");
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']

    for command in fix_wiring(cables, sockets, plugs):
        print(command)
    
    print("SECOND");
    plugs1 = ['plugZ', None, 'plugY', 'plugX']
    sockets1 = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables1 = ['cable2', 'cable1', False]

    for command in fix_wiring(cables1, sockets1, plugs1):
        print(command)

if __name__ == "__main__":
    main()
