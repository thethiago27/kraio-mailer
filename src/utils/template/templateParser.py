from typing import Dict


def template_parser(template: str, args: Dict[str, str]):
    for key, value in args.items():
        template = template.replace(f"{{{{{key}}}}}", value)
    return template
