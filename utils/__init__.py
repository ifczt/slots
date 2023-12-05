def convert_keys_to_numbers(d) -> dict:
    """将字典的key转换为数字"""
    if not isinstance(d, dict):
        return d

    return {int(key) if isinstance(key, str) and key.isdigit() else key: convert_keys_to_numbers(value) for key, value in d.items()}


def remove_str_key(d) -> dict:
    """删除字典中的字符串key"""
    if not isinstance(d, dict):
        return d

    return {key: remove_str_key(value) for key, value in d.items() if not isinstance(key, str)}
