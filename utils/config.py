"""Configuration module for OrangeHRM test automation.

Loads settings from environment variables with sensible defaults.
"""
import os
from dataclasses import dataclass


@dataclass
class Settings:
    """Application settings for test execution."""
    base_url: str
    admin_username: str
    admin_password: str
    employee_username: str
    employee_password: str
    headless: bool


def load_settings() -> Settings:
    """Load configuration from environment variables.

    Returns:
        Settings: Configuration object with values from env vars or defaults.
    """
    return Settings(
        base_url=os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/"),
        admin_username=os.getenv("ADMIN_USERNAME", "Admin"),
        admin_password=os.getenv("ADMIN_PASSWORD", "admin123"),
        employee_username=os.getenv("EMPLOYEE_USERNAME", ""),
        employee_password=os.getenv("EMPLOYEE_PASSWORD", ""),
        headless=os.getenv("HEADLESS", "true").lower() == "true",
    )


# Global settings instance - loaded once at module import
settings = load_settings()
