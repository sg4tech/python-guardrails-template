"""Fixture: every construct the composition-root rule rejects, one per flagged line."""

from typing import Any


def wiring(value: Any, items: Any, errors: Any) -> Any:
    if value:
        pass
    for item in items:
        del item
    while value:
        break
    try:
        pass
    except errors:
        value = errors
    try:
        pass
    finally:
        pass
    match value:
        case 1:
            pass
    with value:
        pass
    selected = value if items else errors
    listed = [item * 2 for item in items]
    unique = {item * 2 for item in items}
    mapped = {item: item for item in items}
    generated = (item for item in items)
    either = value or items
    both = value and items
    assert value
    raise errors
    return selected, listed, unique, mapped, generated, either, both


def produce(items: Any) -> Any:
    yield items


class Service:
    pass


def more_wiring(items: Any, rows: Any, errors: Any) -> Any:
    try:
        pass
    except errors:
        items = errors
    else:
        pass
    filtered = [item for item in items if item]
    nested = [cell for row in rows for cell in row]
    unique = {item * 2 for item in items if item}
    mapped = {item: item for item in items if item}
    generated = (item for item in items if item)
    counted = (count := len(items))
    return filtered, nested, unique, mapped, generated, counted, count


def even_more_wiring(items: Any, rows: Any, errors: Any) -> Any:
    try:
        pass
    except errors:
        items = errors
    else:
        pass
    finally:
        pass
    unique = {cell for row in rows for cell in row}
    mapped = {cell: row for row in rows for cell in row}
    generated = (cell for row in rows for cell in row)
    filtered = [item for item in items if item if errors]
    return unique, mapped, generated, filtered
