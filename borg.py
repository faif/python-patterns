class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Running'

    def __str__(self):
        return self.state

if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    print('rm1 state: {}'.format(rm1))
    print('rm2 state: {}'.format(rm2))

    rm2.state = 'Idle'

    print('rm1 state: {}'.format(rm1))
    print('rm2 state: {}'.format(rm2))

    print('rm1 id: {}', id(rm1))
    print('rm2 id: {}', id(rm2))
