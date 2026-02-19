import uuid
import time

class DataGenerator:
    """
    Production-ready test data generator
    Ensures uniqueness across:
    - Parallel execution
    - CI runs
    - Multiple test sessions
    """

    @staticmethod
    def generate_unique_suffix() -> str:
        return uuid.uuid4().hex[:6]
    
    @staticmethod
    def generate_employee_name():
        unique_suffix = DataGenerator.generate_unique_suffix()
        timestamp = int(time.time())

        first_name = f"AutoFN_{unique_suffix}"
        middle_name = f"AutoMN_{unique_suffix}"
        last_name = f"AutoLN_{timestamp}"

        return first_name, middle_name, last_name
