from patterns.creational.borg import Borg, YourBorg


class TestBorg:
    def setup_method(self):
        self.b1 = Borg()
        self.b2 = Borg()
        # creating YourBorg instance implicitly sets the state attribute
        # for all borg instances.
        self.ib1 = YourBorg()

    def teardown_method(self):
        self.ib1.state = "Init"

    def test_initial_borg_state_shall_be_init(self):
        b = Borg()
        assert b.state == "Init"

    def test_changing_instance_attribute_shall_change_borg_state(self):
        self.b1.state = "Running"
        assert self.b1.state == "Running"
        assert self.b2.state == "Running"
        assert self.ib1.state == "Running"

    def test_instances_shall_have_own_ids(self):
        assert id(self.b1) != id(self.b2), id(self.ib1)
