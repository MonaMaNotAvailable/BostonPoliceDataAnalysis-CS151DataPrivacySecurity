#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3



### 1. Import ###

import pandas as pd
# The vetting process is currently underway for the code in the OpenDP Library. Any constructors that have not been vetted may still be accessed if you opt-in to "contrib".
import opendp.prelude as dp
dp.enable_features('contrib')



### 2. SetUp ###

# Read the CSV file into a DataFrame
df = pd.read_csv('../DatasetForPrivacy/officers_employees.csv')
# Print the 'total' column
# print(df['total'])

# # Get the number of rows
# number_of_rows = len(df)
# print(number_of_rows)

# # Load the CSV file
# df1 = pd.read_csv('../DatasetForPrivacy/PersonShot.csv')
# number_of_rows1 = len(df1)
# print(number_of_rows1)

# Get the column names as a list
col_names = df.columns.tolist()
# establish public information: col_names
# print(col_names) #The output is :
# ['url', 'employee_id', 'badge', 'name', 'title', 'org_url', 'organization', 'doa', 'total', 'regular', 'retro', 'other', 'overtime', 'injured', 'detail', 'quinn', 'details_count', 'articles_officers_count', 'articles_officers_to_review_count', 'ia_score', 'field_contacts_count', 'incidents_count', 'swats_count', 'citations_count', 'postal', 'state', 'neighborhood']

# the greatest number of records that any one individual can influence in the dataset
max_influence = 1

total_bounds = (0, 370000)



### 3. Load CSV files ###

income_preprocessor = (
    # Convert data into a dataframe where columns are of type Vec<str>
    dp.t.make_split_dataframe(separator=",", col_names=col_names) >>
    # The column name is off by 1 because of the "," in name, therefore instead of using "total", we use "regular"
    dp.t.make_select_column(key="regular", TOA=str)
)

# Convert DataFrame to CSV string (without index and header)
data = df.to_csv(index=False, header=False)

# check the first entry
# print('\n'.join(data.split('\n')[:1]))

transformed = income_preprocessor(data)
# print(type(transformed))
print(transformed[:6])



### 4. Casting from str to float ###

# make a transformation that casts from a vector of strings to a vector of floats
cast_str_float = (
    # start with the output space of the income_preprocessor
    income_preprocessor.output_space >>
    # cast Vec<str> to Vec<Option<float>>
    dp.t.then_cast(TOA=float) >>
    # Replace any elements that failed to parse with 0, emitting a Vec<float>
    dp.t.then_impute_constant(0.0)
)

# replace the previous preprocessor: extend it with the caster
income_preprocessor = income_preprocessor >> cast_str_float
print(income_preprocessor(data)[:6])



#TODO: explore the SQL queries instead of Python codes

# ###Private Count###
# count = income_preprocessor >> dp.t.then_count()
# # NOT a DP release!
# count_response = count(data)

# dp_count = count >> dp.m.then_base_discrete_laplace(scale=1.)

# # estimate the budget...
# epsilon = dp.binary_search(
#     lambda eps: dp_count.check(d_in=max_influence, d_out=eps),
#     bounds=(0., 100.))
# print("DP count budget:", epsilon)

# # ...and then release
# count_release = dp_count(data)
# print("DP count:", count_release)



# ###Private Sum###

# bounded_income_sum = (
#     income_preprocessor >>
#     # clamp income values. 
#     # "then_*" means it uses the output domain and output metric from the previous transformation
#     dp.t.then_clamp(bounds=income_bounds) >>
#     # similarly, here we use "then_sum" to avoid needing to specify the input space.
#     # the sum constructor gets told that the input consists of bounded data
#     dp.t.then_sum()
# )

# discovered_scale = dp.binary_search_param(
#     lambda s: bounded_income_sum >> dp.m.then_base_discrete_laplace(scale=s),
#     d_in=max_influence,
#     d_out=1.)

# dp_sum = bounded_income_sum >> dp.m.then_base_discrete_laplace(scale=discovered_scale)

# dp_sum = dp.binary_search_chain(
#     lambda s: bounded_income_sum >> dp.m.then_base_discrete_laplace(scale=s),
#     d_in=max_influence,
#     d_out=1.)

# # ...and make our 1-epsilon DP release
# print("DP sum:", dp_sum(data))



# ###Private Mean###

# try:
#     mean_age_preprocessor = (
#         # Convert data into a dataframe of string columns
#         dp.t.make_split_dataframe(separator=",", col_names=col_names) >>
#         # Selects a column of df, Vec<str>
#         dp.t.make_select_column(key="age", TOA=str) >>
#         # Cast the column as Vec<float>, and fill nulls with the default value, 0.
#         dp.t.then_cast_default(TOA=float) >>
#         # Clamp age values
#         dp.t.then_clamp(bounds=age_bounds)
#     )
# except TypeError as err:
#     assert str(err).startswith("inferred type is") # type: ignore
#     print(err)

# float_age_bounds = tuple(map(float, age_bounds))

# dp_mean = (
#     # Convert data into a dataframe of string columns
#     dp.t.make_split_dataframe(separator=",", col_names=col_names) >>
#     # Selects a column of df, Vec<str>
#     dp.t.make_select_column(key="age", TOA=str) >>
#     # Cast the column as Vec<float>, and fill nulls with the default value, 0.
#     dp.t.then_cast_default(TOA=float) >>
#     # Clamp age values
#     dp.t.then_clamp(bounds=float_age_bounds) >>
#     # Resize the dataset to length `count_release`.
#     #     If there are fewer than `count_release` rows in the data, fill with a constant of 20.
#     #     If there are more than `count_release` rows in the data, only keep `count_release` rows
#     dp.t.then_resize(size=count_release, constant=20.) >>
#     # Compute the mean
#     dp.t.then_mean() >>
#     # add laplace noise
#     dp.m.then_laplace(scale=1.0)
# )

# mean_release = dp_mean(data)
# print("DP mean:", mean_release)