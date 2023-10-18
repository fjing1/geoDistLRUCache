from packaging import version

def compare_versions(version1: str, version2: str) -> int:
    """Compare two version strings.

    :param version1: A string representing the first version.
    :param version2: A string representing the second version.
    :return: -1 if version1 < version2, 0 if version1 == version2, 1 if version1 > version2
    """
    if version.parse(version1) < version.parse(version2):
        return f'"{version1}" is less than "{version2}"'
    elif version.parse(version1) == version.parse(version2):
        return f'"{version1}" is equal to "{version2}"'
    else:
        return f'"{version1}" is greater than "{version2}"'

print(compare_versions("1.2", "1.1"))
print(compare_versions("1.0", "1.0"))
print(compare_versions("1.0", "1.0.1"))
print(compare_versions("3.3.3", "3.3.10"))
print(compare_versions("0.0.0", "0.0.0"))
