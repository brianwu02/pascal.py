class ScannerException(Exception):
    pass

if __name__ == "__main__":
    e = ScannerException('val', {'error':'this error'})
    raise e
