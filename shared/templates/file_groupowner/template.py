from ssg.utils import parse_template_boolean_value
from ssg.utils import ensure_file_paths_and_file_regexes_are_correctly_defined


def preprocess(data, lang):
    ensure_file_paths_and_file_regexes_are_correctly_defined(data)

    data["recursive"] = parse_template_boolean_value(data,
                                                     parameter="recursive",
                                                     default_value=False)

    try:
        int(data["gid_or_name"])
        data["group_represented_with_gid"] = True
    except ValueError:
        data["group_represented_with_gid"] = False

    if data["group_represented_with_gid"] == False:
        groups = data["gid_or_name"].split("|")
        if any(element.isnumeric() for element in groups):
            raise ValueError("gid_or_name list cannot contain gids when there are multiple groups")

    if lang == "oval":
        data["fileid"] = data["_rule_id"].replace("file_groupowner", "")
    return data
