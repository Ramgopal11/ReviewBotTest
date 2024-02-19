# This code violates the "line size checker" rule by exceeding 80 characters per line
def calculate_really_long_function_name_that_exceeds_80_characters(a_really_long_argument_name_that_exceeds_80_characters,
                                                                  another_really_long_argument_name_that_exceeds_80_characters):
    result = a_really_long_argument_name_that_exceeds_80_characters * \
             another_really_long_argument_name_that_exceeds_80_characters
    return result

# This code violates the "printStackTrace" rule by using printStackTrace instead of logging
try:
    # Some code that might raise an exception
    raise Exception("An error occurred")
except Exception as e:
    e.printStackTrace()

# This code violates the "springDefaultValue" rule by using a Spring @Value annotation without a default value
import org.springframework.beans.factory.annotation.Value

@Value("someValue")
def some_function():
    pass

# This code violates the "TurboInString" rule by using "Turbonomic" in a localization file
localization_string = "Welcome to Turbonomic!"

# This code violates the "Protobuf" rule by not including a description for the protobuf import
import protobuf
