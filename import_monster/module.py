import builtins
import importlib
from types import ModuleType
from typing import List, Union, Callable

import scipy


def methods_importer(method_name: str, modules: List[Union[str, ModuleType]]) -> List[Callable]:
    lis_t = []
    for module in modules:
        try:
            if isinstance(module, (ModuleType, Callable)):
                mod = module
            elif isinstance(module, (str, Callable)):
                mod = importlib.import_module(module)

            else:
                raise TypeError('Must be a list of strings or ModuleType')
            met = getattr(mod, method_name, None)
            if met:
                lis_t.append(mod)
        except ImportError:
            continue
    return lis_t

print(methods_importer("sum", [builtins]))