import json
#!/usr/bin/python3
"""returns an object represented by a JSON string"""
def from_json_string(my_str):
    """returns a string from a json"""
    return json.loads(my_str)
