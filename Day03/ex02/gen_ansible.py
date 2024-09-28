import yaml

def generate_ansible_playbook(todo_file='../../materials/todo.yml', deploy_file='deploy.yml'):
    with open(todo_file, 'r') as f:
        todo = yaml.safe_load(f)

    deploy = [{
        'hosts': 'all',
        'tasks': []
    }]

    deploy[0]['tasks'].append({
        'name': 'Ensure destination directory exists',
        'file': {
            'path': './ansible_test/',
            'state': 'directory'
        }
    })

    deploy[0]['tasks'].append({
        'name': 'Install packages',
        'package': {
            'name': todo['server']['install_packages'],
            'state': 'present'
        }
    })

    deploy[0]['tasks'].append({
        'name': 'Copy exploit.py',
        'copy': {
            'src': '../ex00/exploit.py',
            'dest': './ansible_test/exploit.py'
        }
    })

    deploy[0]['tasks'].append({
        'name': 'Copy producer.py',
        'copy': {
            'src': '../ex01/producer.py',
            'dest': './ansible_test/producer.py'
        }
    })

    deploy[0]['tasks'].append({
        'name': 'Copy consumer.py',
        'copy': {
            'src': '../ex01/consumer.py',
            'dest': './ansible_test/consumer.py'
        }
    })

    deploy[0]['tasks'].append({
        'name': 'Debug copy destination',
        'debug': {
            'msg': 'Copying files to ansible_test directory'
        }
    })

    deploy[0]['tasks'].append({
        'name': 'Run producer.py',
        'command': 'python3 ./ansible_test/producer.py'
    })

    deploy[0]['tasks'].append({
        'name': 'Run consumer.py with bad guy accounts',
        'shell': 'python3 ./ansible_test/consumer.py -e ' + ','.join(todo['bad_guys']) + ' &',
        'async': 10,
        'poll': 0
    })

    with open(deploy_file, 'w') as f:
        yaml.dump(deploy, f, default_flow_style=False)

if __name__ == "__main__":
    generate_ansible_playbook()

