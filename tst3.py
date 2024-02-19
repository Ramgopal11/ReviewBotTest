# Violates GitlabChecker1: Line length exceeds 80 characters
characters = "This is a long line"

# Violates GitlabChecker2: Contains ".()"
try:
    some_function_that_might_raise_an_exception()
except Exception as e:
    print(e.p())

# Violates GitlabChecker3: Contains '@Value("${' without ':'
private String someProperty;

# Violates GitlabChecker4: Contains '', '', or ''
localized_string = "This is a localized string."

# Violates GitlabChecker5: Proto file with required and repeated fields
message Person {
    optional int32 age = 3;
}
