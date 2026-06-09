"""Basic tests for MythosAI."""

import pytest
import asyncio
import os
from pathlib import Path


def test_import_mythosai():
    """Test that mythosai can be imported."""
    import mythosai
    assert mythosai.__version__ == "0.1.0"


def test_env_file_handling():
    """Test that environment file handling works."""
    # Test that dotenv can be imported (part of dependencies)
    from dotenv import load_dotenv
    assert load_dotenv is not None


def test_pydantic_models():
    """Test that pydantic is available for data models."""
    from pydantic import BaseModel
    
    class SampleModel(BaseModel):
        name: str
        value: int
    
    model = SampleModel(name="test", value=42)
    assert model.name == "test"
    assert model.value == 42


def test_pytest_asyncio_plugin():
    """Test pytest-asyncio plugin is working."""
    assert asyncio.get_event_loop() is not None


@pytest.mark.asyncio
async def test_async_functionality():
    """Test basic async functionality."""
    async def sample_async_func():
        return "async works"
    
    result = await sample_async_func()
    assert result == "async works"


def test_basic_assertion():
    """Basic test to verify pytest is working."""
    assert True
    assert 1 + 1 == 2
