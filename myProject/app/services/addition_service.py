import multiprocessing
import logging

def add_chunk(numbers):
    return sum(numbers)

def process_addition(payload):
    try:
        with multiprocessing.Pool() as pool:
            results = pool.map(add_chunk, payload)
        return results
    except Exception as e:
        logging.error(f"Error in process_addition: {e}")
        raise
