import xmltodict  # XML to dictionary conversion

def xml_to_json(xml_text: str) -> dict:
    """
    Converts XML text to a JSON-like dictionary.
    """
    return xmltodict.parse(xml_text)