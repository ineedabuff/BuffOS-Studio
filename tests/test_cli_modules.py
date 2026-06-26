from app.cli.modules import create_runner


def test_create_runner_registers_default_modules():
    runner = create_runner(dry_run=True)

    names = [module.name for module in runner.modules]

    assert names == [
        "Operating System",
        "Firmware",
        "Secure Boot",
        "Filesystem",
        "Root Subvolume",
        "Home Subvolume",
        "Mount Options",
        "Timeshift",
        "grub-btrfs",
    ]

    assert runner.dry_run is True
