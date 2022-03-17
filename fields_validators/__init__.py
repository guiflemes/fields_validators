from .cpf_validator import CPFValidator
from .cnpj_validator import CNPJValidator
from .email_validator import EmailValidator
from .options_validator import OptionsValidator
from .regex_validator import RegexValidator
from .type_validator import TypeValidator
from .string_validator import StrValidator
from .uuid_validator import UUIDValidator

__version__ = '0.1.4'

__all__ = [
    "CPFValidator",
    "CNPJValidator",
    "EmailValidator",
    "OptionsValidator",
    "RegexValidator",
    "TypeValidator",
    "StrValidator",
    "UUIDValidator",
    "__version__",
]
