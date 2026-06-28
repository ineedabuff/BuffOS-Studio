from app.core.doctor.doctor import Doctor


def test_doctor_runs():
    results = Doctor().run()

    assert len(results) > 0
