# Violates GitlabChecker1: Line length exceeds 80 characters
this_is_a_very_long_variable_name_that_exceeds_80_characters = "This is a long line that exceeds the maximum length of 80 characters"

# Violates GitlabChecker2: Contains ".printStackTrace()"
try:
    some_function_that_might_raise_an_exception()
except Exception as e:
    print(e.printStackTrace())

# Violates GitlabChecker3: Contains '@Value("${' without ':'
@Value("${some_value}")
private String someProperty;

# Violates GitlabChecker4: Contains 'Turbonomic', 'CWOM', or 'IWO'
localized_string = "This is a Turbonomic localized string."

# Violates GitlabChecker5: Proto file with required and repeated fields
message Person {
    required string name = 1;
    repeated string emails = 2;
    optional int32 age = 3;
}
