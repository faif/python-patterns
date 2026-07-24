from patterns.structural.proxy import Proxy, client


class TestProxy:
    def test_do_the_job_for_admin_shall_pass(self, capsys):
        client(Proxy(), "admin")
        assert capsys.readouterr().out == (
            "[log] Doing the job for admin is requested.\n"
            "I am doing the job for admin\n"
        )

    def test_do_the_job_for_anonymous_shall_reject(self, capsys):
        client(Proxy(), "anonymous")
        assert capsys.readouterr().out == (
            "[log] Doing the job for anonymous is requested.\n"
            "[log] I can do the job just for `admins`.\n"
        )
