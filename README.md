## Package validator

package fields_validators implements validations for class attributes.

It has the following unique features that validates whether the attribute is:

* Specific type.
* Email field.
* CPF or CNPJ field.
* Field among some options.
* String between some predefined length.
* Regex match.

## Installation

```pip install fields-validators```

## How to Use

```python
@dataclasses.dataclass
class Company:
    cpf_cnpj: str = CPFValidator()
    street: str = StrValidator("street", 1, 20)
    email_admin: str = EmailValidator("email_admin")
```

