from dataclasses import dataclass


# def execute_command(command):
#     if command == 'ls':
#         print('$ listing files')
#     elif command == 'cd':
#         print('$ changing directory')
#     else:
#         print('$ command not implemented')

#     print('...rest of the code')


# execute_command('pwd')

# BASIC
# case 'batata': = if case == 'batata':
# case _: == else (default case)


# def execute_command(command):
#     match command:
#         case 'ls':
#             print('$ listing files')
#         case 'cd':
#             print('$ changing directory')
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command('pwd')


# Commands in match
# match command_food.split(' '): # split two values
#     case ['like', food, ]: # get a literal and a variable

# def execute_command(command):
#     match command.split():
#         case ['ls', path, *_]:
#             print('$ listing files from', path)
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('cd /Users/')

# Case with or inside a list
# case ['enjoy' | 'love', food]:

# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', path, *_]:
#             print('$ listing files from', path)
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('list /home/ /Users /mais')

# With rest
# case ['like', *foods]


# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories]:
#             for directory in directories:
#                 print('$ listing directory from', directory)
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command('ls /home/ /Users /mais')

# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories] if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing directory from', directory)
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             print('$ listing directory from', directories[0])
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command('ls /home/ /Users /mais')

# def execute_command(command):
#     match command.split():
#         case [
#             'ls' | 'list' as the_command, *directories
#         ] as the_list if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing directory from', directory)
#             print(f'{the_command=}, {the_list=}')
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             print('$ listing directory from', directories[0])
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command('ls /home/ /Users /mais')

# Com dicionarios
# case {'name': _, 'last': 'Doe'}:
# case {'name': 'Otávio' as name, 'last': 'Doe'} as data:


# def execute_command(command):
#     match command:
#         case {'command': 'ls', 'directories': [_, *_]}:
#             for directory in command['directories']:
#                 print('$ listing ALL directories from', directory)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command({'command': 'ls', 'directories': []})
# execute_command('ls /one/')

# Com objetos (classes)

@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command: Command):
    match command:
        case Command(command='ls', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing to', directory)
        case _:
            print('$ command not implemented')

    print('...rest of the code')


command_1 = Command('ls', ['/users'])
command_2 = Command('cd', ['/users'])

execute_command(command_1)
execute_command(command_2)
