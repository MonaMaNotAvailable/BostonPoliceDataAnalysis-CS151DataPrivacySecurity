from opendp.transformations import *
from opendp.domains import option_domain, atom_domain
from opendp.mod import enable_features
enable_features('contrib') # we are using un-vetted constructors

num_tests = 3  # d_in=symmetric distance; we are told this is public knowledge
budget = 1. # d_out=epsilon

num_students = 50  # we are assuming this is public knowledge
size = num_students * num_tests  # 150 exams
bounds = (0., 100.)  # range of valid exam scores- clearly public knowledge
constant = 70. # impute nullity with a guess

transformation = (
    make_split_dataframe(',', col_names=['Student', 'Score']) >>
    make_select_column(key='Score', TOA=str) >>
    then_cast(TOA=float) >>
    then_impute_constant(constant=constant) >>
    then_clamp(bounds) >>
    then_resize(size, constant=constant) >>
    then_mean()
)