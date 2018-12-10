from .fixtures import beat


def test_volumes(beat):
    volumes = beat.docker_metadata['Config']['Volumes']
    assert len(volumes) > 0
