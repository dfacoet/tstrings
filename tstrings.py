from string import templatelib


def t_item_to_str(i: str | templatelib.Interpolation) -> str:
    match i:
        case str():
            return i
        case templatelib.Interpolation(value=value, format_spec=format_spec):
            # TODO: do something about conversion
            return format(value, format_spec)


def t_string_to_str(t: templatelib.Template) -> str:
    return "".join(map(t_item_to_str, t))
