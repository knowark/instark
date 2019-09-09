from instark.infrastructure.core.configuration import (
    TrialConfig, MemoryRegistry, Context)


def test_memory_registry_context_instantiation():
    config = TrialConfig()
    registry = MemoryRegistry(config)
    context = Context(config, registry)
    assert context.config == config
    assert context.registry == registry
