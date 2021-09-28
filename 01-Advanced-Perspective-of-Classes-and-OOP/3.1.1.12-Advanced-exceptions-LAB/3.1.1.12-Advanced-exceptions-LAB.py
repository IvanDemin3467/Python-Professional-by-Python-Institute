class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print(f'Fuel tank is full in {format(100 / 0)}')
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e


def batteries_check():
    try:
        print('Batteries are full in' + 0 + ' %')
    except TypeError as e:
        raise RocketNotReadyError('Problem with batteries') from e


def circuits_check():
    circuits = {'Vibration circuit': 'AT345-x', 'Landing circuit': 'XK567CD'}
    try:
        _1 = circuits['Vibration circuit']
        _2 = circuits['Landing circuit']
        _3 = circuits['Aiming circuit']
    except KeyError as e:
        raise RocketNotReadyError('Problem with circuits') from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
